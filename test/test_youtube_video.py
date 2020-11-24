import pytest
from youtube_video import YoutubeVideo


@pytest.fixture
def youtube_video():
    result = YoutubeVideo("https://www.youtube.com/watch?v=Hu4Yvq-g7_Y")
    return result


def test_from_id():
    expected = "Hu4Yvq-g7_Y"
    youtube_video = YoutubeVideo("Hu4Yvq-g7_Y")

    actual = youtube_video.id
    assert expected == actual


def test_from_url():
    expected = "Hu4Yvq-g7_Y"
    youtube_video = YoutubeVideo("https://www.youtube.com/watch?v=Hu4Yvq-g7_Y")
    actual = youtube_video.id
    assert expected == actual


def test_transcript(youtube_video):
    actual = youtube_video.transcript
    assert len(actual) > 10
    assert list(actual[0].keys()) == ["text", "start", "duration"]


def test_duration(youtube_video):
    actual = youtube_video.duration
    expected = 950.35
    assert actual == expected


def test_split(youtube_video):
    expected = [0, 86.4, 172.8, 259.2, 345.6, 432.0, 518.4, 604.8, 691.2, 777.6, 864.0]
    n_parts = 10
    actual = youtube_video.split(n_parts=n_parts)
    assert actual == expected
    assert actual[0] == 0
    assert actual[-1] <= youtube_video.duration
    assert len(actual) == n_parts + 1


def test_segmentize(youtube_video):
    expected = [
        {"segment_number": 0, "starts_at_index": 0},
        {"segment_number": 1, "starts_at_index": 27},
        {"segment_number": 2, "starts_at_index": 54},
        {"segment_number": 3, "starts_at_index": 80},
        {"segment_number": 4, "starts_at_index": 105},
        {"segment_number": 5, "starts_at_index": 135},
        {"segment_number": 6, "starts_at_index": 161},
        {"segment_number": 7, "starts_at_index": 189},
        {"segment_number": 8, "starts_at_index": 218},
        {"segment_number": 9, "starts_at_index": 250},
        {"segment_number": 10, "starts_at_index": 281},
    ]
    actual = youtube_video.segmentize(10)
