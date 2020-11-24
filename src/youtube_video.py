import urllib.parse as urlparse
from typing import Dict, List
from urllib.parse import parse_qs

from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeVideo:
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
        return transcript

    def _get_duration(self) -> float:
        last_transcript_item = self.transcript[-1]
        duration = last_transcript_item["start"] + last_transcript_item["duration"]
        return round(duration, 2)

    def split(self, n_parts=10) -> List[float]:
        n_parts = n_parts + 1  # to get n_parts, we need n_parts + 1 time stamps
        part_duration = self.duration / n_parts
        parts = []
        for i in range(n_parts):
            if i == 0:
                parts.append(0)
            else:
                parts.append(round(parts[i - 1] + part_duration, 2))
        return parts

    def segmentize(self, n_parts=10) -> List[Dict]:
        segments = []  # [{"segment_number": 1, "start_time": 150.8}]
        approximate_splits = self.split(n_parts=n_parts)
        temp_transcript = self.transcript

        def get_closest_segment(
            index: int,
            approximate_split: List[int],
            temp_transcript: List[Dict],
        ):
            segment = {"segment_number": index}
            if index == 0:
                segment["starts_at_index"] = 0
                return segment
            smallest_delta = float("inf")
            for transcript_index, transcript_item in enumerate(temp_transcript):
                current_delta = abs(approximate_split - transcript_item["start"])
                if current_delta < smallest_delta:
                    smallest_delta = current_delta
                else:
                    # Take previous transcript item that had the smallest delta
                    segment["starts_at_index"] = transcript_index
                    return segment

        skipped_indices = 0
        for index, approximate_split in enumerate(approximate_splits):
            segment = get_closest_segment(index, approximate_split, temp_transcript)
            segments.append(segment)
        return segments
