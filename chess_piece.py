import unicode_values

class ChessPiece:

    def __init__(self, color, piece):
        self.color, self.piece = color, piece

    def __str__(self):
        return unicode_values.pieces_to_text.get((self.color, self.piece))



        