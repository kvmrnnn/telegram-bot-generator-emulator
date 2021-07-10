import datetime as dt
from typing import List
from uuid import uuid4

from pyqiwi import Wallet
from pyqiwi.types import Transaction, OnlineCommission

from app.loader import config


class QiwiWallet(Wallet):

    def __init__(self, qiwi_token: str):
        if config.qiwi.comment_length < 5:
            raise ValueError('Минимальная длина комментария 5 символов')
        if config.qiwi.comment_length > 32:
            raise ValueError('Максимальная длина комментария 32 символа')
        super().__init__(token=qiwi_token)

    async def withdraw(self, phone_or_card: str, amount: float, calc_commission: bool = False) -> dict:
        """
        Вывод на карту или телефон c учетом коммисии qiwi.
        :param phone_or_card: Номер телефона или номер карты.
        :param amount: Сумма перевода.
        """
        if amount < config.qiwi.min_amount_withdraw:
            raise ValueError('Сумма перевода меньше минимальной')

        commission = await self.calc_commission(phone_or_card, amount)

        if calc_commission:
            amount = amount - commission

        comment = self.generate_comments()

        transaction_data = {
            'wallet_number': self.number,
            'comment': comment,
            'user_wallet_account': phone_or_card,
            'commission': round(float(commission), 1),
            'amount': amount
        }

        self.qiwi_transfer(phone_or_card, amount, comment)
        return transaction_data

    async def get_transaction(self, comment: str) -> Transaction:
        """
        Возвращает данные найденной транзакции по комментарию
        """
        transactions = await self.get_transactions()
        for transaction in transactions:
            if transaction.comment == comment and transaction.status == 'SUCCESS':
                return transaction

    async def get_transactions(self, days: int = 3) -> List[Transaction]:
        """
        Возвращает список транзанкций(максимум 50)
        """
        start_date = dt.datetime.now() - dt.timedelta(days=days)
        transactions = self.history(start_date=start_date).get('transactions')
        return transactions

    async def calc_commission(self, phone_or_card: str, amount: float, commission_amount: float = None,
                              commission_percent: int = None) -> float:
        """Расчет комиссии с учетом настроек проекта"""
        commission_qiwi: OnlineCommission = self.commission('99', phone_or_card, amount).qw_commission.amount

        commission_amount = commission_amount or config.qiwi.commission_amount
        commission_percent = commission_percent or config.qiwi.commission_percent

        commission_fix = commission_amount + (amount / 100 * commission_percent)
        commission = commission_qiwi + commission_fix
        return round(commission, 1)

    def generate_comments(self) -> str:
        """
        Генерирует рандомную строку из 32 символом и возвращает ее срез
        """
        uuid: str = str(uuid4())
        comment: str = ''.join(uuid.split('-'))

        return comment[:config.qiwi.comment_length]
