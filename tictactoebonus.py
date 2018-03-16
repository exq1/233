###############################################################################
#
#  A+ BONUS ATTEMPT!!!
#
###############################################################################
#
#  The location to insert your code is clearly marked with ###############################################################################
#
from SimpleGraphics import *
from random import shuffle
from math import factorial
from copy import deepcopy
import inspect
import sys
from pprint import pprint
import traceback
# Contants for the board size
WIDTH = 600
HEIGHT = 600
# Constants for the game pieces
EMPTY = 0
X = 1
O = 2
# Constants to turn off tests for parts of assignment
TESTPART1 = True
TESTPART2 = True
TESTPART3 = True
TESTPART4 = True
TESTPART5 = True
TESTPART6 = True
TESTPART7 = True
STOP1STFAIL = True

###############################################################################
#
#  Only modify the file below this point
#
###############################################################################
#
#  Insert your implementation of createBoard here (code and comments (in-line and above function))
#
#this function creates a 2d list that acts as the game board
def createBoard(row, col):
    board = []
    for r in range(row):
        board.append([])
        for c in range(col):
            board[r].append(EMPTY)
    return board
#
#  Insert your implementation of canPlay here (code and comments (in-line and above function))
#
#this function checks if a player move is valid
def canPlay(board, row, col):
    boolean = False
    if board[row][col] == EMPTY:
        boolean = True
    return boolean
#
#  Insert your implementation of play here (code and comments (in-line and above function))
#
#this function plays a piece at the given location
def play(board, row, col, piece):
    board[row][col] = piece
#
#  Returns True if there is no EMPTY location in the board
#
#  Parameters:
#    board: The board to examine
#
#  Returns: True if board has no EMPTY locations, False otherwise
#
#this function checks if the board is full
def full(board):
    boolean = True
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == EMPTY:
                boolean = False
    return boolean
#
#  Insert your implementations of winInRow, winInCol, winInDiag here (code and comments (in-line and above functions))
#
#this function checks for row win condition
def winInRow(board, row, piece):
    # if board is 4x4, check for 4 in a row
    if (len(board) == 4) and ((len(board[0]) == 4)):
        return True if str(piece)*4 in ''.join(str(e) for e in board[row]) else False
    # else check for 3 in a row
    else:
        return True if str(piece)*3 in ''.join(str(e) for e in board[row]) else False

#this function checks for column win condition
def winInCol(board, col, piece):
    #if board is 4x4, check for 4 in a row
    if (len(board) == 4) and ((len(board[0]) == 4)):
        return True if str(piece)*4 in ''.join(str(e) for e in [row[col] for row in board]) else False
    #else check for 3 in a row
    else:
        return True if str(piece)*3 in ''.join(str(e) for e in [row[col] for row in board]) else False

#this function checks for diagonal win condition
def winInDiag(board, piece):
    #diagonals for 3x3 board
    if ((len(board) == 3) and (len(board[0]) == 3) and (board[0][0] == piece) and (board[1][1] == piece) and (board[2][2] == piece)):
        return True
    if ((len(board) == 3) and (len(board[0]) == 3) and (board[0][2] == piece) and (board[1][1] == piece) and (board[2][0] == piece)):
        return True
    #diagonals for 4x3 board
    if ((len(board) == 4) and (len(board[0]) == 3) and (board[0][0] == piece) and (board[1][1] == piece) and (board[2][2] == piece)):
        return True
    if ((len(board) == 4) and (len(board[0]) == 3) and (board[1][0] == piece) and (board[2][1] == piece) and (board[3][2] == piece)):
        return True
    if ((len(board) == 4) and (len(board[0]) == 3) and (board[0][2] == piece) and (board[1][1] == piece) and (board[2][0] == piece)):
        return True
    if ((len(board) == 4) and (len(board[0]) == 3) and (board[1][2] == piece) and (board[2][1] == piece) and (board[3][0] == piece)):
        return True
    # diagonals for 3x4 board
    if ((len(board) == 3) and (len(board[0]) == 4) and (board[0][0] == piece) and (board[1][1] == piece) and (board[2][2] == piece)):
        return True
    if ((len(board) == 3) and (len(board[0]) == 4) and (board[0][1] == piece) and (board[1][2] == piece) and (board[2][3] == piece)):
        return True
    if ((len(board) == 3) and (len(board[0]) == 4) and (board[0][2] == piece) and (board[1][1] == piece) and (board[2][0] == piece)):
        return True
    if ((len(board) == 3) and (len(board[0]) == 4) and (board[0][3] == piece) and (board[1][2] == piece) and (board[2][1] == piece)):
        return True
    # diagonals for 4x4 board
    if ((len(board) == 4) and (len(board[0]) == 4) and (board[0][0] == piece) and (board[1][1] == piece) and (board[2][2] == piece) and (board[3][3] == piece)):
        return True
    if ((len(board) == 4) and (len(board[0]) == 4) and (board[0][3] == piece) and (board[1][2] == piece) and (board[2][1] == piece) and (board[3][0] == piece)):
        return True
    return False
#
#  Returns True if player with indicated piece type has won game
#       Uses winInRow, winInCol, winInDiag
#
#  Parameters:
#    board: The board to examine
#    peice: The piece type to look for (will be X or O)
#
#  Returns: True if player with indicated piece has winning arrangement in board
#
def won(board, piece):
    for r in range(len(board)):
        if winInRow(board, r, piece):
            return True
    for c in range(len(board[0])):
        if winInCol(board, c, piece):
            return True
    if winInDiag(board, piece):
        return True
    return False
#
#  Identify if a position will complete 3 in a row for a win
#
#  Parameters:
#    board: The game board to be checked, the piece type to be played
#
#  Returns: The row and column of the location the piece could be played to win.
#           If no winning play is possible then -1, -1 is returned.
#
def hint(board, piece):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if canPlay(board, r, c):
                play(board, r, c, piece)
                if won(board, piece):
                    board[r][c] = EMPTY
                    return r, c
                else:
                    board[r][c] = EMPTY
    return -1, -1

##############################################################################
#
# Only modify code above this point in the file
#
##############################################################################

# Uses students full and won functions to decide if game has ended in current board
def gameover(board):
    if full(board) or won(board, X) or won(board, O):
        return True
    return False


##############################################################################
#
# Code below is for testing student functions (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
#
##############################################################################

# Determine whether or not a function exists in the namespace at the time
# this function is called
# Parameters:
#   name: The name of the function to check the existence of
# Returns: True if the function exists, False otherwise
def functionExists(name):
    members = inspect.getmembers(sys.modules[__name__])
    for (n, m) in members:
        if n == name and inspect.isfunction(m):
            return True
    return False


# Run a series of tests on the createBoard function
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testCreateBoard():
    if not TESTPART1:
        return
    print("Testing createBoard...")
    # Does the createBoard function exist?
    if functionExists("createBoard"):
        print("  The function seems to exist...")
    else:
        print("  The createBoard function doesn't seem to exist...")
        return False

    for (rows, cols) in [(3, 3), (3, 4), (4, 3), (4, 4)]:
        # Try and call the function
        try:
            print("  Attempting to use createBoard(%d, %d)... " % (rows, cols))
            b = createBoard(rows, cols)
        except Exception as e:
            print("An exception occurred during the attempt.")
            traceback.print_exc(file=sys.stdout)
            return False

        # Does it have the correct return type?
        if type(b) is not list:
            print("    The value returned was a", str(type(b)) + ", not a list.")
            return False

        # Does the list have the corret number of elements?
        if len(b) != rows:
            print("    The board had", len(b), "rows when", rows, "were expected.")
            return False

        # Is each row a list?  Does each row have the correct length?
        for i in range(len(b)):
            if type(b[i]) is not list:
                print("    The row at index", i, "is a", str(type(b[i])) + ", not a list.")
                return False
            if len(b[i]) != cols:
                print("    The row at index", i, "had", len(b[i]), "elements when", cols, "were expected.")
                return False

        # Is every space on the board populated with an integer value between
        # 0 and syms (not including syms)?
        for r in range(0, len(b)):
            for c in range(0, len(b[r])):
                if type(b[r][c]) is not int:
                    print("    The value in row", r, "column", c, "is a", str(type(b[r][c])) + ", not an integer")
                    return False
                if b[r][c] != EMPTY:
                    print("    The integer in row", r, "column", c, "is a", b[r][c], "which is not EMPTY=0")
                    return False
    print("Success.")
    print()
    return True


# Run a series of tests on the canPlay and play functions
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testPlay():
    if not TESTPART2:
        return
    print("Testing play, canPlay...")
    # Does the play, canPlay function exist?
    if functionExists("play"):
        print("  The function play seems to exist...")
    else:
        print("  The play function doesn't seem to exist...")
        return False
    if functionExists("canPlay"):
        print("  The function canPlay seems to exist...")
    else:
        print("  The canPlay function doesn't seem to exist...")
        return False

    rows = 4
    cols = 4
    b = createBoard(rows, cols)
    print("  The canPlay for all spots in empty board...")
    for row in range(rows):
        for col in range(cols):
            r = canPlay(b, row, col)
            # Check return type and value? Should be able to play everywhere.
            if type(r) is not bool:
                print("    The value returned was a", str(type(r)) + ", not a boolean.")
                return False
            if r is False:
                message = "    The board " + str(b) + " is empty but canPlay(board, %d, %d) was False."
                print(message % (row, col))
                return False
            b[row][col] = X
            r = canPlay(b, row, col)
            # Check return type and value? Should not be able to play here now.
            if type(r) is not bool:
                print("    The value returned was a", str(type(r)) + ", not a boolean.")
                return False
            if r is True:
                message = "    The board " + str(b) + " has piece at this spot but canPlay(board, %d, %d) was True."
                print(message % (row, col))
                return False
            b[row][col] = EMPTY
    copy = deepcopy(b)
    # Change a copy of the board and check if result of play, canPlay matches changes expected
    print("  Test play/canPlay before and after playing at every location in 4x4 empty board")
    for row in range(rows):
        for col in range(cols):
            r0 = canPlay(b, row, col)
            if r0 is False:
                message = "   The board " + str(b) + " is empty but canPlay(board, %d, %d) was False."
                print(message % (row, col))
                return False
            # Play an X. Should not be able to play in this spot now.
            r1 = play(b, row, col, X)
            if type(r1) is not type(None):
                message = "    The value returned by play(board, %d, %d, %d) was a " + str(type(r1)) + ", not None."
                print(message % (row, col, X))
                return False
            copy[row][col] = X
            if copy != b:
                message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(copy)
                print(message % (row, col, X))
                return False
            r2 = canPlay(b, row, col)
            if r2 is True:
                message = "   The board " + str(b) + " is occupied but canPlay(board, %d, %d) was True."
                print(message % (row, col))
                return True
            # Play an EMPTY. Should be able to play in this spot now.
            r3 = play(b, row, col, EMPTY)
            if type(r3) is not type(None):
                message = "    The value returned by play(board, %d, %d, %d) was a " + str(type(r3)) + ", not None."
                print(message % (row, col, EMPTY))
                return False
            copy[row][col] = EMPTY
            if copy != b:
                message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(copy)
                print(message % (row, col, EMPTY))
                return False
            r4 = canPlay(b, row, col)
            if r4 is False:
                message = "   The board " + str(b) + " is empty but canPlay(board, %d, %d) was False."
                print(message % (row, col))
                return False
                # Play an O. Should not be able to play in this spot now.
            r5 = play(b, row, col, O)
            if type(r5) is not type(None):
                message = "    The value returned by play(board, %d, %d, %d) was a " + str(type(r5)) + ", not None."
                print(message % (row, col, O))
                return False
            copy[row][col] = O
            if copy != b:
                message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(copy)
                print(message % (row, col, O))
                return False
            r6 = canPlay(b, row, col)
            if r6 is True:
                message = "   The board " + str(b) + " is occupied but canPlay(board, %d, %d) was True."
                print(message % (row, col))
                return True
                # Play an EMPTY. Should be able to play in this spot now.
            r7 = play(b, row, col, EMPTY)
            if type(r7) is not type(None):
                message = "    The value returned by play(board, %d, %d, %d) was a " + str(type(r7)) + ", not None."
                print(message % (row, col, EMPTY))
                return False
            copy[row][col] = EMPTY
            if copy != b:
                message = "    The board " + str(b) + " returned by play(board, %d, %d, %d) was not " + str(copy)
                print(message % (row, col, EMPTY))
                return False
            r8 = canPlay(b, row, col)
            if r8 is False:
                message = "   The board " + str(b) + " is empty but canPlay(board, %d, %d) was False."
                print(message % (row, col))
                return False
    print("Success.")
    print()
    return True


# Run a series of tests on the full functions
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testFull():
    if not TESTPART3:
        return
    print("Testing full...")
    # Does the full function exist?
    if functionExists("full"):
        print("  The function full seems to exist...")
    else:
        print("  The full function doesn't seem to exist...")
        return False
    rows = 4
    cols = 4
    b = createBoard(rows, cols)
    # Does full return right for empty board?
    print("  Testing call to full for empty board.")
    r = full(b)
    if type(r) is not bool:
        print("    The value returned by full(board) was a", str(type(r)) + ", not a boolean.")
        return False
    if r == True:
        print("    The board ", b, " is empty but full returned True.")
        return False
    for row in range(rows):
        for col in range(cols):
            b[row][col] = X
    r = full(b)
    # Does full return right for full board?
    print("  Testing call to full for board full of Xs.")
    if type(r) is not bool:
        print("    The value returned by full(board) was a", str(type(r)) + ", not a boolean.")
        return False
    if r == False:
        print("    The board ", b, " is full but full returned False.")
        return False
    # Does full return right if we selectively remove single piece from anywhere on board?
    print("  Testing full for almost full board of Xs with one EMPTY spot")
    for row in range(rows):
        for col in range(cols):
            b[row][col] = EMPTY
            r = full(b)
            if type(r) is not bool:
                print("    The value returned by full(board) was a", str(type(r)) + ", not a boolean.")
                return False
            if r == True:
                print("    The board ", b, " is not full returned True.")
                return False
            b[row][col] = X
    for row in range(rows):
        for col in range(cols):
            b[row][col] = O
    r = full(b)
    # Does full return right for full board?
    print("  Testing call to full for board full of Os.")
    if type(r) is not bool:
        print("    The value returned by full(board) was a", str(type(r)) + ", not a boolean.")
        return False
    if r == False:
        print("    The board ", b, " is full but full returned False.")
        return False
    # Does full return right if we selectively remove single piece from anywhere on board?
    print("  Testing full for almost full board of Os with one EMPTY spot")
    for row in range(rows):
        for col in range(cols):
            b[row][col] = EMPTY
            r = full(b)
            if type(r) is not bool:
                print("    The value returned by full(board) was a", str(type(r)) + ", not a boolean.")
                return False
            if r == True:
                print("    The board ", b, " is not full returned True.")
                return False
            if r == True:
                print()
                return False
            b[row][col] = O
    print("Success.")
    print()
    return True


#
# Run a series of tests on the winInRow function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInRow():
    if not TESTPART4:
        return
    print("Testing winInRow...")

    # Does the winInRow function exist?
    if functionExists("winInRow"):
        print("  The function winInRow seems to exist...")
    else:
        print("  The winInRow function doesn't seem to exist...\n")
        return

    passed = 0
    failed = 0
    attempt = 0
    for (b, r, p, s) in [ \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, True), \
            ([[0, 0, 0, 0], \
              [2, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 2, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 1], \
              [0, 0, 0, 0]], 2, 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 2, 2]], 3, 2, True), \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 2, False), \
            ([[0, 0, 0, 0], \
              [2, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 1], \
              [0, 0, 0, 0]], 2, 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 2, 1]], 3, 1, False), \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for i in range(4):
                attempt += 1
                result = winInRow(b, i, p)
                # Does it have the correct return type?
                if type(result) is not bool:
                    print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
                    print("The board was:")
                    pprint(b)
                    print()
                    Failed += 1
                    return

                # Did it return the correct value
                if s and not result and r == i:
                    print("  Attempting to use winInRow Test", attempt, end="")
                    print("\nFAILED: The value returned was", str(result), " for row = ", i, " piece =", p,
                          "when True was expected.")
                    print("The board was:")
                    pprint(b)
                    print()
                    failed += 1
                    return
                # Did it return the correct value
                elif s and result and r != i:
                    print("  Attempting to use winInRow Test", attempt, end="")
                    print("\nFAILED: The value returned was", str(result), " for row = ", i, " piece =", p,
                          "when False was expected.")
                    print("The board was:")
                    pprint(b)
                    print()
                    failed += 1
                    return
                elif not s and result:
                    print("  Attempting to use winInRow Test", attempt, end="")
                    print("\nFAILED: The value returned was", str(result), " for row = ", i, " piece =", p,
                          "when False was expected.")
                    print("The board was:")
                    pprint(b)
                    print()
                    failed += 1
                    return
                passed += 1
        except Exception as e:
            print("  Attempting to use winInRow Test", attempt, end="")
            print("\nFAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(b)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            return
    print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the winInCol function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInCol():
    if not TESTPART4:
        return
    print("Testing winInCol...")

    # Does the winInCol function exist?
    if functionExists("winInCol"):
        print("  The function winInCol seems to exist...")
    else:
        print("  The winInCol function doesn't seem to exist...\n")
        return

    passed = 0
    failed = 0
    attempt = 0
    for (b, r, p, s) in [ \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, True), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 1, 2, True), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, 1, True), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 3, 2, True), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 2, False), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 1, 1, False), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, 2, False), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 3, 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 0, 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 0, 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for i in range(4):
                attempt += 1
                result = winInCol(b, i, p)
                # Does it have the correct return type?
                if type(result) is not bool:
                    print("  Attempting to use winInCol Test", attempt, end="")
                    print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
                    print("The board was:")
                    pprint(b)
                    print()
                    Failed += 1
                    return

                # Did it return the correct value
                elif s and not result and r == i:
                    print("  Attempting to use winInCol Test", attempt, end="")
                    print("\nFAILED: The value returned was", str(result), " for row = ", i, " piece =", p,
                          "when True was expected.")
                    print("The board was:")
                    pprint(b)
                    print()
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif s and result and r != i:
                    print("  Attempting to use winInCol Test", attempt, end="")
                    print("\nFAILED: The value returned was", str(result), " for row = ", i, " piece =", p,
                          "when False was expected.")
                    print("The board was:")
                    pprint(b)
                    print()
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                elif not s and result:
                    print("  Attempting to use winInCol Test", attempt, end="")
                    print("\nFAILED: The value returned was", str(result), " for row = ", i, " piece =", p,
                          "when False was expected.")
                    print("The board was:")
                    pprint(b)
                    print()
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                passed += 1
        except Exception as e:
            print("  Attempting to use winInCol Test", attempt, end="")
            print("\nFAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(b)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print("Failed ", failed, "test cases", "of", attempt)
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the winInDiag function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInDiag():
    if not TESTPART5:
        return
    print("Testing winInDiag...")

    # Does the winInDiag function exist?
    if functionExists("winInDiag"):
        print("  The function winInDiag seems to exist...")
    else:
        print("  The winInDiag function doesn't seem to exist...\n")
        return

    passed = 0
    failed = 0
    attempt = 0
    for (b, p, s) in [ \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, True), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 2, 0]], 2, False), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            ([[0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 2, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 2, False), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 2, 0]], 1, False), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 2, False), \
            ([[0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 1, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False)]:

        # Attempt the function call
        try:
            attempt += 1
            result = winInDiag(b, p)
            # Does it have the correct return type?
            if type(result) is not bool:
                print("  Attempting to use winInDiag Test", attempt, end="")
                print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
                print("The board was:")
                pprint(b)
                print()
                Failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if s and not result:
                print("  Attempting to use winInDiag Test", attempt, end="")
                print("\nFAILED: The value returned was", str(result), " piece =", p, "when True was expected.")
                print("The board was:")
                pprint(b)
                print()
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not s and result:
                print("  Attempting to use winInDiag Test", attempt, end="")
                print("\nFAILED: The value returned was", str(result), " for piece =", p, "when False was expected.")
                print("The board was:")
                pprint(b)
                print()
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as e:
            print("  Attempting to use winInDiag Test", attempt, end="")
            print("\nFAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(b)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print("Failed ", failed, "test cases", "of", attempt)
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the won function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWon():
    if not TESTPART6:
        return
    print("Testing won...")

    # Does the won function exist?
    if functionExists("won"):
        print("  The function won seems to exist...")
    else:
        print("  The won won doesn't seem to exist...\n")
        return

    passed = 0
    failed = 0
    attempt = 0
    for (b, p, s) in [ \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [2, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 1], \
              [0, 0, 0, 0]], 1, True), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 2, 2]], 2, True), \
            ([[1, 1, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [2, 2, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 1, 1], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 2, 2]], 1, False), \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 2, True), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 1, True), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 2, True), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 2, False), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 1, False), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, False), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 1, False), \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, True), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 2, 0]], 2, False), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, True), \
            ([[0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 2, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 2, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 2, False), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 2, 0]], 1, False), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 2, False), \
            ([[0, 0, 2, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 1]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, False), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, False)]:

        # Attempt the function call
        try:
            attempt += 1
            result = won(b, p)
            # Does it have the correct return type?
            if type(result) is not bool:
                print("  Attempting to use won Test", attempt, end="")
                print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
                print("The board was:")
                pprint(b)
                print()
                Failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if s and not result:
                print("  Attempting to use won Test", attempt, end="")
                print("\nFAILED: The value returned was", str(result), " piece =", p, "when True was expected.")
                print("The board was:")
                pprint(b)
                print()
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not s and result:
                print("  Attempting to use won Test", attempt, end="")
                print("\nFAILED: The value returned was", str(result), " for piece =", p, "when False was expected.")
                print("The board was:")
                pprint(b)
                print()
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as e:
            print("  Attempting to use won Test", attempt, end="")
            print("\nFAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(b)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print("Failed ", failed, "test cases", "of", attempt)
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


#
# Run a series of tests on the hint function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testHint():
    if not TESTPART7:
        return
    print("Testing hint...")

    # Does the hint function exist?
    if functionExists("hint"):
        print("  The function hint seems to exist...")
    else:
        print("  The winInDiag hint doesn't seem to exist...\n")
        return

    passed = 0
    failed = 0
    attempt = 0
    for (b, p, r, c) in [ \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 2), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 1), \
            ([[0, 0, 0, 0], \
              [2, 0, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, 1, 1), \
            ([[0, 0, 0, 0], \
              [2, 2, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, 1, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1], \
              [0, 0, 0, 0]], 1, 2, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1], \
              [0, 0, 0, 0]], 1, 2, 1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 0, 2, 2]], 2, 3, 1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 0, 2]], 2, 3, 2), \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [2, 0, 2, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [2, 2, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 0, 2, 2]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [2, 2, 0, 2]], 1, -1, -1), \
 \
            ([[1, 1, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 2), \
            ([[1, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[1, 0, 1, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, 0, 1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 1, 0, 1]], 1, 3, 2), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 1]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 1, 1]], 1, 3, 1), \
 \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, 2, 0), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 0), \
            ([[0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 2, 1, 1), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0]], 2, 2, 1), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0]], 1, 2, 2), \
            ([[0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 1, 1, 2), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 2, 1, 3), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2]], 2, 2, 3), \
 \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 2, -1, -1), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 2, -1, -1), \
            ([[0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 2, 0, 0]], 1, -1, -1), \
            ([[0, 2, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0], \
              [0, 2, 0, 0]], 1, -1, -1), \
            ([[0, 0, 1, 0], \
              [0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0]], 2, -1, -1), \
            ([[0, 0, 1, 0], \
              [0, 0, 0, 0], \
              [0, 0, 1, 0], \
              [0, 0, 1, 0]], 2, -1, -1), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2], \
              [0, 0, 0, 2]], 1, -1, -1), \
            ([[0, 0, 0, 2], \
              [0, 0, 0, 2], \
              [0, 0, 0, 0], \
              [0, 0, 0, 2]], 1, -1, -1), \
 \
            ([[1, 0, 0, 0], \
              [1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, 2, 0), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0]], 1, -1, -1), \
            ([[1, 0, 0, 0], \
              [0, 0, 0, 0], \
              [1, 0, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 0), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, 2, 3), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, -1, -1), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1], \
              [0, 0, 0, 1]], 1, 1, 3), \
 \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, 2, 2), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 2), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 1, 2, 2), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 1, 1, 2), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 2, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 2, -1, -1), \
 \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 2, -1, -1), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 2, -1, -1), \
            ([[1, 0, 0, 0], \
              [0, 1, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 1]], 2, -1, -1), \
            ([[0, 0, 0, 1], \
              [0, 0, 0, 0], \
              [0, 1, 0, 0], \
              [1, 0, 0, 0]], 2, -1, -1), \
            ([[0, 2, 0, 0], \
              [0, 0, 2, 0], \
              [0, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 2, 0, 0], \
              [2, 0, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [2, 0, 0, 0], \
              [0, 2, 0, 0], \
              [0, 0, 0, 0]], 1, -1, -1), \
            ([[0, 0, 0, 0], \
              [0, 0, 0, 0], \
              [0, 0, 2, 0], \
              [0, 2, 0, 0]], 1, -1, -1)

    ]:

        # Attempt the function call
        try:
            attempt += 1
            row, col = hint(b, p)
            # Does it have the correct return type?
            if type(row) is not int:
                print("  Attempting to use hint Test", attempt, end="")
                print("\nFAILED: The value returned was a", str(type(row)) + ", not a Integer.")
                print("The board was:")
                pprint(b)
                print()
                Failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            if type(col) is not int:
                print("  Attempting to use hint Test", attempt, end="")
                print("\nFAILED: The value returned was a", str(type(col)) + ", not a Integer.")
                print("The board was:")
                pprint(b)
                print()
                Failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if r != row or c != col:
                print("  Attempting to use hint Test", attempt, end="")
                print("\nFAILED: The value returned was", str(row), ",", str(col), "for piece =", p, "when", str(r),
                      ",", str(c), " was expected.")
                print("The board was:")
                pprint(b)
                print()
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as e:
            print("  Attempting to use hint Test", attempt, end="")
            print("\nFAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(b)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print("Failed ", failed, "test cases", "of", attempt)
    else:
        print("Passed all tests. <", attempt, ">")

    print()
    return


##############################################################################
##
##  Code for drawing (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
##
##############################################################################

# Draw X with lines in box beginning at (x,y) with given square size and color
def drawX(x, y, size, color="black"):
    setColor(color)
    line(x + 15, y + 15, x + size - 15, y + size - 15)
    line(x + size - 15, y + 15, x + 15, y + size - 15)


# Draw O with lines in box beginning at (x,y) with given square size and color
def drawO(x, y, size, color="black"):
    setColor(color)
    setFill(None)
    ellipse(x + 15, y + 15, size - 30, size - 30)


# Draw hint information and X or O based on piece in given row, col of board
def drawHint(board, row, col, piece):
    setColor("orange")
    setFill(None)
    rows = len(board)
    cols = len(board[0])
    row_diff = int(HEIGHT / rows)
    col_diff = int(WIDTH / cols)
    rect(col * col_diff, row * row_diff, row_diff + 1, col_diff + 1)
    if piece == X:
        drawX(col * col_diff, row * row_diff, min(row_diff, col_diff), "orange")
    elif piece == O:
        drawO(col * col_diff, row * row_diff, min(row_diff, col_diff), "orange")


# Draw the board in given color
def drawBoard(board, color="black"):
    setColor("white")
    rect(0, 0, WIDTH, HEIGHT)
    setColor(color)
    rows = len(board)
    cols = len(board[0])
    row_diff = int(HEIGHT / rows)
    col_diff = int(WIDTH / cols)
    for y in range(row_diff, HEIGHT - 1, row_diff):
        line(0, y, WIDTH, y)
    for x in range(col_diff, WIDTH - 1, col_diff):
        line(x, 0, x, HEIGHT)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                drawX(col * col_diff, row * row_diff, min(row_diff, col_diff), color)
            elif board[row][col] == O:
                drawO(col * col_diff, row * row_diff, min(row_diff, col_diff), color)


# Setup window and draw initial white line to make it resize
def setupWindow():
    background("white")
    setColor("white")
    resize(WIDTH, HEIGHT)
    line(0, 0, 1, 1)


##############################################################################
##
##  Code for AI and hint for 3x3 tic-tac-toe (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
##
##############################################################################

# Main minmax, calls subfunction for recursion
# uses game board with player1 trying to decide move vs player 2, limit to depth given
def minmax1(board, player1, player2, depth):
    # Find all valid moves, shuffle for interesting
    moves = []
    rows = list(range(0, len(board)))
    shuffle(rows)
    cols = list(range(0, len(board[0])))
    shuffle(cols)
    for row in rows:
        for col in cols:
            if canPlay(board, row, col):
                moves.append([row, col])
    values = []
    # for each move if game won save value (make bigger than regular to show next play wins)
    # if not won recurse on game state for opponent playing
    for move in moves:
        row = move[0]
        col = move[1]
        play(board, row, col, player1)
        if won(board, player1):
            values.append(20)
        elif won(board, player2):
            values.append(-20)
        elif full(board):
            values.append(0)
        else:
            values.append(minmax2(board, player1, player2, False, depth - 1))
        play(board, row, col, EMPTY)
    # Return best move found, next play wins first, followed by future wins, and ties, losses, and next play losses
    for i in range(len(moves)):
        if values[i] == 20:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == 10:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == 0:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == -10:
            return moves[i][0], moves[i][1]
    for i in range(len(moves)):
        if values[i] == -20:
            return moves[i][0], moves[i][1]


# Recursion minmax, calls itself for recursion
# uses game board with player1 trying to decide move vs player 2, limit to depth given
# not of maximze means it is player1's turn and not maximize is player2's turn
def minmax2(board, player1, player2, maximize, depth):
    if depth == 0:
        return 0
    # Find all valid moves, shuffle for interesting
    moves = []
    rows = list(range(0, len(board)))
    shuffle(rows)
    cols = list(range(0, len(board[0])))
    shuffle(cols)
    for row in rows:
        for col in cols:
            if canPlay(board, row, col):
                moves.append([row, col])
    values = []
    # for each move if game won save value
    # if not won recurse on game state for opponent playing
    for move in moves:
        row = move[0]
        col = move[1]
        if maximize:
            play(board, row, col, player1)
        else:
            play(board, row, col, player2)
        if gameover(board):
            if won(board, player1):
                play(board, row, col, EMPTY)
                return 10
            elif won(board, player2):
                play(board, row, col, EMPTY)
                return -10
            elif full(board):
                play(board, row, col, EMPTY)
                return 0
        result = minmax2(board, player1, player2, not maximize, depth - 1)
        values.append(result)
        if maximize and result == 10:
            play(board, row, col, EMPTY)
            break
        elif not maximize and result == -10:
            play(board, row, col, EMPTY)
            break
        play(board, row, col, EMPTY)
    # Return maximial or minimal value found depending on recursion level
    if maximize:
        return max(values)
    else:
        return min(values)


# Calling AI, if level 4 we do full recursive minmax, if not we recurse only to certain depth
# If level=0 AI we just pick random open spot
def AI(board, level, human, computer):
    if level == 4:
        return minmax1(board, computer, human, len(board) * len(board[0]) + 1)
    elif level > 0:
        return minmax1(board, computer, human, level * 2)
    rows = list(range(0, len(board)))
    shuffle(rows)
    cols = list(range(0, len(board[0])))
    shuffle(cols)
    trying = True
    for row in rows:
        for col in cols:
            if canPlay(board, row, col):
                return row, col
    return -1, -1


##############################################################################
##
##  Main function (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
##
##############################################################################

def main():
    if not testCreateBoard():
        return
    if not testPlay():
        return
    testFull()
    testWinInRow()
    testWinInCol()
    testWinInDiag()
    testWon()
    testHint()
    setupWindow()
    rows = "?"
    while rows != "3" and rows != "4":
        rows = input("Pick a board row size (3 or 4): ")
    rows = int(rows)
    cols = "?"
    while cols != "3" and cols != "4":
        cols = input("Pick a board col size (3 or 4): ")
    cols = int(cols)
    board = createBoard(rows, cols)
    drawBoard(board)
    difficulty = "?"
    if rows == cols == 3:
        while difficulty != "0" and difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != "4":
            difficulty = input(
                "Pick a difficulty [0=RANDOM,1=WINS,2=LOOKAHEAD1,3=LOOKAHEAD2,4=FULLAI]:\n(Note a difficulty of 4 uses an AI algorithm that may slow down some computers and you will have to wait.)\n")
    else:
        while difficulty != "0" and difficulty != "1" and difficulty != "2" and difficulty != "3":
            difficulty = input("Pick a difficulty [0=RANDOM,1=WINS,2=LOOKAHEAD1,3=LOOKAHEAD2]: ")
    difficulty = int(difficulty)
    human = "?"
    while human != "X" and human != "O":
        human = input("Enter choice of X or O: ")
    if human == "X":
        print("Human is X.")
        print("Computer is O.")
        human = X
        computer = O
    else:
        print("Human is O.")
        print("Computer is X.")
        human = O
        computer = X
    player = X
    plays = 0
    while not gameover(board):
        value = (rows * cols) - plays
        if (value > 0):
            complexity = factorial(value)
            print("Estimated complexity of current game:", complexity)
        if human == player:
            print("Human player's turn.")
            h = input("Enter 'h' for a game winning hint; ")
            if h == "h":
                row1, col1 = hint(board, human)
                row2, col2 = hint(board, computer)
                if row1 != -1:
                    print("Hint is row =", row1, "and col =", col1)
                    drawHint(board, row1, col1, human)
                elif row2 != -1:
                    print("Hint is row =", row2, "and col =", col2)
                    drawHint(board, row2, col2, human)
                else:
                    print("No hint")
            elif h == "a":
                row = -1
                col = -1
                if rows == cols == 3:
                    row, col = minmax1(board, human, computer, 5)
                else:
                    row, col = minmax1(board, human, computer, 4)
                if row != -1:
                    print("Hint is row =", row, "and col =", col)
                    drawHint(board, row, col, human)
                else:
                    print("No hint")

            trying = True
            while trying:
                selection = list(range(0, rows))
                row = -1
                while row < 0 or row > rows - 1:
                    try:
                        row = int(input("Enter row " + str(selection) + ": "))
                    except Exception as e:
                        print("Invalid row entered!")
                selection = list(range(0, cols))
                col = -1
                while col < 0 or col > cols - 1:
                    try:
                        col = int(input("Enter col " + str(selection) + ": "))
                    except Exception as e:
                        print("Invalid row entered!")
                if canPlay(board, row, col):
                    play(board, row, col, human)
                    trying = False
                else:
                    print("Chosen location board[" + str(row) + "][" + str(col) + "] is full!")
                print("Human plays in row", row, "and column", str(col) + ".")
                player = computer
        else:
            row, col = AI(board, difficulty, human, computer)
            play(board, row, col, computer)
            print("AI plays in row", row, "and column", str(col) + ".")
            player = human
        drawBoard(board)
        plays += 1
    setFont("Times", "50", "bold")

    if won(board, X):
        if human == X:
            drawBoard(board, "green")
        else:
            drawBoard(board, "red")
        setColor("black")
        text(300, 300, "X won!")
    elif won(board, O):
        if human == O:
            drawBoard(board, "green")
        else:
            drawBoard(board, "red")
        setColor("black")
        text(300, 300, "O won!")
    else:
        drawBoard(board, "blue")
        setColor("black")
        text(300, 300, "Board full. Draw.")


main()