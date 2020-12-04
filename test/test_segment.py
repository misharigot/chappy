import pytest
from segment import Segment


@pytest.fixture
def segment():
    body = [
        {"text": "build up and accumulate", "start": 924.914, "duration": 1.56},
        {
            "text": "to create a life that feels\nmore distracted and overwhelming,",
            "start": 926.474,
            "duration": 3.342,
        },
        {
            "text": "like we don't have a clear direction.",
            "start": 929.816,
            "duration": 2.657,
        },
        {
            "text": "But when we become less stimulated,\nwhen we make our mind more calm,",
            "start": 932.473,
            "duration": 5.082,
        },
        {
            "text": "we get the benefits of added productivity\nand focus and ideas and creativity,",
            "start": 937.555,
            "duration": 3.719,
        },
        {
            "text": "but we also live\na better life because of it.",
            "start": 941.274,
            "duration": 3.699,
        },
        {"text": "Thank you so much.", "start": 946.195, "duration": 1.461},
        {"text": "(Applause)", "start": 947.656, "duration": 2.699},
    ]
    s = Segment(body)
    return s


def test_get_text(segment):
    expected = "build up and accumulate to create a life that feels more distracted and overwhelming, like we don't have a clear direction. But when we become less stimulated, when we make our mind more calm, we get the benefits of added productivity and focus and ideas and creativity, but we also live a better life because of it. Thank you so much. (Applause)"
    actual = segment.get_text()
    print(actual)
    assert actual == expected
