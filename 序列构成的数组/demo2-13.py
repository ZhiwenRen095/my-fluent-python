""" 注意区分可变对象和不可变对象 """

board = [['_'] * 3 for _ in range(3)]
print(board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
print(id(board[0][0]))
print(id(board[0][1]))
print(id(board[1][1]) == id(board[0][0]))


# str '_' 是不可变对象，*3操作会创建3个新的对象
board[1][2] = 'x'
print(board)  # [['_', '_', '_'], ['_', '_', 'x'], ['_', '_', '_']]
print(id(board[1][1]) == id(board[0][0]))
print(id(board[1][2]) == id(board[0][0]))

# 相当于
example_weird_board_1 = []
for _ in range(3):
    raw_1 = ['_'] * 3
    example_weird_board_1.append(raw_1)

weird_board = [['_'] * 3] * 3
print(weird_board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# 相当于
raw_2 = ['_'] * 3
example_weird_board_2 = []
for _ in range(3):
    example_weird_board_2.append(raw_2)

# ['_', '_', '_'] 是list可变对象，外层再*3，会复制对象引用地址
weird_board[1][2] = 'x'
print(weird_board)  # [['_', '_', 'x'], ['_', '_', 'x'], ['_', '_', 'x']]
