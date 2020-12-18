import pytest
from data_objects.transcribed_youtube_video import TranscribedYoutubeVideo
from transcriber import Transcriber


@pytest.fixture
def transcribed_youtube_video():
    video_id = "Hu4Yvq-g7_Y"
    transcript = Transcriber().get_transcript(video_id)
    return TranscribedYoutubeVideo(video_id, transcript)


def test_duration(transcribed_youtube_video):
    actual = transcribed_youtube_video.duration
    expected = 950.35
    assert actual == expected
