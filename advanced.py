def check_relationship(subject_user, object_user, relationships):
    if object_user in relationships[subject_user]["following"]:
        if subject_user in relationships[object_user]["following"]:
            return "friends"
        else:
            return "follower"
    elif subject_user in relationships[object_user]["following"]:
        return "followed by"
    else:
        return "no relationship"

def check_winner(game_board):
    board_size = len(game_board)
    for i in range(board_size):
        if all(game_board[i][0] == game_board[i][j] != '' for j in range(board_size)):
            return game_board[i][0]
        if all(game_board[0][i] == game_board[j][i] != '' for j in range(board_size)):
            return game_board[0][i]
    if all(game_board[0][0] == game_board[i][i] != '' for i in range(board_size)):
        return game_board[0][0]
    if all(game_board[0][board_size-1] == game_board[i][board_size-1-i] != '' for i in range(board_size)):
        return game_board[0][board_size-1]
    return "NO WINNER"

def calculate_eta(start_stop, end_stop, travel_routes):
    travel_time = 0
    current_location = start_stop
    while current_location != end_stop:
        for (start, destination), travel_details in travel_routes.items():
            if start == current_location:
                travel_time += travel_details['travel_time_mins']
                current_location = destination
                break
    return travel_time
