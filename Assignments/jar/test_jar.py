from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"



def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.deposit(100)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)

    with pytest.raises(ValueError):
        jar.deposit(100)
