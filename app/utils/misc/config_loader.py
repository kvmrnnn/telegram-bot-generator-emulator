import configparser

from app.data.config import BotConfig, Config


class ConfigLoader:

    def __init__(self, path_to_config: str):
        self._path_to_config = path_to_config
        self._config = configparser.ConfigParser()

        self._config.read(self._path_to_config)


    def _get_bot_config(self) -> BotConfig:
        bot_config = BotConfig(
            self._config['BotConfig']['token'],
            self._config['BotConfig']['admins_channel'],
        )
        return bot_config

    def get_config(self) -> Config:
        config = Config(
            self._get_bot_config()
        )
        return config


