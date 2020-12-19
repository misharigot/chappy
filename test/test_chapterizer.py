import pytest
from chapterizer import Chapterizer


@pytest.fixture
def chapterizer():
    chapterizer = Chapterizer(summary_word_count=30)
    return chapterizer


def test_should_have_chapters_after_chapterize(chapterizer):
    url = "https://www.youtube.com/watch?v=Hu4Yvq-g7_Y"
    chapterized_youtube_video = chapterizer.chapterize(url)
    assert chapterized_youtube_video.chapters is not None
