from typing import Dict, List

from youtube_transcript_api import YouTubeTranscriptApi

from punctuator_model_provider import PunctuatorModelProvider


class Transcriber:
    def __init__(self):
        self.punctuator_model_provider: PunctuatorModelProvider = PunctuatorModelProvider()

    def get_transcript(self, youtube_video_id) -> List[Dict]:
        transcript = YouTubeTranscriptApi.get_transcript(youtube_video_id)
        if not self._has_manually_created_transcript(youtube_video_id):
            return self._punctuate(transcript)
        return transcript
    
    def _has_manually_created_transcript(self, youtube_video_id):
        transcript_list = YouTubeTranscriptApi.list_transcripts(youtube_video_id)
        try:
            transcript_list.find_manually_created_transcript(["en"])
        except Exception:
            return False
        return True

    def _get_text_string(self, transcript):
        subs_list = []
        for subs in transcript:
            subs_list.append(subs["text"])
            text = " ".join(subs_list)
        return text

    def _punctuate(self, transcript) -> List[Dict]:
        # global punctuator_model

        text_string = self._get_text_string(transcript)

        punctuator_model = self.punctuator_model_provider.get_punctuator_model()
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
