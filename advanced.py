def relationship_status(subject_user, object_user, relationships):
    if object_user in relationships[subject_user]["following"]:
        if subject_user in relationships[object_user]["following"]:
            return "friends"
        else:
            return "follower"
    elif subject_user in relationships[object_user]["following"]:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(game_board):
    n = len(game_board)
    for row in game_board:
        if all(cell == row[0] and cell != '' for cell in row):
            return row[0]
    for col_index in range(n):
        if all(game_board[row_index][col_index] == game_board[0][col_index] and game_board[row_index][col_index] != '' for row_index in range(n)):
            return game_board[0][col_index]
    if all(game_board[index][index] == game_board[0][0] and game_board[index][index] != '' for index in range(n)):
        return game_board[0][0]
    if all(game_board[index][n - 1 - index] == game_board[0][n - 1] and game_board[index][n - 1 - index] != '' for index in range(n)):
        return game_board[0][n - 1]
    return "NO WINNER"


def eta(start_stop, end_stop, stop_times):
    current_location = start_stop
    total_time = 0
    while current_location != end_stop:
        for (origin, destination), travel_info in stop_times.items():
            if origin == current_location:
                total_time += travel_info['travel_time_mins']
                current_location = destination
                break
    return total_time


