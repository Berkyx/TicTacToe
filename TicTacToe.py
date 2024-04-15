def generate_grid(dimensions):
    return [[' ' for _ in range(dimensions)] for _ in range(dimensions)]

def display_grid(grid):
    dimensions = len(grid)
    horizontal_sep = '-' * (dimensions * 4 + 1)
    vertical_lines = '|'.join(['   '] * dimensions)
    column_titles = '   ' + '   '.join(chr(ord('A') + i) for i in range(dimensions))
    print(column_titles)
    print('  ' + horizontal_sep)

    for idx, row in enumerate(grid):
        formatted_row = ' | '.join(f"{cell}" for cell in row)
        print(f"{str(idx + 1).ljust(2)}| {formatted_row} |")
        if idx < dimensions - 1:
            print('  ' + horizontal_sep)

def setup_grid(dimensions):
    return [[' ' for _ in range(dimensions)] for _ in range(dimensions)]

def display_scores(p1, p2, score_p1, score_p2, current_player):
    print(f"Player1 ({p1}) - Score: {score_p1}")
    print(f"Player2 ({p2}) - Score: {score_p2}")
    print(f"{current_player} playing...")
    print()

def validate_line(segment, symbol):
    return all(x == symbol for x in segment)

def assess_victory(grid, symbol, win_cond=3):
    dimensions = len(grid)
    for row in range(dimensions):
        for col in range(dimensions):
            if col + win_cond <= dimensions:  # Horizontal check
                if validate_line([grid[row][i] for i in range(col, col + win_cond)], symbol):
                    return True
            if row + win_cond <= dimensions:  # Vertical check
                if validate_line([grid[i][col] for i in range(row, row + win_cond)], symbol):
                    return True
            if row + win_cond <= dimensions and col + win_cond <= dimensions:  # Diagonal check down-right
                if validate_line([grid[i][i + col - row] for i in range(row, row + win_cond)], symbol):
                    return True
            if row + win_cond <= dimensions and col - win_cond >= -1:  # Diagonal check up-right
                if validate_line([grid[i][col - (i - row)] for i in range(row, row + win_cond)], symbol):
                    return True
    return False

def player_input(grid, symbol, name):
    dimensions = len(grid)
    while True:
        user_move = input(f"Player {name}, enter your move (e.g., a1): ").lower()
        if len(user_move) >= 2 and user_move[0].isalpha() and user_move[1:].isdigit():
            column = ord(user_move[0]) - ord('a')
            row = int(user_move[1:]) - 1
            if 0 <= row < dimensions and 0 <= column < dimensions and grid[row][column] == ' ':
                grid[row][column] = symbol
                return
        print("Invalid move, try again.")

def game_play():
    game_type = input("Enter 2 for a two-player game, 3 for a three-player game or 4 for a four-player game: ")
    if game_type == '2':
        participants = ['X', 'O']
    elif game_type == '3':
        participants = ['X', 'O', '#']
    elif game_type == '4':
        participants = ['X', 'O', '#', '@']
    else:
        print("Invalid selection.")
        return
    victory_condition = 5
    dimensions = int(input("Enter the dimensions of the grid (e.g., 5 for a 5x5 grid): "))
    while dimensions < 5 or dimensions > 25:
        dimensions = int(input("Enter a valid dimension (from 5 to 25): "))

    participants_names = input("Enter the names of the participants separated by commas: ")
    participants_names = participants_names.split(',')
    while len(participants_names) != len(participants):
        participants_names = input("Enter the correct number of names: ")
        participants = participants_names.split(',')

    grid = [[' ' for _ in range(dimensions)] for _ in range(dimensions)]
    player_turn = 0
    while True:
        display_grid(grid)
        player_input(grid, participants[player_turn], participants_names[player_turn])
        if assess_victory(grid, participants[player_turn], victory_condition):
            display_grid(grid)
            print(f"Player {participants_names[player_turn]} wins!")
            break
        if all(grid[i][j] != ' ' for i in range(dimensions) for j in range(dimensions)):
            print("It's a draw!")
            break
        player_turn = (player_turn + 1) % len(participants)

if __name__ == "__main__":
    game_play()
