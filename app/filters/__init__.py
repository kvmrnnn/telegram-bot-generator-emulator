from loguru import logger

from app.filters.private.message.card import CardFilter
from app.filters.private.message.promocode import PromocodeFilter
from app.filters.private.user.is_premium import IsPremiumFilter
from app.filters.private.user.not_subscriber import NotSubscribedChat
from app.filters.private.user.user_role import UserRoleFilter
from app.loader import dp

dp.filters_factory.bind(NotSubscribedChat)
dp.filters_factory.bind(UserRoleFilter)
dp.filters_factory.bind(CardFilter)
dp.filters_factory.bind(PromocodeFilter)
dp.filters_factory.bind(IsPremiumFilter)


logger.info(f'Setup filter')
