import urllib.parse as urlparse
from typing import Dict, List
from urllib.parse import parse_qs

from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeVideo:
    """A YouTube video with its transcript."""

    def __init__(self, url_or_id: str):
        self.id = self._get_youtube_id(url_or_id)
        self.transcript = self._get_transcript()
        self.text = self._get_text_string()
        self.duration = self._get_duration()

    def _get_youtube_id(self, arg: str) -> str:
        if "youtube" in arg:
            parsed = urlparse.urlparse(arg)
            youtube_id = parse_qs(parsed.query)["v"][0]
        else:
            youtube_id = arg
        return youtube_id

    def _get_transcript(self) -> List[Dict]:
        transcript = YouTubeTranscriptApi.get_transcript(self.id)
        return transcript
        
    def _get_text_string(self):
        subs_list = []
        for subs in self.transcript:
            subtitle_text = subs["text"]
            subs_list.append(subtitle_text.replace('\n', ' '))
        text = " ".join(subs_list)
        return text

    def _get_duration(self) -> float:
        last_transcript_item = self.transcript[-1]
        duration = last_transcript_item["start"] + last_transcript_item["duration"]
        return round(duration, 2)

if __name__ == '__main__':
    print('url: https://www.youtube.com/watch?v=Hu4Yvq-g7_Y')
    youtube = YoutubeVideo('https://www.youtube.com/watch?v=Hu4Yvq-g7_Y')
    print(youtube.text)
