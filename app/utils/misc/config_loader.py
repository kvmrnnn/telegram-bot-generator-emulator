import configparser

from loguru import logger

from app.data.types.config import BotConfig, Config, DatabaseConfig, QiwiConfig


class ConfigLoader:

    def __init__(self, path_to_config: str):
        logger.info(f'Config: Read Config')
        self._path_to_config = path_to_config
        self._config = configparser.ConfigParser()

        self._config.read(self._path_to_config)

    @property
    def get_config(self) -> Config:
        config = Config(
            self._get_bot_config,
            self._get_database_config,
            self._get_qiwi_config
        )
        return config

    @property
    def get_bot_commands(self):
        return dict(self._config['BotCommands'])

    @property
    def _get_qiwi_config(self) -> QiwiConfig:
        qiwi_config = QiwiConfig(
            self._config['QiwiConfig']['token'],
            int(self._config['QiwiConfig']['comment_length']),
            int(self._config['QiwiConfig']['min_amount_withdraw']),
            int(self._config['QiwiConfig']['commission_amount']),
            int(self._config['QiwiConfig']['commission_percent']),
        )
        return qiwi_config

    @property
    def _get_bot_config(self) -> BotConfig:
        bot_config = BotConfig(
            self._config['BotConfig']['token'],
            self._config['BotConfig']['default_lang'],
            self._config['BotConfig']['second_lang'] or self._config['BotConfig']['default_lang'],
            int(self._config['BotConfig']['admin_id']),
            [int(chat_id) for chat_id in self._config['BotConfig']['chats_id'].split()],
            self.get_bot_commands,
            int(self._config['BotConfig']['generate_limit_default']),
        )
        return bot_config

    @property
    def _get_database_config(self) -> DatabaseConfig:
        host = self._config['DatabaseConfig']['host']
        port = self._config['DatabaseConfig']['port']
        db = self._config['DatabaseConfig']['db']
        db_user = self._config['DatabaseConfig']['db_user']
        db_pass = self._config['DatabaseConfig']['db_pass']
        database_config = DatabaseConfig(
            host,
            port,
            db,
            db_user,
            db_pass,
            f'postgresql://{db_user}:{db_pass}@{host}:{port}/{db}',
        )
        return database_config
