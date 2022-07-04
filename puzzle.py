# Name: Devon Miller
# Course: CS  325
# Date: 5/14/2022
# Description: Takes a board game start and end as paramaters goal is to get from
#               start to end in least possible moves avoiding spaces marked by "#"
#               returns array of move cordinates traversed to reache end and the direction of
#               moves as a string

import heapq
import copy


def solve_puzzle(board, start, end):
    """adds values and send to helper function, initialize results and visited
    with starting space"""

    result = [[(float('inf'), 0, "") for x in range(len(board[0]))] for x in range(len(board))]
    result[start[0]][start[1]] = (0, [(start[0], start[1])], "")
    visited = [(start[0], start[1])]
    return solve_puzzle_helper(board, start, end, result, visited, [])


def solve_puzzle_helper(board, start, end, result, visited, queue):
    """returns path from start to end in least possible spaces and the
    directions of each move"""

    path = [(start[0], start[1])]
    result[start[0]][start[1]] = (0, path, "")
    heapq.heappush(queue, (0, path))
    while len(queue) > 0:                   # if queue empty then no solution found
        current = heapq.heappop(queue)
        cordinates = current[1][-1]
        y = cordinates[0]
        x = cordinates[1]
        path = current[1]
        if (y, x) == (end[0], end[1]):           # destination space reached
            string = result[y][x][2]
            return (path, string)
        moves = [[y - 1, x, y > 0, "U"], [y + 1, x, y < len(board)-1, "D"],
                 [y, x + 1, x < len(board[0])-1, "R"], [y, x - 1, x > 0, "L"]]

        for move in moves:                      # make all moves up down left right
            if move[2] and (move[0], move[1]) not in visited:
                if board[move[0]][move[1]] == "-":
                    if result[y][x][0] + 1 < result[move[0]][move[1]][0]:
                        path1 = copy.deepcopy(path)
                        path1.append((move[0], move[1]))
                        value = result[y][x][0] + 1
                        string = result[y][x][2] + move[3]
                        heapq.heappush(queue, (value, path1))
                        result[move[0]][move[1]] = (value, path1, string)
        visited.append((y, x))        # space processed and finished
    return None
