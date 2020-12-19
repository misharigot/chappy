from data_objects.youtube_video import YoutubeVideo
from data_objects.chapter import Chapter
from typing import List


class ChapterizedYoutubeVideo:
    """A YoutubeVideo with a list of Chapters.
    """
    def __init__(self, youtube_video: YoutubeVideo, chapters):
        self.youtube_video = youtube_video
        self.chapters: List[Chapter] = chapters

    def print_chapters(self):
        if self.chapters is None:
            print("No chapters found.")

        print(f"Chapters for video : https://www.youtube.com/watch?v={self.youtube_video.id}\n-----\n")
        for chapter in self.chapters:
            print(chapter)
