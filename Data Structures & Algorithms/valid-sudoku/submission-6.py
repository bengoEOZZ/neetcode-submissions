class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet, colSet, boxSet = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                curr = board[row][col]
                if curr != '.':
                    if curr in rowSet[row] or curr in colSet[col] or curr in boxSet[(row//3, col//3)]:
                        return False
                    rowSet[row].add(curr)
                    colSet[col].add(curr)
                    boxSet[(row//3, col//3)].add(curr)
        return True