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
    expected = [0, 86.4, 172.8, 259.2, 345.6, 432.0, 518.4, 604.8, 691.2, 777.6, 864.0]
    n_parts = 10
    actual = segmentizer._split()
    assert actual == expected
    assert actual[0] == 0
    assert actual[-1] <= segmentizer.youtube_video.duration
    assert len(actual) == n_parts + 1


def test_get_segment_indices(segmentizer):
    expected = [
        {"segment_number": 0, "starts_at_index": 0, "ends_at_index": 27},
        {"segment_number": 1, "starts_at_index": 27, "ends_at_index": 54},
        {"segment_number": 2, "starts_at_index": 54, "ends_at_index": 80},
        {"segment_number": 3, "starts_at_index": 80, "ends_at_index": 105},
        {"segment_number": 4, "starts_at_index": 105, "ends_at_index": 135},
        {"segment_number": 5, "starts_at_index": 135, "ends_at_index": 161},
        {"segment_number": 6, "starts_at_index": 161, "ends_at_index": 189},
        {"segment_number": 7, "starts_at_index": 189, "ends_at_index": 218},
        {"segment_number": 8, "starts_at_index": 218, "ends_at_index": 250},
        {"segment_number": 9, "starts_at_index": 250, "ends_at_index": 281},
        {"segment_number": 10, "starts_at_index": 281, "ends_at_index": 306},
    ]
    actual = segmentizer._get_segment_indices()
    assert actual == expected


def test_generate_segments(segmentizer):
    actual: List[Segment] = []
    for segment in segmentizer.generate_segments():
        actual.append(segment)
    assert len(actual[0].body) == 27
    assert len(actual[1].body) == 27
    last_index = len(actual) - 1
    assert len(actual[last_index].body) == 25
