from aiogram.types import CallbackQuery

from app.data.types.menu_cd import MenuProfileCd
from app.keyboards.default.callback_data.profile.main_profile import payment_cd
from app.loader import dp


@dp.callback_query_handler(payment_cd.filter(command=MenuProfileCd.check_payment))
async def check_payment(call: CallbackQuery):
    await call.answer('One moment..', cache_time=5)
    await call.message.answer(
        text='yes'
    )
