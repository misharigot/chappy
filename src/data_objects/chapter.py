from data_objects.segment import Segment


class Chapter:
    """A segment with its summary"""

    def __init__(self, segment: Segment, summary: str):
        self.segment = segment
        self.summary = summary

    def __str__(self):
        return self.segment.get_starts_at_in_minutes() + " " + self.summary
