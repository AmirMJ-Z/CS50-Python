from twttr import shorten

def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('apple') == 'ppl'
    assert shorten('CS50') == 'CS50'
    assert shorten('Apple') == 'ppl'
    assert shorten('a.a') == '.'
