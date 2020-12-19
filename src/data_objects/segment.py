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

    def get_starts_at_in_minutes(self) -> str:
        """Returns the segment start time formatted in minutes, e.g. 1:05 for 65 seconds.

        Returns:
            str: The segment start time in minutes.
        """
        starts_at_seconds = round(self.starts_at)
        number_minutes = str(math.floor(starts_at_seconds / 60))
        number_seconds = str(starts_at_seconds % 60)

        def add_leading_zero_to_single_digit_seconds(seconds: str):
            return (
                number_seconds
                if not (len(number_seconds) == 1)
                else "0" + number_seconds
            )

        number_seconds = add_leading_zero_to_single_digit_seconds(number_seconds)
        return number_minutes + ":" + number_seconds

    def get_text(self):
        result = ""
        for item in self.body:
            result += item["text"] + " "
        return str.strip(result.replace("\n", " "))
