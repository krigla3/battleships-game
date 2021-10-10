"""
    Battleship game
    
    - the game will be made on a 10x10 grid area.
    - the number of battleships per player will be 5.
    - each batteship can be placed verticaly or horizontaly, no diagonal placements.
    - the player will be able to select a column and row where the desired shot will impact.
    - the number of shots will be 30 or potentially more
    - the game is one once all 4 ships of the enemy player have been destroyed.
"""

"""
    Symbols that will be used as indicators in the game:

     "." -missed shot

     "O" -area of the ship

     "X" -confirmed hit

     "~" -missed hit on open water

"""

# variable for the playable area
game_field = [[]]
#variable for playable area size
game_field_size = 10
# variable for number of battleships intended for placement
amount_of_battleships = 10
# variable for ammunition remaining
bullets_left = 30
# variable for game over
game_over = False
# variable for number of battleships destroyed
num_of_destroyed_battleships = 0
# variable for battleship positions
battleship_coordinates = [[]]
#variable for vertical grid
vertical_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

