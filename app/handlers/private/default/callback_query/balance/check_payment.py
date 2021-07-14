from aiogram.types import CallbackQuery

from app.data import text
from app.data.types.menu_cd import MenuProfileCd
from app.keyboards.default.callback_data.profile.main_profile import payment_cd
from app.loader import dp, config
from app.utils.qiwi_api import qiwi_wallet


@dp.callback_query_handler(payment_cd.filter(command=MenuProfileCd.check_payment))
async def check_payment(call: CallbackQuery, callback_data: dict, lang_code, user):
    comment = callback_data.get('comment')
    payment = await qiwi_wallet.get_transaction(comment)
    if not payment:
        await call.answer(
            show_alert=True,
            cache_time=60,
            text=text[lang_code].message.default.payment_qiwi_not_found.format(
                qiwi_wallet=qiwi_wallet.number,
                comment=comment
            )
        )
        return False
    await user.update_balance(payment.total.amount)
    await call.answer(text=text[lang_code].message.default.balance_replenished, cache_time=900)
