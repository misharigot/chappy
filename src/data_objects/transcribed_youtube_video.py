from data_objects.youtube_video import YoutubeVideo


class TranscribedYoutubeVideo(YoutubeVideo):
    def __init__(self, url_or_id, transcript):
        super().__init__(url_or_id)
        self.transcript = transcript
        self.duration = self._get_duration()

    def _get_duration(self) -> float:
        last_transcript_item = self.transcript[-1]
        duration = last_transcript_item["start"] + last_transcript_item["duration"]
        return round(duration, 2)
