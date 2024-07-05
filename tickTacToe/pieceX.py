from playingPiece import playingPiece
from rep_enum import repEnum


class PieceX(playingPiece):
    def __init__(self):
        super().__init__(repEnum.X)
