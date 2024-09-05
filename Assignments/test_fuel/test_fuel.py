from fuel import convert, gauge
import pytest

def test_fuel():
    with pytest.raises(ValueError):
        convert('a/b')

    with pytest.raises(ZeroDivisionError):
        convert('1/0')

    with pytest.raises(ValueError):
        convert('3/2')

    assert convert('1/2') == 50
    assert convert('0/5') == 0
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
