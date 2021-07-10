from aiogram.types import CallbackQuery

from app.data import text
from app.data.types.menu_cd import MenuProfileCd
from app.keyboards.default import inline
from app.keyboards.default.callback_data.profile.main_profile import profile_cd
from app.loader import dp, config
from app.utils.qiwi_api import qiwi_wallet


@dp.callback_query_handler(profile_cd.filter(command=MenuProfileCd.increase_balance))
async def ask_for_payment(call: CallbackQuery, lang_code):
    await call.answer(text='One moment...', cache_time=5)
    comment = qiwi_wallet.generate_comments()
    await call.message.answer(
        text=text[lang_code].message.default.qiwi_payment_data.format(
            qiwi_wallet=config.qiwi.token,
            comment=comment
        ),
        reply_markup=inline.check_payment.make_keyboard_check_payment(lang_code=lang_code, comment=comment)
    )
