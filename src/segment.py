from typing import Dict, List
import re

punctuator_model = Punctuator('./punctuator/INTERSPEECH-T-BRNN.pcl') #use pretrained model

class Segment:
    def __init__(self, body: List[Dict]):
        """[summary]

        Args:
            body (List[Dict]): Example: [
                    {'text': 'build up and accumulate', 'start': 924.914, 'duration': 1.56},
                    {'text': 'something or other,', 'start': 926.474, 'duration': 3.342}
                ]
        """
        self.body: List[Dict] = body
        self.starts_at: float = body[0]["start"]
        self.ends_at: float = body[-1]["start"] + body[-1]["duration"]

    def get_starts_at_in_minutes(self):
        return format(round(self.starts_at / 60, 2), ".2f")

    def get_text(self):
        result = ""
        for item in self.body:
            result += item["text"] + " "
        return str.strip(result.replace("\n", " "))

    def punctuate_text(self, text):
        global punctuator_model
        text = re.sub("\[[^\]]*\]","",text) #remove comments between [] i.e. [applause]
        return punctuator_model.punctuate(text)
