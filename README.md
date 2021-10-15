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


## Testing

### Validator testing

I have tested the code by passing it through PEP8 online Python validator to ensure there are no problems.

![python_validator](https://github.com/krigla3/battleships-game/blob/main/docs/python_validator.jpg)


### Other testing

    1. Testing validate_position_and_place_battleship()

       The function is intended to place battleships of sizes 3-5 spaces randomly on the game field in four directions without having any battleships overlap. To ensure this is properly tested, I introduced a test mode variable which shows the placement of the battleships. Through multiple game restarts I was able to confirm that no battleships overlap and the feature runs as expected.

    2. Testing attempt_to_place_battleship_on_field()

       If the function validate_position_and_place_battleship() returns ‘True’ this means that no battleship has overlapped and the battleship is placed on the field through the attempt_to_place_battleship_on_field() function.

    3. Testing construct_game_field()

       The purpose of the function is to create 10 rows and 10 columns resulting in a 10 x 10 grid where battleships are randomly placed. By initially running the game, we can see that the 10 by 10 grid is correctly displayed. 

    4. Testing print_game_field()

       The purpose of the function is to print the grid containing rows A – J and columns 0 – 9 and the relevant shot indicator symbols ‘X’, ‘!’ and ‘~’ to the Python terminal. Upon running the game in the terminal, the grid is displayed correctly. This has been tested through the test mode below that reveals the battleship placement.

       To display the placed ships, the print statement in test_mode should contain “0”:

       if game_field[row][column] == “0”:
            if test_mode:
                print(“0”, end=(“ ”)

        To hide the placed ships, the print statement in test_mode should be changed to “~”:

        if game_field[row][column] == “0”:
            if test_mode:
                print(“~”, end=(“ ”)

        All symbols are displaying the correct output.

    5. Testing confirm_valid_shot_placement()

        The function tests if the user has entered a valid input from the rows A – J and columns 0 – 9 in the form that it has been requested in. If the user enters an invalid input, they will receive one of the following error messages in the terminal:

        If the user inputs more than one letter and more than one number, the following error message appears:

![error_one](https://github.com/krigla3/battleships-game/blob/main/docs/error_one.gif) 

        If the user enters the input in wrong order such as 7D instead of D7, the following error message appears:



        If the user enters an input greater than A – J or greater than 0 – 9, the following error message appears:

![error_two](https://github.com/krigla3/battleships-game/blob/main/docs/error_two.gif)

        If the user tries to place a shot on the grid spaces that have previously been marked by ‘X’ for hit or ‘!’ for miss, the following error message appears:

<screenshot>


    






















