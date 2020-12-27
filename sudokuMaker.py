class SudokuMaker:
    def __init__(self):
        self.board = self.new_board()
        self.print_board()

    def new_board(self):
        tmp = []
        for row in range(9):
            tmp.append([])
            for col in range(9):
                tmp[row].append(0)
        return tmp

    def print_board(self):
        print("\n-------------------------")
        for row in range(9):
            print("| ", end="")
            for col in range(9):
                print(self.board[row][col], end=" ")
                if col % 3 == 2:
                    print("| ", end="")
            if row % 3 == 2:
                print("\n-------------------------")
            else:
                print()