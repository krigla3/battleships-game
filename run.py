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
# variable for playable area size
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
# variable for vertical grid
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


    elif orientation == "up":
        if row - size < 0:
            return False
        begin_row = row - size + 1

    elif orientation == "down":
        if row + size >= game_field_size:
            return False
        end_row = row + size

    return validate_position_and_place_battleship(begin_row, end_row, begin_column, end_column)


def construct_game_field():
    global game_field
    global game_field_size
    global amount_of_battleships
    global battleship_coordinates

    random.seed(time.time())

    rows, columns = (game_field_size, game_field_size)

    
    game_field = []
    for r in range(rows):
        row = []
        for j in range(columns):
            row.append("!")
        game_field.append(row)

    amount_of_placed_battleships = 0

    ship_positions = []

    while amount_of_placed_battleships != amount_of_battleships:
        random_row = random.randint(0, rows - 1)
        random_column = random.randint(0, cols - 1)
        orientation = random.choice(["right", "left", "up", "down"])
        battleship_size = random.randint(3, 5)
        if attempt_to_place_battleship_on_field(random_row, random_column, orientation, battleship_size):
            amount_of_placed_battleships += 1

def print_game_field():

    global game_field
    global vertical_letters

    debug_mode = True

    vertical_letters = vertical_letters[0: len(game_field) + 1]

    for row in range(len(game_field)):
        print(vertical_letters[row], end=") ")
        for column in range(len(game_field[row])):
            if game_field[row][column] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print("!", end=" ")
            else:
                print(game_field[row][column], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(game_field[0])):
        print(str(i), end=" ")
    print("")


def confirm_valid_shot_placement():
 
    global vertical_letters
    global game_field

    valid_placement = False
    row = -1
    column = -1
    while valid_placement is False:
        position = input("Please enter row (A-J) and column (0-9), valid example: B7: ")
        position = position.upper()
        if len(position) <= 0 or len(position) > 2:
            print("Error: Please check to input only one row and column such as B7")
            continue
        row = position[0]
        column = position[1]
        if not row.isalpha() or not column.isnumeric():
            print("Error: Please input a leter from (A-J) for row, and number from (0-9) for column")
            continue
        row = vertical_letters.find(row)
        if not (-1 < row < game_field):
            print("Error: Please input a leter from (A-J) for row, and number from (0-9) for column")
            continue
        col = int(column)
        if not (-1 < column < game_field):
            print("Error: Please input a leter from (A-J) for row, and number from (0-9) for column")
            continue
        if game_field[row][column] == "~" or game_field[row][column] == "X":
            print("This target has already been hit, please chose other coordinates")
            continue
        if game_field[row][column] == "!" or grid[row][col] == "O":
            valid_placement = True

    return row, column

def validate_battleship_destroyed(row, column):
    
    global battleship_coordinates
    global game_field

    for coordinate in battleship_coordinates:
        begin_row = coordinate[0]
        end_row = coordinate[1]
        begin_column = coordinate[2]
        end_column = coordinate[3]
        if begin_row <= row <= end_row and begin_column <= column <= end_column:
           
            for i in range(begin_row, end_row):
                for j in range(begin_column, end_column):
                    if grid[i][j] != "X":
                        return False
    return True