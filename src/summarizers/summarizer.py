from gensim.summarization.summarizer import summarize as gensim_summarize


class Summarizer:
    """Able to summarize a piece of text."""

    def __init__(self, word_count=30):
        self.word_count = word_count

    def summarize(self, text: str):
        return gensim_summarize(text, word_count=self.word_count)
