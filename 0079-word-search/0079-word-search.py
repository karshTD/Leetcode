class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def backtrack(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            found = (backtrack(i+1, j, idx+1) or
                     backtrack(i-1, j, idx+1) or
                     backtrack(i, j+1, idx+1) or
                     backtrack(i, j-1, idx+1))

            board[i][j] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False