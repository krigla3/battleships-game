# Battleship game

A single player Command Line Interface Python game of Battleship.

![game_preview](https://github.com/krigla3/battleships-game/blob/main/docs/game_preview.jpg)


## How to Play

In this version the user tries to find and sink five battleships of varying sizes before their ammunition runs out! The board has a vertical axis of A to J and a horizontal axis of 0 to 9 with wave icons concealing the battleship locations. The user pinpoints where they wish to strike by choosing one point from each axis, for example ‘B7’. If the user has hit an area on a battleship, the wave icon is replaced by the ‘X’ symbol. If they have missed, the wave symbol is replaced by the ‘!’ symbol. The user has 60 rounds of ammunition which equals 60 tries. 

When a user misses, a message in the terminal reads “Shot missed, no battleship was hit.”

When a user strikes a part of a battleship, a message in terminal reads “Battleship was hit!”

When all points of a battleship are hit, a message in the terminal reads “Hit!!! Battleship destroyed!!!”


## Features

    1. The game features an introduction to the user before they start the game.

![game_introduction](https://github.com/krigla3/battleships-game/blob/main/docs/game_introduction.jpg)

    2. The user is presented with a 10 x 10 grid game board featuring a vertical (A – J) and a horizontal axis (0 – 9).

![game_grid](https://github.com/krigla3/battleships-game/blob/main/docs/game_grid.jpg)

    3. The user is shown the number of battleships he needs to find (5) and the number of tries available (60). 
       The battleships range between 3 – 5 spaces on the grid, and are concealed behind the wave symbols until hit.

![ammo-battleships](https://github.com/krigla3/battleships-game/blob/main/docs/ammo-battleships.jpg)

    4. Lastly, the user is shown instructions on how to play the game. 
       User isinstructed to choose a point on the vertical axis and the horizontal axis, for
       example ‘C7’ and then to press enter for the strike to release.

![play_instructions](https://github.com/krigla3/battleships-game/blob/main/docs/play_instructions.jpg)

    5. Win and loss announcements are shown throughout the game:

When a user misses, a message in the terminal reads “Shot missed, no battleship was hit.”

![user-miss](https://github.com/krigla3/battleships-game/blob/main/docs/user-miss.gif)

When a user strikes a part of a battleship, a message in terminal reads “Battleship was hit!”

![battleship_hit](https://github.com/krigla3/battleships-game/blob/main/docs/battleship_hit.gif)

When all points of a battleship are hit, a message in the terminal reads “Hit!!! Battleship destroyed!!!”

![battleship_destroyed](https://github.com/krigla3/battleships-game/blob/main/docs/battleship_destroyed.gif)


## Future Features

* Make the game multiplayer
* Ability to enter username
* Leaderboard
* Ability to place your own ships to play against the AI or between two players
* Option to increase the grid, number of ammunition and ships per game
* Display hits and misses in separate colours instead of black and white









