import urllib.parse as urlparse
from urllib.parse import parse_qs

# from transcriber import Transcriber


class YoutubeVideo:
    """A YouTube video with its transcript."""

    def __init__(self, url_or_id: str):
        self.id = self._get_youtube_id(url_or_id)

    def _get_youtube_id(self, arg: str) -> str:
        if "youtube" in arg:
            parsed = urlparse.urlparse(arg)
            youtube_id = parse_qs(parsed.query)["v"][0]
        else:
            youtube_id = arg
        return youtube_id
