from uuid import uuid4

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data.types.tmp_files import TextFile
from app.loader import dp
from app.states.private.create_promo_code import CreatePromoCode
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.promocode_model import Promocode


@dp.message_handler(state=CreatePromoCode.wait_for_data)
@dp.message_handler(state=CreatePromoCode.wait_for_data)
async def create_promo_codes(message: Message, state: FSMContext, user):
    if not message.text.replace(' ', '').isdigit() or len(message.text.split()) != 3:
        await message.answer(
            text='Wrong data'
        )
        return False
    bot_data = await dp.bot.get_me()
    days, hours, count = map(int, message.text.split())
    if (days == 0 or hours == 0 or days > 999 or hours > 999) and (count == 0 or count > 20) :
        await message.answer(
            text='Wrong data'
        )
        return False
    file = TextFile()
    promocodes = ''
    prom_urls = ''
    await send_main_keyboard(user, state)
    for i in range(count):
        promo_code = str(uuid4())
        prom_url = f'<a href="t.me/{bot_data.username}?start={promo_code}"> Promocode: {days}d {hours}h</a>\n'
        promocodes += f"{promo_code}: {days}d {hours}h\n"
        prom_urls += prom_url
        await Promocode.insert(
            code=promo_code,
            premium_datetime=f"{days} {hours}",
            creator_user_id=message.from_user.id
        )
    file.write_text(promocodes)
    await message.answer_document(
        document=file.input_file,
        caption=prom_urls
    )
    await send_main_keyboard(user, state)
