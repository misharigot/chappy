import pytest
from chapterizer import Chapterizer


@pytest.fixture
def chapterizer():
    url = "https://www.youtube.com/watch?v=Hu4Yvq-g7_Y"
    chapterizer = Chapterizer(url, summary_word_count=30)
    return chapterizer


def test_should_have_chapters_after_chapterize(chapterizer):
    chapterizer.chapterize()
    assert chapterizer.chapters is not None
