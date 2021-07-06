from loguru import logger

from app.loader import dp
from app.middlewares.getting_state_data import StateDataMiddleware
from app.middlewares.getting_user_from_db import GettingUserFromDataBaseMiddleware

logger.info(f'Setup middleware')
dp.setup_middleware(GettingUserFromDataBaseMiddleware())
dp.setup_middleware(StateDataMiddleware())
