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

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

def clear_screen():
    os.system('clear')

class App():
    def __init__(self):
        self.database = Database('/mnt/c/users/amirr/Main Server/Python Projects/CS50 Final Project/database.db')
        self.current_player = None

    def __str__(self):
        return bordered('XO GAME\nCREATED BY AMIRREZA MIRJALILY\nJULY 2024\nCS50P')
    
class Email():
    def __init__(self, email):
        regex = re.search(r'^(\w+)@(\w+).com$', email)
        self.email = email

    def __str__(self):
        return self.email
    
    def is_valid(email):
        return re.search(r'^\s*(\w+)@(\w+).com\s*$', email)
    
class Password():
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return self.password

    def generate_password():
        password_length = random.randint(9, 15)
        return Password(secrets.token_urlsafe(password_length))
    
    def is_strong(password):
        if len(password) < 8:
            return False
        
        has_upper = False
        has_lower = False
        has_digit = False
        
        for i in password:
            if i.isupper() and not has_upper:
                has_upper = True

            if i.islower() and not has_lower:
                has_lower = True

            if i.isdigit() and not has_digit:
                has_digit = True

        return has_lower and has_digit and has_upper
    
    def validate(self, password):
        return self.password == password
    
class Player():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.xp = 0
        self.level = 1

    def add_xp(self, value):
        self.xp += value 

        if self.xp >= 9 ** (self.level + 1):
            self.xp -= 9 ** (self.level + 1)
            self.level += 1
            return True
        
        return False
    
    def __str__(self):
        return bordered(f'{self.username.upper()}\n===================\nEMAIL {self.email.__str__()}\nLEVEL {self.level}\nXP {self.xp}')
    

def initialize():
    global app
    global MACHINE
    app = App()
    MACHINE = Player('MACHINE', Password('MACHINE'), Email('MACHINE@MACHINE.com'))

    
class Menu():
    @abc.abstractmethod
    def start():
        pass

    def check(input):
        pass

class MainMenu():
    def __init__(self):
        self.patterns = [
            r'^\s*game\s+menu\s*$',
            r'^\s*game\s+history\s*$',
            r'^\s*profile\s+menu\s*$',
            r'^\s*exit\s*$',
            r'^\s*login\s+menu\s*$',
            r'^\s*signup\s+menu\s*$',
        ]

    def __str__(self):
        return bordered('MAIN MENU\n=========\n\n1- GAME MENU\n2- GAME HISTORY\n3- PROFILE MENU\n4- LOGIN MENU\n5- SIGNUP MENU\n6- EXIT')
    
    def check(self, input):
        if (re.search(self.patterns[0], input)):
            menu = GameMenu(Game())
            menu.start()
            return -1

        elif (re.search(self.patterns[1], input)):
            menu = GameHistory()
            menu.start()
            return -1

        elif (re.search(self.patterns[2], input)):
            if app.current_player == None:
                print(bordered('THERE IS NO PLAYER LOGGED INTO THE GAME'))
                return 
            
            menu = ProfileMenu()
            menu.start()
            return -1
        
        elif (re.search(self.patterns[3], input)):
            print(bordered('THE XO GAME EXITED SUCCESSFULLY'))
            time.sleep(2)
            clear_screen()
            sys.exit()

        elif (re.search(self.patterns[4], input)):
            menu = LoginMenu()
            menu.start()
            return -1

        elif (re.search(self.patterns[5], input)):
            menu = SignupMenu()
            menu.start()
            return -1

    
    def start(self):
        clear_screen()
        print(self)

        while True:
            s = input()

            if self.check(s) == -1:
                break

class ProfileMenu():
    def __init__(self):
        self.patterns = [
            r'^\s*show\s+profile\s*$',
            r'^\s*log\s*out\s*$',
            r'^\s*back\s*$',
        ]

    def __str__(self):
        return bordered('PROFILE MENU\n============\n\n1- SHOW PROFILE\n2- LOGOUT\n3- BACK')
    
    def check(self, input):
        if re.search(self.patterns[0], input):
            print(app.current_player)

        elif re.search(self.patterns[1], input):
            print(bordered(f'PLAYER {app.current_player.username} LOGOYT SUCCESSFULLY'))
            app.current_player = None
            menu = MainMenu()
            menu.start()
            return -1
            

        elif re.search(self.patterns[2], input):
            menu = MainMenu()
            menu.start()
            return -1
        
    def start(self):
        clear_screen()
        print(self)

        while True:
            s = input()

            if self.check(s) == -1:
                break

class LoginMenu():
    def __str__(self):
        return bordered('LOGIN MENU\n==========\n\n1-BACK')
    
    def check_out(self, input):
        if re.search(r'^\s*back\s*$', input):
            menu = MainMenu()
            menu.start()
            return -1
            
    
    def start(self):
        clear_screen()
        print(self)

        while True:
            username = input('USERNAME: ')

            if self.check_out(username) == -1:
                break

            password = input('PASSWORD: ')

            if self.check_out(password) == -1:
                break

            if self.check(username, password) == -1:
                break

    def check(self, username, password):
        if app.database.get_player_by_username(username) == None:
            print(bordered('PLAYER WITH THIS USERNAME DOES NOT EXIST'))
            return 
        
        player = app.database.get_player_by_username(username)

        if not player.password.validate(password):
            print(bordered('USERNAME AND PASSWORD DO NOT MATCH'))
            return
        
        app.current_player = player
        print(bordered(f'PLAYER {player.username} LOGGED IN SUCCESSGULLY'))
        time.sleep(2)
        menu = MainMenu()
        menu.start()
        return -1
    
class SignupMenu():
    def __init__(self) -> None:
        pass

    def __str__(self):
        return bordered('SIGNUP MENU\n===========\n\n1- BACK\n* TYPE "RANDOM" IN THE PASSWORD FIELD TO GENERATE A PASSWORD')
    
    def check_out(self, input):
        if re.search(r'^\s*back\s*$', input):
            menu = MainMenu()
            menu.start()
            return -1 
        
    def check_password(self, password):
        if not Password.is_strong(password):
            print(bordered('PASSWORD IS NOT STRONBG ENOUGH'))
            return
        
        return -1
    
    def check_email(self, email):
        if not Email.is_valid(email):
            print(bordered('EMAIL FORMAT IS NOT VALID'))
            return -1
        
    
    def check_username(self, username):
        if app.database.get_player_by_username(username) != None:
            print(bordered('A PLAYER WITH THIS USERNAME ALREADY EXISTS'))
            return -1

        
    def start(self):
        clear_screen()
        print(self)

        while True:
            username = input('USERNAME: ')

            if self.check_username(username) == -1:
                continue

            else:
                break


        if self.check_out(username) == -1:
            return

        while True:
            password = Password(input('PASSWORD: '))

            if self.check_out(password.password) == -1:
                return

            if password.password == 'random':
                password = Password.generate_password()
                print(bordered(f'YOUR RANDOMLY GENERATED PASSWORD\n================================\n\n{password.password}'))
                break
    

            if self.check_password(str(password.password)) == -1:
                break

        while True:
            email = input('EMAIL: ')

            if self.check_email(email) != -1:
                email = Email(email)
                break

        player = Player(username, password, email)
        app.database.add_player(player)
        app.current_player = player
        print(bordered(f'PLAYER {player.username} WAS SIGNED UP AND LOGGED IN SUCCESSFULLY'))


class Database():
    def __init__(self, address):
        self.address = address
        self.connection = sqlite3.connect(address)

    def add_player(self, player):
        self.connection.cursor().execute(f'''INSERT INTO users VALUES("{player.username}", "{player.password.password}", "{player.email.email}", {player.xp}, {player.level});''')
        self.connection.commit()

    def add_game(self, game):
        if game.winner == None:
            self.connection.cursor().execute(f"INSERT INTO games VALUES('{game.player.username}', 'DRAW', '{game.date_and_time.__str__()}');")
            self.connection.commit()
            return 
        
        self.connection.cursor().execute(f"INSERT INTO games VALUES('{game.player.username}', '{game.winner.username}', '{game.date_and_time.__str__()}');")
        self.connection.commit()


    def get_player_by_username(self, username):
        if username == 'MACHINE':
            return MACHINE
        
        result = self.connection.execute(f"SELECT * FROM users WHERE username='{username}';")
        
        result = result.fetchone()

        if result == None:
            return None
        
        player = Player(result[0], Password(result[1]), Email(result[2]))
        player.xp = int(result[3])
        player.level = int(result[4])
        return player
    
    def update_current_user(self):
        self.connection.cursor().execute(f"UPDATE users SET level={int(app.current_player.level)}, xp={int(app.current_player.xp)} WHERE username='{app.current_player.username}';")
        self.connection.commit()

    def get_all_games(self):
        result = self.connection.execute(f'SELECT * FROM games;')
        result = result.fetchall()
        games = []

        for game in result:
            if game[1] == 'DRAW':
                games.append(GameIdentifier(self.get_player_by_username(game[0]), None, game[2]))

            else:
                games.append(GameIdentifier(self.get_player_by_username(game[0]), self.get_player_by_username(game[1]), game[2]))

        return games

    
class GameIdentifier():
    def __init__(self, player, winner, date_and_time):
        self.player = player
        self.winner = winner
        self.date_and_time = date_and_time

    def __str__(self):
        if self.winner == None:
            return bordered(f'PLAYER: {self.player.username}\nWINNER: DRAW\nDATE AND TIME: {self.date_and_time.__str__()}')

        return bordered(f'PLAYER: {self.player.username}\nWINNER: {self.winner.username}\nDATE AND TIME: {self.date_and_time.__str__()}')


class Game():
        
    def __init__(self):
        self.player = app.current_player
        self.winner = None
        self.date_and_time = datetime.now()
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        
    def row_sum(self, row):
        sum = 0
        for i  in range(3):
            sum += self.board[row][i]

        return sum
    
    def col_sum(self, col):
        sum  = 0
        for i in range(3):
            sum += self.board[i][col]

        return sum
    
    def diagonal_sum(self, d):
        sum = 0
        if d == 1:
            sum += self.board[0][2] + self.board[1][1] + self.board[2][0]
        else:
            sum += self.board[0][0] + self.board[1][1] + self.board[2][2]

        return sum
    
    def has_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return True
        
        return False
    
    def machine_place(self):
        if self.diagonal_sum(1) == -2 or self.diagonal_sum(1) == 2:
            if self.board[0][2] == 0:
                self.board[0][2] = -1
                return
            
            elif self.board[1][1] == 0:
                self.board[1][1] = -1
                return
            
            else:
                self.board[2][0] = -1
                return
            
        elif self.diagonal_sum(-1) == -2 or self.diagonal_sum(-1) == 2:
            if self.board[0][0] == 0:
                self.board[0][0] = -1
                return
            
            elif self.board[1][1] == 0:
                self.board[1][1] = -1
                return
            
            else:
                self.board[2][2] = -1
                return
        
        for i in range(3):
            if self.row_sum(i) == -2 or self.row_sum(i) == 2:
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = -1
                        return

            elif self.col_sum(i) == -2 or self.col_sum(i) == 2:
                for j in range(3):
                    if self.board[j][i] == 0:
                        self.board[j][i] = -1
                        return
                    
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if self.board[row][col] != 0:
                continue

            self.board[row][col] = -1
            break

    def print_board(self):
        new_board = [[0, 0, 0],
                    [0, 0, 0], 
                    [0, 0, 0]]
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    new_board[i][j] = '\t'

                elif self.board[i][j] == 1:
                    new_board[i][j] = 'O'

                else:
                    new_board[i][j] = 'X'

        clear_screen()
        print(bordered(f'MACHINE -> X\n{app.current_player.username} -> O'))
        print(tabulate(new_board, tablefmt="psql"))

    def place(self, row, col):
        if self.board[row][col] != 0:
            print(bordered('CANNOT BE PLACED IN THIS POSITION'))
            return 2
        
        self.board[row][col] = 1
        win_status = self.check_win()

        if win_status == 0:
            self.machine_place()
            self.print_board()

            if self.check_win() == -1:
                return -1
            
            elif self.check_win() == 0 :
                return 0
            
            else:
                return -2

        elif win_status == 1 :
            return 1
        
        else :
            return -2


    def check_win(self):
        if not self.has_empty():
            self.winner = None
            return -2
        
        for i in range(3):
            if self.row_sum(i) == 3:
                self.winner = self.player
                return 1
            elif self.row_sum(i) == -3:
                self.winner = MACHINE
                return -1
            elif self.col_sum(i) == 3:
                self.winner = self.player
                return 1
            elif self.col_sum(i) == -3:
                self.winner = MACHINE
                return -1
            elif self.diagonal_sum(1) == 3:
                self.winner = self.player
                return 1
            elif self.diagonal_sum(1) == -3:
                self.winner = MACHINE
                return -1
            elif self.diagonal_sum(-1) == 3:
                self.winner = self.player
                return 1
            elif self.diagonal_sum(-1) == -3:
                self.winner = MACHINE
                return -1
            
        return 0
    
    def __str__(self):
        if self.winner == None:
            return bordered(f'PLAYER: {self.player.username}\nWINNER: {self.winner.username}\nDATE AND TIME: {self.date_and_time.__str__()}')

        return bordered(f'PLAYER: {self.player.username}\nWINNER: {self.winner.username}\nDATE AND TIME: {self.date_and_time.__str__()}')
    


class GameMenu():
    def __init__(self, game):
        self.game = game
 
    def start(self):
        self.game.print_board()

        while True:
            s = input('PLACE: ')

            if not re.search(r'^\s*\d{1}\s+\d{1}\s*$', s):
                print(bordered('INVALID PLACEMENT FORMAT\n========================\n\nRIGHT FORMAT: <ROW INDEX> <COLUMN INDEX>'))
                continue

            row, col = s.split(' ')
            row = int(row) - 1
            col = int(col) - 1

            win_status = self.game.place(row, col)

            if win_status == 0:
                continue

            elif win_status == -2:
                print(bordered('DRAW'))
                app.database.add_game(self.game)
                time.sleep(5)
                menu = MainMenu()
                menu.start()
                break

            elif win_status == 1:
                if app.current_player.add_xp(100):
                    print(bordered(f'YOU WIN\nYOU HAVE BEEN LEVELED UP\n=======\n\nXP: 100\nLEVEL: {app.current_player.level}'))

                else:
                    print(bordered(f'YOU WIN\n=======\n\nXP: 100'))
                
                app.database.add_game(self.game)
                app.database.update_current_user()
                time.sleep(5)
                menu = MainMenu()
                menu.start()
                break

            elif win_status == -1:
                print(bordered('MACHINE WINS'))
                app.database.add_game(self.game)
                time.sleep(5)
                menu = MainMenu()
                menu.start()
                break

class GameHistory(Menu):

    def start(self):
        output = "GAME HISTORY\n==========\n\n"

        for game in app.database.get_all_games():
            output += game.__str__() + '\n'

        clear_screen()
        print(bordered(output))

        while True:
            s = input()
            if self.check(s) == -1:
                menu = MainMenu()
                menu.start()
                break

    def check(self, input):
        if re.search(r'^\s*back\s*$', input):
            return -1
        
        return 0

def main():
    initialize()
    menu = MainMenu()
    menu.start()

if __name__ == '__main__':
    main()






    



