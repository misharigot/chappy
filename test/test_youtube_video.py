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

def test_auto_generated_transcript_should_be_punctuated(youtube_video):
  youtube_video.transcript = [{
            "text": "but when we become less stimulated when we make our mind more calm",
            "start": 932.473,
            "duration": 5.082,
        },
        {
            "text": "we get the benefits of added productivity and focus and ideas and creativity",
            "start": 937.555,
            "duration": 3.719,
        },
        {
            "text": "but we also live a better life because of it",
            "start": 941.274,
            "duration": 3.699,
        }]

  expected = [{
            "text": "But when we become less stimulated when we make our mind more calm,",
            "start": 932.473,
            "duration": 5.082,
        },
        {
            "text": "we get the benefits of added productivity and focus and ideas and creativity.",
            "start": 937.555,
            "duration": 3.719,
        },
        {
            "text": "But we also live a better life because of it.",
            "start": 941.274,
            "duration": 3.699,
        }]
  youtube_video._punctuate(youtube_video.transcript)
  assert youtube_video.transcript == expected
