from segment import Segment


class Chapter:
    """A segment with its summary
    """
    def __init__(self, segment: Segment, summary: str):
        self.segment = segment
        self.summary = summary
