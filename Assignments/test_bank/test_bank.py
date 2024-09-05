from bank import value

def test_bank():
    assert value('Im amir') == 100
    assert value('Hey amir') == 20
    assert value('hey amirr') == 20
    assert value('hello amir') == 0
    assert value('Hello amir') == 0
