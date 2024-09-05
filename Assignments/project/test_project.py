from project import *
from tabulate import tabulate
import sqlite3
import re
import secrets
import random
import abc
import sys
import os
import time
from datetime import datetime

def test_signup():
    menu = SignupMenu()
    assert menu.check_email('jake') != None
    assert menu.check_password('abcdEfg') != -1
    assert menu.check_email('jake@gmail.com') == None
    assert menu.check_password('abcdEfg23') == -1


def test_databse():
    assert app.current_player == None
    assert app.database.get_player_by_username('jake') != None
    assert app.database.get_player_by_username('lisa') == None

def test_game():
    game = Game()
    assert game.has_empty() == True
    assert game.check_win() == 0
