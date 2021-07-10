from app.loader import config
from app.utils.qiwi_api.qiwi_api import QiwiWallet

qiwi_wallet = QiwiWallet(qiwi_token=config.qiwi.token)
