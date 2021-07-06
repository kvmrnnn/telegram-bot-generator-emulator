from aiogram.types import CallbackQuery

from app import dp
from app.data import text
from app.data.types.menu_cd import MenuSettingsCD
from app.keyboards.default.callback_data.settings_profile import menu_settings_cd


@dp.callback_query_handler(menu_settings_cd.filter(menu=MenuSettingsCD.upload_user_data))
async def upload_user_data(call: CallbackQuery, user, lang_code):
    await call.answer(
        text=text[lang_code].message.default.soon,
        cache_time=5
    )