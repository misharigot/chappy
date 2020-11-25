from typing import List

import pytest
from segment import Segment
from simple_segmentizer import SimpleSegmentizer
from youtube_video import YoutubeVideo


@pytest.fixture
def segmentizer():
    youtube_video = YoutubeVideo("https://www.youtube.com/watch?v=Hu4Yvq-g7_Y")
    segmentizer = SimpleSegmentizer(youtube_video, n_parts=10)
    return segmentizer


def test_split(segmentizer):
    expected = [0.0, 95.03, 190.06, 285.1, 380.13, 475.16, 570.2, 665.24, 760.27, 855.3]
    n_parts = 10
    actual = segmentizer._split()
    assert actual == expected
    assert actual[0] == 0
    assert actual[-1] <= segmentizer.youtube_video.duration
    assert len(actual) == n_parts


def test_get_segment_indices(segmentizer):
    expected = [
        {"segment_number": 0, "starts_at_index": 0, "ends_at_index": 30},
        {"segment_number": 1, "starts_at_index": 30, "ends_at_index": 60},
        {"segment_number": 2, "starts_at_index": 60, "ends_at_index": 87},
        {"segment_number": 3, "starts_at_index": 87, "ends_at_index": 116},
        {"segment_number": 4, "starts_at_index": 116, "ends_at_index": 149},
        {"segment_number": 5, "starts_at_index": 149, "ends_at_index": 179},
        {"segment_number": 6, "starts_at_index": 179, "ends_at_index": 210},
        {"segment_number": 7, "starts_at_index": 210, "ends_at_index": 243},
        {"segment_number": 8, "starts_at_index": 243, "ends_at_index": 278},
        {"segment_number": 9, "starts_at_index": 278, "ends_at_index": 306},
    ]
    actual = segmentizer._get_segment_indices()
    assert actual == expected


def test_generate_segments(segmentizer):
    actual: List[Segment] = []
    for segment in segmentizer.generate_segments():
        actual.append(segment)
    assert len(actual) == 10
