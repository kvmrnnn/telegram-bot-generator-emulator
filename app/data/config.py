from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    admins_channel: int

@dataclass
class Config:
    bot: BotConfig
