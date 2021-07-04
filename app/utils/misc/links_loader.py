import configparser

from loguru import logger

from app.data.links import Links, MiscLinks, TelegraphLinks, PhotoLinks, VideoLinks, DocumentLinks


class LinksLoader:

    def __init__(self, path_to_links: str):
        logger.info(f'Config: Read Config')
        self._path_to_links = path_to_links
        self._links = configparser.ConfigParser()

        self._links.read(self._path_to_links)

    def get_links(self) -> Links:
        links = Links(
            misc=self._get_misc_links(),
            photo=self._get_photo_links(),
            video=self._get_video_links(),
            document=self._get_document_links(),
            telegraph=self._get_telegraph_links(),
        )
        return links

    def _get_misc_links(self) -> MiscLinks:
        links = MiscLinks(

        )
        return links

    def _get_photo_links(self) -> PhotoLinks:
        links = PhotoLinks(

        )
        return links

    def _get_video_links(self) -> VideoLinks:
        links = VideoLinks(
            read_rules=self._links['VideoLinks']['read_rules']
        )
        return links

    def _get_document_links(self) -> DocumentLinks:
        links = DocumentLinks(

        )
        return links

    def _get_telegraph_links(self) -> TelegraphLinks:
        links = TelegraphLinks(
            bot_rules=self._links['TelegraphLinks']['bot_rules']
        )
        return links




