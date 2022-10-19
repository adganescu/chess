# White pieces and square

w_sq = "\u25A0"
w_pawn = "\u2659"
w_rook = "\u2656"
w_bishop = "\u2657"
w_knight = "\u2658"
w_queen = "\u2655"
w_king = "\u2654"

# White rows

w_f_row = ["7", w_pawn, w_pawn, w_pawn, w_pawn, w_pawn, w_pawn, w_pawn, w_pawn, "7"] 
w_b_row = ["8", w_rook, w_knight, w_bishop, w_queen, w_king, w_bishop, w_knight, w_rook, "8"]

# Black pieces and square

b_sq = "\u25A1"
b_pawn = "\u265F"
b_rook = "\u265C"
b_bishop = "\u265D"
b_knight = "\u265E"
b_queen = "\u265B"
b_king = "\u265A"

# Black rows

b_f_row = ["2", b_pawn, b_pawn, b_pawn, b_pawn, b_pawn, b_pawn, b_pawn, b_pawn, "2"] 
b_b_row = ["1", b_rook, b_knight, b_bishop, b_queen, b_king, b_bishop, b_knight, b_rook, "1"]

# Black Pieces to text equivalent

pieces = [(color, piece) for color in "wb" for piece in "RNBQKP"]
text_equivalent = [b_rook, b_knight, b_bishop, b_queen, b_king, b_pawn, w_rook, w_knight, w_bishop, w_queen, w_king, w_pawn]
pieces_to_text = dict(zip(pieces, text_equivalent))