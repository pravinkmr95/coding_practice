from collections import deque, defaultdict


class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = []
        self.initialize_game()

    def initialize_game(self):
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    print("_", end=" ")
                else:
                    print(self.board[i][j].symbol.value, end=" ")
            print()

    def valid_input(self, x, y):
        if x >= self.size or y >= self.size:
            print("indexes Out of bound")
            return False
        if self.board[x][y] == 0:
            return True
        else:
            return False

    def is_winner(self, player):
        # check rows
        for i in range(self.size):
            row = self.board[i]
            row_dict = defaultdict(int)
            for piece in row:
                row_dict[piece] += 1
            if row_dict[player.playing_piece] == self.size:
                return True
        # check columns
        for j in range(self.size):
            column_dict = defaultdict(int)
            for i in range(self.size):
                column_dict[self.board[i][j]] += 1
            if column_dict[player.playing_piece] == self.size:
                return True

        # check diagonal
        diagonal_dict = defaultdict(int)
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    diagonal_dict[self.board[i][j]] += 1
        if diagonal_dict[player.playing_piece] == self.size:
            return True
        # reverse diagonal
        _diagonal_dict = defaultdict(int)
        for i in range(self.size):
            for j in range(self.size):
                if i == self.size-1-j:
                    _diagonal_dict[self.board[i][j]] += 1
        if _diagonal_dict[player.playing_piece] == self.size:
            return True
        return False

    def draw_check(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
        return True

    def start_game(self, player1, player2, player3):
        self.print_board()
        game_on = True
        queue = deque()
        queue.append(player1)
        queue.append(player2)
        queue.append(player3)
        while game_on:
            player = queue.popleft()
            print("Enter index of your move {}".format(player.playing_piece.symbol.value))
            inp = input("Please enter space separated position")
            print(inp)
            x, y = inp.split(" ")
            x = int(x)
            y = int(y)
            if self.valid_input(x, y) is False:
                print("Invalid Move. Please put the valid index.")
                queue.appendleft(player)
                continue
            self.board[x][y] = player.playing_piece
            winner = self.is_winner(player)
            if winner:
                print("Winner is {}".format(player.playing_piece.symbol.value))
                game_on = False
            else:
                if self.draw_check():
                    print(".....Game draw...")
                    game_on = False
                queue.append(player)
            self.print_board()
