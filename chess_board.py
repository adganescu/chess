import unicode_values

class ChessBoard:
    w_sq = unicode_values.w_sq
    w_b_row = unicode_values.w_b_row
    w_f_row = unicode_values.w_f_row

    b_sq = unicode_values.b_sq
    b_b_row = unicode_values.b_b_row
    b_f_row = unicode_values.b_f_row

    def __init__(self,  w_sq=w_sq, b_sq=b_sq, 
                        w_b_row=w_b_row, w_f_row=w_f_row,
                        b_b_row=b_b_row, b_f_row=b_f_row):
        
        self.board = [    
            ["a", "b", "c", "d", "e", "f", "g", "f"],
            b_b_row,
            b_f_row,
            [w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq],
            [b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq],
            [w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq],
            [b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq],
            w_f_row,
            w_b_row,
            ["a", "b", "c", "d", "e", "f", "g", "f"],]

    def __str__(self):
        
        output = "" 

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                output += " {}".format(str(self.board[i][j]))
            output += "\n"

        return output 