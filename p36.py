def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    
    rows = {i: [] for i in range(9)}
    columns = {i: [] for i in range(9)}
    squares = {i: [] for i in range(9)}

    for row in range(9):
        for col in range(9):
            if board[row][col] != ".":

                # checking for row condition
                if board[row][col] in rows[row]:
                    return False
                else:
                    rows[row].append(board[row][col])

                # checking for column condition
                if board[row][col] in columns[col]:
                    return False
                else:
                    columns[col].append(board[row][col])

                # checking for 3x3 square
                row_index = (row//3) * 3
                col_index = col//3
                square_index = row_index + col_index

                # print(f"row index: {row}\ncol index: {col}\nsquare_index: {square_index}\n")
                if board[row][col] in squares[square_index]:
                    return False
                else:
                    squares[square_index].append(board[row][col])
    return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

board2 = [[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board2))