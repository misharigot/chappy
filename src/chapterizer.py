from data_objects.chapter import Chapter
from data_objects.chapterized_youtube_video import ChapterizedYoutubeVideo
from data_objects.transcribed_youtube_video import TranscribedYoutubeVideo
from data_objects.youtube_video import YoutubeVideo
from segmentizers.sentence_similarity_segmentizer import SentenceSimilaritySegmentizer
from summarizers.bart_summarizer import BartSummarizer
from transcriber import Transcriber


class Chapterizer:
    """Able to chapterize a YoutubeVideo. A chapter is a segment and its summary."""

    def __init__(self, summary_word_count=30, number_of_chapters=10):
        self.transcriber = Transcriber()
        self.segmentizer = SentenceSimilaritySegmentizer()
        self.summarizer = BartSummarizer(word_count=summary_word_count)

    def chapterize(self, url) -> ChapterizedYoutubeVideo:
        print(f"Processing: {url}")
        transcribed_youtube_video = self._get_transcribed_youtube_video(url)
        chapters = []
        for segment in self.segmentizer.generate_segments(transcribed_youtube_video):
            try:
                summary = self.summarizer.summarize(segment.get_text())
                if summary == "":
                    summary = segment.get_text()
            except ValueError:
                summary = segment.get_text()
            chapter = Chapter(segment=segment, summary=summary)
            chapters.append(chapter)
        chapterized_youtube_video = ChapterizedYoutubeVideo(
            transcribed_youtube_video, chapters
        )
        print("Successfully chapterized!\n")
        return chapterized_youtube_video

    def _get_transcribed_youtube_video(self, url):
        youtube_video: YoutubeVideo = YoutubeVideo(url)
        transcript = self.transcriber.get_transcript(youtube_video.id)
        return TranscribedYoutubeVideo(youtube_video.id, transcript)
