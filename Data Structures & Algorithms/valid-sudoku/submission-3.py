class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet, colSet, boxSet = {}, {}, {}
        for row in range(len(board)):
            for col in range(len(board[0])):
                curr = board[row][col]
                if curr != '.':
                    if row not in rowSet:
                        rowSet[row] = set(curr)
                    elif curr in rowSet[row]:
                        return False
                    else:
                        rowSet[row].add(curr)

                    if col not in colSet:
                        colSet[col] = set(curr)
                    elif curr in colSet[col]:
                        return False
                    else:
                        colSet[col].add(curr)
                    
                    if (row//3, col//3) not in boxSet:
                        boxSet[(row//3, col//3)] = set(curr)
                    elif curr in boxSet[(row//3, col//3)]:
                        return False
                    else:
                        boxSet[(row//3, col//3)].add(curr)

        return True