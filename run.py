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

     "!" -missed shot

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



def validate_position_and_place_battleship(begin_column, end_column, begin_row, end_row):
    
    global game_field
    global battleship_coordinates

    all_positions_validated = True
    for i in range(begin_row, end_row):
        for j in range(begin_column, end_column):
            if game_field[i][j] != "!":
                all_positions_validated = False
                break
    if all_positions_validated:
        battleship_coordinates.append([begin_column, end_column, begin_row, end_row])
        for i in range(begin_row, end_row):
            for j in range(begin_column, end_column):
                game_field[i][j] = "O"
    return all_positions_validated

    
def attempt_to_place_battleship_on_field(row, column, orientation, size):

    global game_field_size

    begin_row, end_row, begin_column, end_column = row, row + 1, column, column + 1
    if orientation == "left":
        if column - size < 0:
            return False
        begin_column = column - size + 1

    elif orientation == "right":
        if column + size >= game_field_size:
            return False
        end_column = column + size

   