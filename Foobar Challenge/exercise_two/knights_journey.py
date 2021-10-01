def solution(src, dest):
    source = [get_x_coordinate(src), get_y_coordinate(src)]
    destination = [get_x_coordinate(dest), get_y_coordinate(dest)]
    current_pos = source
    total_distance = get_distance(source, destination)

    # start by attempting to get to the destination in a single move

    min_moves_required = 1

    # check to see if the knight is already at the destination
    # OR if the source and destination are in opposite corners

    if src == dest:
        return 0
    elif total_distance == 14:
        return 6

    # repeat loop until knight at destination

    while current_pos != destination:

        # increment min number of moves if attempt did not reach the destination
        # in given move range

        min_moves_required += 1
        restricted_moves = []

        # start next attempt to get to destination in min_moves_required
        while source not in restricted_moves and current_pos != destination:

            used_moves = []
            current_pos = source

            for x in range(min_moves_required):
                used_moves.append(current_pos)
                moves = get_possible_moves(current_pos[0], current_pos[1], restricted_moves, used_moves)

                # loop through possible moves to determine which brings us closest

                if len(moves) > 0:
                    current_pos = moves[0]
                else:
                    restricted_moves.append(current_pos)

                distance = get_distance(current_pos, destination)

                # if position is at destination

                if current_pos == destination:
                    return str(x + 1)

            # If distance was not met add the current position to restricted_moves

            if distance != 0:
                restricted_moves.append(current_pos)


def get_x_coordinate(position):
    if position <= 7:
        return position + 1
    else:
        return (position % 8) + 1


def get_y_coordinate(position):
    if position <= 7:
        return 1
    else:
        return (position // 8) + 1


def get_possible_moves(x, y, restricted_moves, used_moves):
    moves = []

    moves.append([x - 1, y + 2])
    moves.append([x - 1, y - 2])
    moves.append([x + 1, y + 2])
    moves.append([x + 1, y - 2])
    moves.append([x - 2, y + 1])
    moves.append([x - 2, y - 1])
    moves.append([x + 2, y + 1])
    moves.append([x + 2, y - 1])

    valid_moves = []

    for move in moves:

        # Check the co-ords lands within the chessboard
        in_bounds = move[0] > 0 and move[0] < 9 and move[1] > 0 and move[1] < 9

        # Checks that the move hasn't been attempted previously and is within the chessboard
        unrestricted_move = move not in restricted_moves and move not in used_moves

        if in_bounds and unrestricted_move:
            valid_moves.append(move)

    return valid_moves


# Get distance between two points
def get_distance(src, dest):
    x_dist = abs(src[1] - dest[1])
    y_dist = abs(src[0] - dest[0])

    return x_dist + y_dist