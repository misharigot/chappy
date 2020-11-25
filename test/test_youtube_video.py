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
