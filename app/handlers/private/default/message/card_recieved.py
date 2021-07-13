from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, Message

from app.keyboards.default import inline, reply
from app.loader import dp
from app.filters import CardFilter
from app.states.private.choose_card import ChooseCard


@dp.message_handler(CardFilter())
@dp.message_handler(CardFilter(), content_types=ContentTypes.DOCUMENT)
async def choose_card_type(message: Message, state: FSMContext, cards_data: dict, lang_code):
    await message.answer(
        text='Выберите тип карты',
        reply_markup=reply.choose_card.make_keyboard(lang_code)
    )
    await state.update_data(cards_data=cards_data)
    await ChooseCard.wait_for_type.set()
