from dataclasses import dataclass


@dataclass
class MiscLinks:
    pass


@dataclass
class PhotoLinks:
    pass


@dataclass
class VideoLinks:
    read_rules: str


@dataclass
class DocumentLinks:
    pass


@dataclass
class TelegraphLinks:
    bot_rules: str


@dataclass
class Links:
    misc: MiscLinks
    photo: PhotoLinks
    video: VideoLinks
    document: DocumentLinks
    telegraph: TelegraphLinks
