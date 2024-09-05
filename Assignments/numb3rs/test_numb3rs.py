from numb3rs import validate

def test_numb3rs_nondigit():
    assert validate('cat') == False
    assert validate('a.b.c.d') == False

def test_numb3rs_digit():
    assert validate('1234.232.232.1') == False
    assert validate('232.232.1') == False
    assert validate('1234.232.232.1') == False
    assert validate('270.232.232.1') == False
    assert validate('123.232.232.1.123') == False
    assert validate('123.260.232.1') == False
    assert validate('123.232.232.1') == True
