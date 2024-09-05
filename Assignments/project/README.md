# XO Game
## Amirreza Mirjalily

## Video demo on YouTube:

> https://www.youtube.com/watch?v=62nt0MICnRg

## Description:

I made a simple game of XO that you place with the simple decision making algorithm that I designed.

I used SQLite3 to handle users data and game data in two tables in total.

There are 5 menu's implemented into the game that I used ReGex to handle the user's input.

All the classes and functions are implemented in the `project.py` file, the `database.db` file is the local SQLite3 database and `test_project.py` is the testing file implemented for PyTest.

I used a simple decision making algorithm for the computer playing the game, at first it tries to win the game. If the sum of a row, column or a diagonal is -2, it places an extra -1 in there to win the game (In the game visuals, -1 is the X), if there is no way for the machine to win the game, it tries to prevent the other player from winning the game with the same exact procedure, and at last, if it cannot prevent the player from winning the game or the other player cannot win the game, it places the X randomly on the board.

I implemented all the menus as classes, they all have the same design pattern. A `check` function and a `start` function that starts a loop to get input from the user and check it using ReGex in `check`.

I used the `tabulate` module that I learned in the course to make my game visualization look much fancier.

I also used `sys` and `os` to exit the game or clear the screen to make the game look fancier.

