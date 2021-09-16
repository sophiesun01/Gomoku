##Testing Code
import copy
def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def is_empty(board):
    for row in range(len(board)):
        for entry in range(len(board[0])):
            if board[row][entry] == " ":
                return True
    return False

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    ''' y_end and x_end are integers between 0-7 which represents the coordinate it ends at
    This function analyses the sequence of length length that ends at location (y end, x end).
    The function returns "OPEN" if the sequence is open,
    "SEMIOPEN" if the sequence if semi-open, and
    "CLOSED" if the sequence is closed.
    Assume that the sequence is complete'''
    y_start1 = y_end - d_y * length #the space to the left of the sequence
    # print(y_start1)
    x_start1 = x_end - d_x * length
    # print(x_start1)
    y_start = y_end - d_y * length + d_y #the first space of the sequence
    # print(y_start)
    x_start = x_end - d_x * length + d_x #the first space of the sequence
    # print(x_start)
    y_end1 = y_end + d_y
    # print(y_end1)
    x_end1 = x_end + d_x

    if  (0 <=  y_start1 <=7 and 0 <=  y_end1 <=7 and 0 <=  x_start1 <=7 and 0 <=  x_end1 <=7) and board[y_start1][x_start1] == " " and board[y_end1][x_end1] == " ":
        return "OPEN"
    elif (0 <=  y_start1 <=7 and 0 <=  y_end1 <=7 and 0 <=  x_start1 <=7 and 0 <=  x_end1 <=7) and board[y_start1][x_start1] != " " and board[y_end1][x_end1] != " ":
        return "CLOSED" #both ends are in range but both ends have full spaces
    elif (y_end1 < 0 or y_end1 > 7 or x_end1 < 0 or x_end1 > 7) and (y_start1 < 0 or y_start1 > 7 or x_start1 < 0 or x_start1 >7):
        return "CLOSED" #both ends are out of range
    elif ((y_end1 < 0 or y_end1 > 7) or (x_end1 < 0 or x_end1 > 7)) and board[y_start1][x_start1] != " ":
        return "CLOSED" #end is out of range, start is full space
    elif ((y_start1 < 0 or y_start1 > 7) or (x_start1 < 0 or x_start1 >7)) and board[y_end1][x_end1] != " ":
        return "CLOSED" #start is out of range, end is full space
    else:
        return "SEMIOPEN"

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    i = 0
    len = 0
    open_seq_count = 0
    semi_open_seq_count = 0
    while i <= (8-length):
        e = i

        while 0 <= (y_start + d_y * e) <= 7 and 0 <= (x_start + d_x * e) <= 7 and board[y_start + d_y * e][x_start + d_x * e] == col:
            e += 1
            len += 1



        if len == length:
            y_start_seq = y_start + i * d_y
            # print(y_start_seq)
            x_start_seq = x_start + i * d_x
            # print(x_start_seq)
            y_end_seq = y_start_seq + d_y * (len) - d_y
            # print(y_end_seq)
            x_end_seq = x_start_seq + d_x * (len) - d_x
            # print(x_end_seq)
            if is_bounded(board, y_end_seq, x_end_seq, len, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count += 1
            elif is_bounded(board, y_end_seq, x_end_seq, len, d_y, d_x) == "OPEN":
                open_seq_count += 1
            i += len
        else:
            i += 1
        len = 0

    return open_seq_count, semi_open_seq_count


# def detect_rows(board, col, length):
#     open_seq_count = 0
#     semi_open_seq_count = 0
#     for row in range(len(board)):
#         open_count, semi_open_count = detect_row(board, col, row, 0, length, 0, 1)
#         open_seq_count += open_count
#         semi_open_seq_count += semi_open_count
#         open_count, semi_open_count = detect_row(board, col, 0, row, length, 1, 0)
#         open_seq_count += open_count
#         semi_open_seq_count += semi_open_count
#         open_count, semi_open_count = detect_row(board, col, row, 0, length, 1, 1)
#         open_seq_count += open_count
#         semi_open_seq_count += semi_open_count
#         open_count, semi_open_count = detect_row(board, col, 0, row, length, 1, 1)
#         open_seq_count += open_count
#         semi_open_seq_count += semi_open_count
#         open_count, semi_open_count = detect_row(board, col, row, 7, length, 1, -1) # 7 because last row of the board
#         open_seq_count += open_count
#         semi_open_seq_count += semi_open_count
#         open_count, semi_open_count = detect_row(board, col, 0, row, length, 1, -1)
#         open_seq_count += open_count
#         semi_open_seq_count += semi_open_count
#     return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    open_seq_count = 0
    semi_open_seq_count = 0
    for row in range(len(board)):
        open_count, semi_open_count = detect_row(board, col, row, 0, length, 0, 1)
        open_seq_count += open_count
        semi_open_seq_count += semi_open_count
        open_count, semi_open_count = detect_row(board, col, 0, row, length, 1, 0)
        open_seq_count += open_count
        semi_open_seq_count += semi_open_count
        open_count, semi_open_count = detect_row(board, col, row, 0, length, 1, 1) #(0, 0 is counted twice)
        open_seq_count += open_count
        semi_open_seq_count += semi_open_count
        open_count, semi_open_count = detect_row(board, col, row, 7, length, 1, -1) # 7 because last row of the board (0, 7 is counted twice)
        open_seq_count += open_count
        semi_open_seq_count += semi_open_count
    for row in range(len(board)-1):
        open_count, semi_open_count = detect_row(board, col, 0, (row + 1), length, 1, 1)
        open_seq_count += open_count
        semi_open_seq_count += semi_open_count

        open_count, semi_open_count = detect_row(board, col, 0, row, length, 1, -1)
        open_seq_count += open_count
        semi_open_seq_count += semi_open_count

    return open_seq_count, semi_open_seq_count

print(detect_rows(board, 'b', 4))


def is_win(board):
    if detect_wins(board, "b") == "No win" and detect_wins(board, "w") == "No win":
        for i in range(8):
            for y in range(8):
                if board[i][y] == " ":
                    return "Continue playing"
        return "Draw"
    elif detect_wins(board, "b") == "b":
        return "Black won"
    elif detect_wins(board, "w") == "w":
        return "White won"

# print(is_win(board))

def detect_win(board, col, y_start, x_start, length, d_y, d_x):
    i = 0
    len = 0
    open_seq_count = 0
    semi_open_seq_count = 0
    while i <= (8-length):
        e = i

        while 0 <= (y_start + d_y * e) <= 7 and 0 <= (x_start + d_x * e) <= 7 and board[y_start + d_y * e][x_start + d_x * e] == col:
            e += 1
            len += 1
        if len == 5:
            return col
        elif len == 0:
            i += 1
        else:
            i += len
        len = 0
    return "none"

# print(detect_win(board, "w", 2, 7, 6, 1, -1))
# print(detect_win(board, "b", 7, 0, 5, 1, 1))
# print(detect_win(board, 'b', 0, 6, 5, 1, 0))

# def detect_win(board, col, y_start, x_start, length, d_y, d_x):
#     for i in range(3):
#         if board[y_start][x_start] == col:
#             for n in range(length):
#                 if 0 > (y_start + d_y * n) or (y_start + d_y * n) > 7 or 0 > (x_start + d_x * n) or (x_start + d_x * n) > 7 or board[y_start+d_y * n][x_start + d_x * n] != col:
#                     return "none"
#             return col
# def detect_win(board, col, y_start, x_start, length, d_y, d_x):
#     count = 0
#     for i in range(3):
#         if 0 <= (y_start + d_y * i) <= 7 and 0 <= (x_start + d_x * i) <= 7 and board[y_start + d_y * i][x_start + d_x * i] == col:
#             for n in range(length):
#                 if 0 > (y_start + d_y * (i + n)) or (y_start + d_y * (i + n)) > 7 or 0 > (x_start + d_x * (i + n)) or (x_start + d_x * (i + n)) > 7 or board[y_start+d_y * (i + n)][x_start + d_x * (i + n)] != col:
#                     count = 0
#                 else:
#                     count += 1
#
#             if count == 5:
#                 return col
#             count = 0
#     return "none"


def detect_wins(board, col):
    for row in range(len(board)):
        if detect_win(board, col, row, 0, 5, 0, 1) == col:
            return col
        elif detect_win(board, col, 0, row, 5, 1, 0) == col:
            return col
        elif detect_win(board, col, row, 0, 5, 1, 1) == col:
            return col
        elif detect_win(board, col, 0, row, 5, 1, 1) == col:
            return col
        elif detect_win(board, col, row, 7, 5, 1, -1) == col:# 7 because last row of the board
            return col
        elif detect_win(board, col, 0, row, 5, 1, -1) == col:
            return col
    return "No win"
# print(detect_wins(board, "b"))

def test_is_bounded():
    board = make_empty_board(8)
    x = 7; y = 0; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 2
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

# def detect_row(board, col, y_start, x_start, length, d_y, d_x):
#     # x = 5; y = 1; d_x = 0; d_y = 1; length = 3
#     # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     i = 0
#     len = 0
#     open_seq_count = 0
#     semi_open_seq_count = 0
#     while i <= length:
#         while board[y_start + d_y * len][x_start + d_x * len] == col:
#             len += 1
#
#         y_start += i * d_y
#         # print(y_start)
#         x_start += i * d_x
#         y_end = y_start + d_y * (len) - d_y
#         x_end = x_start + d_x * (len) - d_x
#         if is_bounded(board, y_end, x_end, len, d_y, d_x) == "SEMIOPEN":
#             semi_open_seq_count += 1
#         elif is_bounded(board, y_end, x_end, len, d_y, d_x) == "OPEN":
#             open_seq_count += 1
#         i += 1 + len
#         len = 0
#
#     return open_seq_count, semi_open_seq_count




def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    x = 5; y = 5; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print(detect_row(board, "w", 0,x,length,d_y,d_x))
        print("TEST CASE for detect_row FAILED")
# print(test_detect_row())

#MY VERSION THAT TESTS DIAGONALS

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 1; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (0,1):
        print("TEST CASE for detect_rows PASSED")
        print(detect_rows(board, col, length))
    else:
        print("TEST CASE for detect_rows FAILED")
        print(detect_rows(board, col, length))
# print(test_detect_rows())

def search_max(board):
    new_board = copy.deepcopy(board)
    max_score = -10000000
    move_y = -1
    move_x = -1

    for y in range(0, 8):
        for x in range(0, 8):
            if new_board[y][x] == " ":
                new_board[y][x] = "b"

            if score(new_board) > max_score:
                max_score = max(score(new_board), max_score)
                move_y = y
                move_x = x
            new_board[y][x] = board[y][x]

    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

board = make_empty_board(8)
# print_board(board)
# print(detect_row(board, "w", 0, 5, 3, 1, 0))
# print(is_bounded(board, 3, 5, 3, 1, 0))
# print(test_is_bounded())
#
# test_detect_row()

# board = make_empty_board(8)
# x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'b'
# put_seq_on_board(board, y, x, d_y, d_x, length, "b")
# print_board(board)

# print(search_max(board))
# print(score(board))

board = make_empty_board(8)
print(is_win(board))

##Chek FOR WIN DIRECTION(1, 1)
# x = 3; y = 0; d_x = 1; d_y = 1; length = 4; col = 'w'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# x = 1; y = 0; d_x = 1; d_y = 1; length = 5; col = 'b'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# print_board(board)
# search_max(board)
# print(detect_win(board, col, 1, 1, 5, 0, 1))
# print(detect_wins(board, "b"))
# print(is_win(board))

##CHECK FOR WIN Direction (0, 1)
# x = 3; y = 0; d_x = 1; d_y = 1; length = 4; col = 'w'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# x = 1; y = 0; d_x = 1; d_y = 0; length = 5; col = 'b'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# print_board(board)
# print(detect_win(board, "b", 0, 0, 5, 0, 1))
# print(is_win(board))

##CHECK FOR WIN Direction (1, -1)
# x = 3; y = 0; d_x = 1; d_y = 1; length = 1; col = 'w'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# x = 7; y = 2; d_x = -1; d_y = 1; length = 5; col = 'w'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# print_board(board)
# print(is_win(board))

##CHECK FOR WIN Direction (1, 0)
# x = 3; y = 0; d_x = 0; d_y = 1; length = 5; col = 'w'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# x = 7; y = 1; d_x = 0; d_y = 1; length = 2; col = 'b'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# print_board(board)
# print(detect_win(board, "b", 0, 0, 5, 1, 0))
# print(is_win(board))

##CHECK MAX SCORE
# x = 1; y = 1; d_x = 1; d_y = 1; length = 4; col = 'w'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# x = 5; y = 5; d_x = 0; d_y = 1; length = 1; col = 'b'
# put_seq_on_board(board, y, x, d_y, d_x, length, col)
# print_board(board)
# print(score(board))
# print(search_max(board))

##RANDOM CHECK
# board = make_empty_board(8)
# put_seq_on_board(board, 0, 4, 1, -1, 5, "w")
# #print_board(board)
# print(is_win(board)) #White won
# board[3][1] = "b"
# #print_board(board)
# print(is_win(board)) #Continue playing"
# put_seq_on_board(board, 1, 5, 1, -1, 5, "w")
# #print_board(board)
# print(is_win(board)) #White won
# board[0][6] = "b"
# #print_board(board)
# print(is_win(board)) #White won
# board[1][5] = "b"
# #print_board(board)
# print(is_win(board)) #Continue playing"
# put_seq_on_board(board, 0, 2, 1, 1, 5, "w")
# print(is_win(board)) #White won
# board[2][4] = "b"
# print(is_win(board)) #Continue playing
# put_seq_on_board(board, 0, 3, 1, 1, 5, "w")
# print(is_win(board)) #White won
# board[2][5] = "b"
# print(is_win(board)) #Continue playing
# board[0][5] = "w"
# print(is_win(board)) #Continue playing
# board[0][5] = "w"
# board[0][1] = "w"
# print(is_win(board)) #White won
# board[2][5] = "b"
# print(is_win(board)) #White won
# board[0][2] = "b"
# print(is_win(board)) #Continue playing
# put_seq_on_board(board, 6, 1, 0, 1, 5, "w")
# print(is_win(board)) #White won
# board[6][0] = "b"
# print(is_win(board)) #White won
# board[6][6] = "b"
# print(is_win(board)) #White won
# board[6][3] = "b"
# print(is_win(board)) #Continue playing
# board[5][2] = "w"
# board[3][2] = "w"
# print(is_win(board)) #White won
# board[7][2] = "b"
# print(is_win(board)) #White won
# board[1][2] = "b"
# print(is_win(board)) #White won
# board[4][2] = "b"
# print(is_win(board)) #Continue playing
# board[3][4] = "b"
# board[0][7] = "b"
# board[0][0] = "w"
# board[7][3] = "w"
# board[7][1] = "b"
# board[7][0] = "b"
#
# print_board(board)
# print(is_win(board)) #Continue playing
# board[7][3] = "w"
# put_seq_on_board(board, 5, 3, 0, 1, 4, "b")
# put_seq_on_board(board, 7, 4, 0, 1, 4, "b")
# board[5][7] = "w"
# put_seq_on_board(board, 4, 2, 0, 1, 4, "b")
# board[4][1] = "w"
# print_board(board)
# print(is_win(board)) #Continue playing
# put_seq_on_board(board, 2, 0, 1, 0, 4, "b")
# #print_board(board)
# print(is_win(board))#Continue playing
# put_seq_on_board(board, 3, 7, 1, 0, 4, "w")
# #print_board(board)
# print(is_win(board))#Continue playing
# put_seq_on_board(board, 2, 4, 0, 1, 4, "b")
# board[5][0] = "w"
# board[1][0] = "w"
# board[2][3] = "w"
# put_seq_on_board(board, 0, 1, 1, 0, 3, "w")
# board[1][6] = "w"
# board[1][7] = "w"
# print(is_win(board)) # "Draw"
# print("\n\n")

###Everything says is same except should say black won not white won
# board = make_empty_board(8)
# put_seq_on_board(board, 0, 4, 1, -1, 5, "b")
# #print_board(board)
# print(is_win(board)) #White won
# board[3][1] = "w"
# #print_board(board)
# print(is_win(board)) #Continue playing"
# put_seq_on_board(board, 1, 5, 1, -1, 5, "b")
# #print_board(board)
# print(is_win(board)) #White won
# board[0][6] = "w"
# #print_board(board)
# print(is_win(board)) #White won
# board[1][5] = "w"
# #print_board(board)
# print(is_win(board)) #Continue playing"
# put_seq_on_board(board, 0, 2, 1, 1, 5, "b")
# print(is_win(board)) #White won
# board[2][4] = "w"
# print(is_win(board)) #Continue playing
# put_seq_on_board(board, 0, 3, 1, 1, 5, "b")
# print(is_win(board)) #White won
# board[2][5] = "w"
# print(is_win(board)) #Continue playing
# board[0][5] = "b"
# print(is_win(board)) #Continue playing
# board[0][5] = "b"
# board[0][1] = "b"
# print(is_win(board)) #White won
# board[2][5] = "w"
# # print_board(board)
# print(is_win(board)) #White won
# board[0][2] = "w"
# print(is_win(board)) #Continue playing
# put_seq_on_board(board, 6, 1, 0, 1, 5, "b")
# print(is_win(board)) #White won
# board[6][0] = "w"
# print(is_win(board)) #White won
# board[6][6] = "w"
# print(is_win(board)) #White won
# board[6][3] = "w"
# print(is_win(board)) #Continue playing
# board[5][2] = "b"
# board[3][2] = "b"
# print(is_win(board)) #White won
# board[7][2] = "w"
# print(is_win(board)) #White won
# board[1][2] = "w"
# print(is_win(board)) #White won
# board[4][2] = "w"
# print(is_win(board)) #Continue playing
# board[3][4] = "w"
# board[0][7] = "w"
# board[0][0] = "b"
# board[7][3] = "b"
# board[7][1] = "w"
# board[7][0] = "w"
# #print_board(board)
# print(is_win(board)) #Continue playing
# board[7][3] = "b"
# put_seq_on_board(board, 5, 3, 0, 1, 4, "w")
# put_seq_on_board(board, 7, 4, 0, 1, 4, "w")
# board[5][7] = "b"
# put_seq_on_board(board, 4, 2, 0, 1, 4, "w")
# board[4][1] = "b"
# print(is_win(board)) #Continue playing
# put_seq_on_board(board, 2, 0, 1, 0, 4, "w")
# #print_board(board)
# print(is_win(board))#Continue playing
# put_seq_on_board(board, 3, 7, 1, 0, 4, "b")
# #print_board(board)
# print(is_win(board))#Continue playing
# put_seq_on_board(board, 2, 4, 0, 1, 4, "w")
# board[5][0] = "b"
# board[1][0] = "b"
# board[2][3] = "b"
# put_seq_on_board(board, 0, 1, 1, 0, 3, "b")
# board[1][6] = "b"
# board[1][7] = "b"
# print(is_win(board)) # "Draw"
#
#
#
#
