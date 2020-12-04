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
    youtube_video.transcript = [
        {
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
        },
    ]

    expected = [
        {
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
        },
    ]
    youtube_video._punctuate(youtube_video.transcript)
    assert youtube_video.transcript == expected


def test_auto_generated_transcript_should_be_punctuated_2():
    youtube_video = YoutubeVideo("https://www.youtube.com/watch?v=G7RgN9ijwE4")

    expected = [
        {
            "text": "Have you ever had a dreams that that you?",
            "start": 0.319,
            "duration": 8.2,
        },
        {
            "text": "Um, you add you do what you could you? Do",
            "start": 4.859,
            "duration": 7.32,
        },
        {
            "text": "you it? You want you you could do so you",
            "start": 8.519,
            "duration": 6.961,
        },
        {
            "text": "you do you could use you want you want",
            "start": 12.179,
            "duration": 5.43,
        },
        {
            "text": "them to do you so much. You could do",
            "start": 15.48,
            "duration": 4.49,
        },
        {"text": "anything.", "start": 17.609, "duration": 2.361},
    ]
    assert youtube_video.transcript == expected
