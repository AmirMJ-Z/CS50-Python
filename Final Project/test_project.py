from project import *

def test_signup():
    menu = SignupMenu()
    assert menu.check_email('jake') == False
    assert menu.check_password('abcdEfg') == False
    assert menu.check_email('jake@gmail.com') == True
    assert menu.check_password('abcdEfg23') == True


def test_databse():
    assert app.current_player == None
    assert app.database.get_player_by_username('jake') != None
    assert app.database.get_player_by_username('lisa') == None

def test_game():
    game = Game()
    assert game.has_empty() == True
    assert game.check_win() == 0