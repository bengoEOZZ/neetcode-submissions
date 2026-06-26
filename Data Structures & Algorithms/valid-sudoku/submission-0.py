class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowSet, colSet, boxSet = {}, {}, {}
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != '.':
                    if row not in rowSet:
                        rowSet[row] = set(board[row][col])
                    elif board[row][col] in rowSet[row]:
                        return False
                    else:
                        rowSet[row].add(board[row][col])

                    if col not in colSet:
                        colSet[col] = set(board[row][col])
                    elif board[row][col] in colSet[col]:
                        return False
                    else:
                        colSet[col].add(board[row][col])

                    if (row//3, col//3) not in boxSet:
                        boxSet[(row//3, col//3)] = set(board[row][col])
                    elif board[row][col] in boxSet[(row//3, col//3)]:
                        return False
                    else:
                        boxSet[(row//3, col//3)].add(board[row][col])
        return True
