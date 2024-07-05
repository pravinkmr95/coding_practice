from player import Player
from Game import TicTacToe
from pieceO import PieceO
from pieceX import PieceX
from pieceK import PieceK


if __name__ == '__main__':
    game = TicTacToe(4)

    piece1 = PieceX()
    piece2 = PieceO()
    piece3 = PieceK()

    player1 = Player(piece1)
    player2 = Player(piece2)
    player3 = Player(piece3)
    game.start_game(player1, player2, player3)
