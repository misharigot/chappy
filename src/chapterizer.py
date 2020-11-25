from typing import List, Optional

from chapter import Chapter
from simple_segmentizer import SimpleSegmentizer
from summarizer import Summarizer
from youtube_video import YoutubeVideo


class Chapterizer:
    """Able to chapterize a YoutubeVideo. A chapter is a segment and its summary."""

    def __init__(self, url, summary_word_count):
        self.url = url
        self.youtube_video: YoutubeVideo = YoutubeVideo(url)
        self.segmentizer = SimpleSegmentizer(self.youtube_video)
        self.summarizer = Summarizer(word_count=summary_word_count)
        self.chapters: Optional[List[Chapter]] = None

    def chapterize(self) -> None:
        print(f"Processing: {self.url}")
        chapters = []
        for segment in self.segmentizer.generate_segments():
            summary = self.summarizer.summarize(segment.get_text())
            chapter = Chapter(segment=segment, summary=summary)
            chapters.append(chapter)
        self.chapters = chapters
        print("Successfully chapterized!\n")

    def print(self):
        if self.chapters is None:
            print("No chapters found.")

        print(f"Chapters for video: {self.url}\n-----\n")
        for chapter in self.chapters:
            print(chapter)
