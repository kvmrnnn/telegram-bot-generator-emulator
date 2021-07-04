from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    admin_id: int
    chats_id: list
    commands: dict


@dataclass
class DatabaseConfig:
    host: str
    port: int
    db: str
    db_user: str
    db_pass: str
    url: str


@dataclass
class Config:
    bot: BotConfig
    database: DatabaseConfig
