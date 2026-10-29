from wordcount import count_words


def test_basic():
    assert count_words('a b  c') == 3
