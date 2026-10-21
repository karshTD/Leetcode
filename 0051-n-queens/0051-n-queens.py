class Solution:
    def solveNQueens(self, n):
        board = [-1] * n
        result = []

        def is_safe(row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    return False
            return True

        def backtrack(row):
            if row == n:
                
                temp = []
                for i in range(n):
                    line = ['.'] * n
                    line[board[i]] = 'Q'
                    temp.append("".join(line))
                result.append(temp)
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

        backtrack(0)
        return result