class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check each cell
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (!isValid(board, i, j, board[i][j])) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

private:
    bool isValid(vector<vector<char>>& board, int row, int col, char num) {
        // Check row
        for (int x = 0; x < 9; x++) {
            if (x != col && board[row][x] == num) return false;
        }
        
        
        for (int x = 0; x < 9; x++) {
            if (x != row && board[x][col] == num) return false;
        }
        
     
        int boxRow = row - row % 3;
        int boxCol = col - col % 3;
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int currRow = boxRow + i;
                int currCol = boxCol + j;
                if (currRow != row && currCol != col && board[currRow][currCol] == num) {
                    return false;
                }
            }
        }
        
        return true;
    }
};