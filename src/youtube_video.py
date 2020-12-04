import urllib.parse as urlparse
from typing import Dict, List
from urllib.parse import parse_qs
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from punctuator import Punctuator

MODEL = str(Path("/app/chappy/punctuator/INTERSPEECH-T-BRNN.pcl").resolve())
punctuator_model = Punctuator(MODEL)  # use pretrained model


class YoutubeVideo:
    """A YouTube video with its transcript."""

    def __init__(self, url_or_id: str):
        self.id = self._get_youtube_id(url_or_id)
        self.bla = YouTubeTranscriptApi.get_transcript(self.id)
        self.transcript = self._get_transcript()
        self.duration = self._get_duration()

    def _get_youtube_id(self, arg: str) -> str:
        if "youtube" in arg:
            parsed = urlparse.urlparse(arg)
            youtube_id = parse_qs(parsed.query)["v"][0]
        else:
            youtube_id = arg
        return youtube_id

    def _has_manually_created_transcript(self):
        transcript_list = YouTubeTranscriptApi.list_transcripts(self.id)
        try:
            transcript_list.find_manually_created_transcript(["en"])
        except Exception:
            return False
        return True

    def _get_transcript(self) -> List[Dict]:
        transcript = YouTubeTranscriptApi.get_transcript(self.id)
        if not self._has_manually_created_transcript():
            return self._punctuate(transcript)
        return transcript

    def _get_duration(self) -> float:
        last_transcript_item = self.transcript[-1]
        duration = last_transcript_item["start"] + last_transcript_item["duration"]
        return round(duration, 2)

    def _get_text_string(self, transcript):
        subs_list = []
        for subs in transcript:
            subs_list.append(subs["text"])
            text = " ".join(subs_list)
        return text

    def _punctuate(self, transcript) -> List[Dict]:
        # global punctuator_model

        text_string = self._get_text_string(transcript)

        punctuated_text = punctuator_model.punctuate(text_string)
        punctuated_list = [token for token in punctuated_text.split(" ")]

        i = 0
        for non_punctuated_line in transcript:
            n_tokens = len(non_punctuated_line["text"].split(" "))
            punctuated_tokens = punctuated_list[i : i + n_tokens]
            punctuated_line = " ".join(punctuated_tokens)
            non_punctuated_line["text"] = punctuated_line
            i += n_tokens

        return transcript
