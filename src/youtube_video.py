import urllib.parse as urlparse
from typing import Dict, List
from urllib.parse import parse_qs
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from punctuator import Punctuator

model = str(Path("punctuator/INTERSPEECH-T-BRNN.pcl").resolve())
punctuator_model = Punctuator(model)  # use pretrained model


class YoutubeVideo:
    """A YouTube video with its transcript."""

    def __init__(self, url_or_id: str):
        self.id = self._get_youtube_id(url_or_id)
        self.transcript = self._get_transcript()
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
        transcript_list = YouTubeTranscriptApi.list_transcripts(self.id)
        print("transcript: ", transcript)
        try:
            transcript_list.find_manually_created_transcript(["en"])
        except:
            punctuated_transcript = self._punctuate(transcript)

            return punctuated_transcript

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
        global punctuator_model

        text_string = self._get_text_string(transcript)

        punctuated_text = punctuator_model.punctuate(text_string)
        punctuated_list = [token for token in punctuated_text.split(" ")]

        i = 0
        for line in transcript:
            line_length = len(line["text"].split(" "))
            line["text"] = " ".join(punctuated_list[i : i + line_length])
            i += line_length

        return transcript
