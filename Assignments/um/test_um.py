from um import count

def test_1():
    assert count('um') == 1
    assert count('um um') == 2
    assert count('askhhdfg') == 0


def test_1():
    assert count('abumab um abum') == 1



def test_1():
    assert count('umumum') == 0
    assert count('Um um UM uM') == 4
    assert count('um, hello') == 1
