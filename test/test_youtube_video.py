import pytest
from data_objects.youtube_video import YoutubeVideo


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
