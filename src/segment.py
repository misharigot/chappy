from typing import Dict, List


class Segment:
    def __init__(self, body: List[Dict]):
        self.body = body
        self.starts_at: float = body[0]["start"]
        self.ends_at: float = body[-1]["start"] + body[-1]["duration"]

    def get_text(self):
        result = ""
        for item in self.body:
            result += item["text"] + " "
        return str.strip(result.replace("\n", " "))

    def punctuate(self):
        raise NotImplementedError("The punctuate functionality is done in Milestone 3.")
