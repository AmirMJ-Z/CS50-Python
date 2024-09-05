from working import convert
import pytest

def test_1():
    with pytest.raises(ValueError):
        convert('amir to omid')

    with pytest.raises(ValueError):
        convert ('9 00 to 9 00')

    with pytest.raises(ValueError):
        convert('amir to omid')

    with pytest.raises(ValueError):
        convert('9: to 9:')

def test_2():
    with pytest.raises(ValueError):
        convert('9:00 to 9:00 PM')

    with pytest.raises(ValueError):
        convert('9:00 AM 9:00 PM')

def test_3():
    with pytest.raises(ValueError):
        convert('25:00 AM to 12:00 PM')

    with pytest.raises(ValueError):
        convert('02:61 AM to 12:00 PM')

    assert convert('2:10 AM to 3:10 PM') == '02:10 to 15:10'
