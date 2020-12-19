from typing import Dict, List, Generator
from nltk.tokenize import sent_tokenize
import nltk

from data_objects.segment import Segment
from data_objects.transcribed_youtube_video import TranscribedYoutubeVideo
from wordnet_sentence_similarity import WordnetSentenceSimilarity


class AdvancedSegmentizer:
    """Able to segmentize a YoutubeVideo based on the similarity between two following sentences.
    A segment is a subset of a transcript."""

    def __init__(self):
        self.wss = WordnetSentenceSimilarity()

    def generate_segments(self, youtube_video: TranscribedYoutubeVideo) -> Generator[Segment, None, None]:
        end_sentences = self._get_end_sentence_segment(youtube_video)
        start_index = 0
        sentence_index = 0
        for idx, transcript in enumerate(youtube_video.transcript):
            transcript_text = transcript['text'].replace('\n', ' ')
            end_sentence = end_sentences[sentence_index].split()
            if transcript_text.find(" ".join(end_sentence[-3:])) != -1:
                body = youtube_video.transcript[start_index:idx+1]
                sentence_index += 1
                start_index = idx+1
                yield Segment(body)

    def _get_end_sentence_segment(self, youtube_video: TranscribedYoutubeVideo) -> List[str]:
        tokenized_text = sent_tokenize(self._get_text_string(youtube_video.transcript))
        end_sentences = []
        sentence_count = 0
        last_score = 0
        for i in range(len(tokenized_text)):
            if len(tokenized_text[i].split()) < 4 or len(tokenized_text[i+1].split()) < 4:
                continue
            current_score = self.wss.sentence_similarity(*tokenized_text[i: i+2])
            sentence_count += 1
            if current_score < 0.2 and sentence_count > 2:
                end_sentences.append(tokenized_text[i])
                sentence_count = 0
            elif current_score < 0.2 and sentence_count <= 2:
                if last_score > current_score:
                    end_sentences[-1:] = [tokenized_text[i]]
                    sentence_count = 0
            last_score = current_score
            if i+2 == len(tokenized_text):
                break
        end_sentences.append(tokenized_text[-1])
        return end_sentences

    def _get_text_string(self, transcript):
        subs_list = []
        for subs in transcript:
            subtitle_text = subs["text"]
            subs_list.append(subtitle_text.replace('\n', ' '))
        text = " ".join(subs_list)
        return text
