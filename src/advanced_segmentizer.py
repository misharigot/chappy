from typing import Dict, List, Generator
from nltk.tokenize import sent_tokenize

from segment import Segment
from youtube_video import YoutubeVideo
from wordnet_sentence_similarity import WordnetSentenceSimilarity


class AdvancedSegmentizer:
    """Able to segmentize a YoutubeVideo based on the similarity between two following sentences.
    A segment is a subset of a transcript."""

    def __init__(self, youtube_video: YoutubeVideo):
        self.youtube_video = youtube_video
        self.wss = WordnetSentenceSimilarity()

    def _get_end_sentence_segment(self) -> List[str]:
        tokenized_text = sent_tokenize(self.youtube_video.text)
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

    def generate_segments(self) -> Generator[Segment, None, None]:
        end_sentences = self._get_end_sentence_segment()
        # print(end_sentences, len(end_sentences))
        start_index = 0
        sentence_index = 0
        for idx, transcript in enumerate(self.youtube_video.transcript):
            transcript_text = transcript['text'].replace('\n', ' ')
            end_sentence = end_sentences[sentence_index].split()
            # print(transcript, " ".join(end_sentence[-3:]))
            if transcript_text.find(" ".join(end_sentence[-3:])) != -1:
                body = self.youtube_video.transcript[start_index:idx+1]
                sentence_index += 1
                start_index = idx+1
                # for text in body:
                #     print(text['text'].replace('\n', ' '))
                # print( '\n')
                yield Segment(body)


if __name__ == '__main__':
    youtube = YoutubeVideo('https://www.youtube.com/watch?v=Hu4Yvq-g7_Y')
    print('segmentize for: https://www.youtube.com/watch?v=Hu4Yvq-g7_Y')
    seg = AdvancedSegmentizer(youtube)
    seg.generate_segments()