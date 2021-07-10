from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.goods import GoodsType
from app.keyboards.default.callback_data.buying_goods import buying_cd
from app.utils.parse_data.prices import ParserPrice


def keyboard(lang_code: str):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.default.inline.buy_premium_week.format(
                        price=ParserPrice.get_price(GoodsType.PREMIUM_WEEK, 299)
                    ),
                    callback_data=buying_cd.new(
                        goods_type=GoodsType.PREMIUM_WEEK,
                        price=ParserPrice.get_price(GoodsType.PREMIUM_WEEK, 299)
                    )
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.default.inline.buy_premium_week.format(
                        price=ParserPrice.get_price(GoodsType.PREMIUM_MONTH, 899)
                    ),
                    callback_data=buying_cd.new(
                        goods_type=GoodsType.PREMIUM_MONTH,
                        price=ParserPrice.get_price(GoodsType.PREMIUM_MONTH, 899)
                    )
                )
            ]
        ]
    )
    return markup
