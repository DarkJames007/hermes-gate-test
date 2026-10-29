from strutil import reverse_words


def test_rw():
    assert reverse_words('a b c') == 'c b a'
