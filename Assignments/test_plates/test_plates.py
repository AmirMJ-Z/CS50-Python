from plates import is_valid

def test_plates():
    assert is_valid('a') == False
    assert is_valid('akdhn543') == False
    assert is_valid('123as') == False
    assert is_valid('a1234') == False
    assert is_valid('abc07') == False
    assert is_valid('abc 7') == False
    assert is_valid('abc .6') == False
    assert is_valid('abc567')
    assert is_valid('ab5bc') == False
