class TicTacToeBoard:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def get_current_player(self):
        return self.current_player
    
    def play(self, row, col):
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_win(self):
        # Check for rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '-':
                return True
        
        # Check for columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != '-':
                return True
        
        # Check for diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
            return True
        
        # No win yet
        return False
    
    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        
        # All spaces filled
        return True
    
    def get_mark_at(self, row, col):
        return self.board[row][col]
