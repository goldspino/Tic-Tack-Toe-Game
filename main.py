class Game:
    def __init__(self):
        self.turn = "X"
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.win_poss = [
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],

            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],

            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]]
        ]

    def __repr__(self):
        print_str = ""
        for row in self.board:
            for symbol in row:
                print_str += symbol
                print_str += " "
            print_str += "\n"
        
        return print_str

    def start(self):
        while True:
            print(self)
            valid = self.ask_move()
            self.check_win()
            
            if valid:
                if self.turn == "X":
                    self.turn = "O"
                elif self.turn == "O":
                    self.turn = "X"

    def ask_move(self):
        coords = input("Enter your move in the format xy: ")
        try:
            x = int(coords[0]) - 1
            y = int(coords[1]) - 1

            if self.board[y][x] == "_":
                self.board[y][x] = self.turn
                return True
            else:
                return False
        except:
            return False

    def check_win(self):
        for squares in self.win_poss:
            c1 = squares[0]
            c2 = squares[1]
            c3 = squares[2]

            won = ""
            if self.board[c1[0]][c1[1]] == self.board[c2[0]][c2[1]] == self.board[c3[0]][c3[1]]:
                if self.board[c1[0]][c1[1]] != "_":
                    won = self.board[c1[0]][c1[1]]

            if won != "":
                print("Yay! You won " + won + "!")
                quit()


game = Game()
game.start()