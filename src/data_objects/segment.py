from typing import Dict, List
import math


class Segment:
    def __init__(self, body: List[Dict]):
        """[summary]

        Args:
            body (List[Dict]): Example: [
                    {'text': 'build up and accumulate', 'start': 924.914, 'duration': 1.56},
                    {'text': 'something or other,', 'start': 926.474, 'duration': 3.342}
                ]
        """
        self._validate_body(body)
        self.body: List[Dict] = body
        self.starts_at: float = body[0]["start"]
        self.ends_at: float = body[-1]["start"] + body[-1]["duration"]

    def _validate_body(self, body: List[Dict]):
        if not len(body) > 0:
            raise ValueError("Body does not contain any elements.")

    def get_starts_at_in_minutes(self):
        starts_at_seconds = round(self.starts_at)
        number_minutes = math.floor(starts_at_seconds / 60)
        number_seconds = starts_at_seconds % 60
        return str(number_minutes) + "." + str(number_seconds)

    def get_text(self):
        result = ""
        for item in self.body:
            result += item["text"] + " "
        return str.strip(result.replace("\n", " "))
