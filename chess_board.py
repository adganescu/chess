# Chessboard.py

"""
Things a chessboard needs

"""

class ChessBoard:

    
    w_sq = "\u25A0"
    w_f_row = ["\u2659" for i in range(8)]
    w_b_row = "R N B Q \u2654 B N R".split()
    
    b_sq = "\u25A1"
    b_f_row = ["\u265F" for i in range(8)]
    b_b_row = ["\u265F" for i in range(8)]


    def __init__(self,  w_sq=w_sq, b_sq=b_sq, 
                        w_b_row=w_b_row, w_f_row=w_f_row,
                        b_b_row=b_b_row, b_f_row=b_f_row):
        self.board = [    
            b_b_row,
            b_f_row,
            [w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq],
            [b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq],
            [w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq],
            [b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq],
            w_f_row,
            w_b_row]

    def __str__(self):
        
        output = "" 

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                output += " {}".format(str(self.board[i][j]))
            output += "\n"

        return output 