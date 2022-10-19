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
            [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "],
            w_b_row,
            w_f_row,
            ["6", w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, "6"],
            ["5", b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, "5"],
            ["4", w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, "4"],
            ["3", b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, b_sq, w_sq, "3"],
            b_f_row,
            b_b_row,
            [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "],]

        notation = [col + row for row in "12345678" for col in "abcdefh"]
        board_positions = [(row, col) for row in range(8, 0, -1) for col in range(1, 8, 1)]
        self.index = dict(zip(notation, board_positions))

    def __str__(self):
        
        output = "" 

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                output += " {}".format(str(self.board[i][j]))
            output += "\n"

        return output 

    def move_piece(self, move, color):

        target_tile = self.board[self.index.get(move)[0]][self.index.get(move)[1]]
        



        print(start_loc)
        print(target_loc)
        # print(str(res))

        return