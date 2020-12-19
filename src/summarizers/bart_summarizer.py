from transformers import BartTokenizer, BartForConditionalGeneration


class BartSummarizer:
    """Able to summarize a piece of text."""

    def __init__(self, word_count=20):
        self.word_count = word_count  # length in amount of words! thus not characters

        print("Loading BartSummarizer models..")
        self.model = BartForConditionalGeneration.from_pretrained(
            "facebook/bart-large-cnn"
        )
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        print("Completed loading BartSummarizer models.\n")

    def summarize(self, text):
        inputs = self.tokenizer([text], max_length=1024, return_tensors="pt")
        summary_ids = self.model.generate(
            inputs["input_ids"],
            num_beams=3,
            min_length=5,
            length_penalty=2.0,
            max_length=self.word_count,
            early_stopping=True,
        )
        return " ".join(
            [
                self.tokenizer.decode(
                    g, skip_special_tokens=True, clean_up_tokenization_spaces=False
                )
                for g in summary_ids
            ]
        )
