from playingPiece import playingPiece
from rep_enum import repEnum


class PieceK(playingPiece):
    def __init__(self):
        super().__init__(repEnum.K)
