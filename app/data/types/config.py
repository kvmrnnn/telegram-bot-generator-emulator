from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    default_lang: str
    second_lang: str
    admin_id: int
    chats_id: list
    commands: dict
    generate_limit_default: int


@dataclass
class DatabaseConfig:
    host: str
    port: int
    db: str
    db_user: str
    db_pass: str
    url: str


@dataclass
class QiwiConfig:
    token: str
    comment_length: int
    min_amount_withdraw: int
    commission_amount: int
    commission_percent: int


@dataclass
class Config:
    bot: BotConfig
    database: DatabaseConfig
    qiwi: QiwiConfig
