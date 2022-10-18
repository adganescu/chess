# White pieces and square

w_sq = "\u25A0"
w_pawn = "\u2659"
w_rook = "\u2656"
w_bishop = "\u2657"
w_knight = "\u2658"
w_queen = "\u2655"
w_king = "\u2654"

# White rows

w_f_row = [w_pawn for i in range(8)] 
w_b_row = [w_rook, w_knight, w_bishop, w_queen, w_king, w_bishop, w_knight, w_rook]

# Black pieces and square

b_sq = "\u25A1"
b_pawn = "\u265F"
b_rook = "\u265C"
b_bishop = "\u265D"
b_knight = "\u265E"
b_queen = "\u265B"
b_king = "\u265A"

# Black rows

b_f_row = [b_pawn for i in range(8)] 
b_b_row = [b_rook, b_knight, b_bishop, b_queen, b_king, b_bishop, b_knight, b_rook]

