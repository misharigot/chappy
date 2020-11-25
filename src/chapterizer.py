from typing import List, Optional

from chapter import Chapter
from simple_segmentizer import SimpleSegmentizer
from summarizer import Summarizer
from youtube_video import YoutubeVideo
# from segment import Segment


class Chapterizer:
    """Able to chapterize a YoutubeVideo. A chapter is a segment and its summary."""

    def __init__(self, url):
        self.youtube_video: YoutubeVideo = YoutubeVideo(url)
        self.segmentizer = SimpleSegmentizer(self.youtube_video)
        self.summarizer = Summarizer()
        self.chapters: Optional[List[Chapter]] = None

    def chapterize(self) -> None:
        print(f"Processing: {self.youtube_video.id}\n")
        chapters = []
        for segment in self.segmentizer.generate_segments():
            summary = self.summarizer.summarize(segment.get_text())
            chapter = Chapter(segment=segment, summary=summary)
            chapters.append(chapter)
        self.chapters = chapters

    def print(self):
        if self.chapters is None:
            print("No chapters found.")
        # print(youtube_video.segmentize())
        # index = youtube_video.segmentize()[-1]["starts_at_index"]
        # print("\nlast transcript item:\n", youtube_video.transcript[index])
        # print("\nnumber of items in transcript:\n", len(youtube_video.transcript))
        print("Chapters found, cannot print as this has not been implemented yet.")
