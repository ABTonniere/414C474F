def get_neighbors(board, i, j):
    neighbors = []
    rows = len(board)
    cols = len(board[0])
    for x in range(max(0, i-1), min(i+2, rows)):
        for y in range(max(0, j-1), min(j+2, cols)):
            if (x, y) != (i, j):
                neighbors.append(board[x][y])
    return neighbors

def next_generation(board):
    new_board = []
    for i in range(len(board)):
        new_row = []
        for j in range(len(board[0])):
            neighbors = get_neighbors(board, i, j)
            live_neighbors = sum(neighbors)
            if board[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
            else:
                if live_neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_board.append(new_row)
    return new_board

def game_of_life(board, iterations):
    for _ in range(iterations):
        board = next_generation(board)
    return board

N, M = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
iterations = int(input())

final_board = game_of_life(board, iterations)

live_cells = sum([sum(row) for row in final_board])
print(live_cells)

