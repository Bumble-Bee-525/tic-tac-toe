import sys

print("WELCOME TO TIC TAC TOE 2.0!")
print("the board works like this:")
print("0-------->∞")
print("|\n|\n|\n\/\n∞")

# dimensions of whole game
dimensions = int(input("dimensions: "))
if dimensions < 2:
    print("no thats not possible")
    sys.exit(0)

board = list()
# player 1's data
nameA = input("player 1: enter your name: ")
row_sumA = list()
column_sumA = list()
diagonal_sumA = 0
antidiagonal_sumA = 0
# player 2's data
nameB = input("player 2: enter your name: ")
row_sumB = list()
column_sumB = list()
diagonal_sumB = 0
antidiagonal_sumB = 0

# print board and initialize variables and arrays
#print(" --- " * dimensions)
for y in range(dimensions):
    #print("|   |" * dimensions)
    #print(" --- " * dimensions)
    row_sumA.append(0)
    column_sumA.append(0)
    board.append(list())
    
    row_sumB.append(0)
    column_sumB.append(0)

    for x in range(dimensions):
        board[y].append(0)

# until player wins
while True:
    # get player 1's input
    ax, ay = 0, 0
    while ax < 1 or ax > dimensions or ay < 1 or ay > dimensions:
        ax, ay = map(int, input("enter " + nameA + " coords: ").split())
    
    # update player's rows and columns
    row_sumA[ay - 1] += 1
    column_sumA[ax - 1] += 1
    # update player1's diaganols
    if ax == ay:
        diagonal_sumA += 1
    if dimensions - ax - 1 ==  ay:
        antidiagonal_sumA += 1
    # update board's display
    board[ay-1][ax-1] = 1
    # check for winner
    if row_sumA[ay - 1] == dimensions or column_sumA[ax - 1] == dimensions or diagonal_sumA == dimensions or antidiagonal_sumA == dimensions:
        print(f"{nameA} has won!")
        break
    # print board
    for row in board:
        print(row)

    
    # get player 2's input
    bx, by = 0, 0
    while bx < 1 or bx > dimensions or by < 1 or by > dimensions:
        bx, by = map(int, input("enter " + nameB + " coords: ").split())
    # update player's rows and columns
    row_sumB[by - 1] += 1
    column_sumB[bx - 1] += 1
    # update player2's diaganols
    if bx == by:
        diagonal_sumB += 1
    if dimensions - bx + 1 ==  by:
        antidiagonal_sumB += 1
    # update board's display
    board[by-1][bx-1] = 2
    # check for winner
    if row_sumB[by - 1] == dimensions or column_sumB[bx - 1] == dimensions or diagonal_sumB == dimensions or antidiagonal_sumB == dimensions:
        print(f"{nameB} has won!")
    
    # print board
    for row in board:
        print(row)