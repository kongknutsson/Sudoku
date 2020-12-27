class SudokuSolver:

    def solve(self, board):
        #Looper over brettet
        for row in range(9):
            for col in range(9):
                #Funnet tom rute
                if board[row][col] == 0:
                    #Sjekker alle muligheter
                    for n in range(1, 10):
                        if self.possible(board, row, col, n):
                            # Funnet et tall som går inn
                            board[row][col] = n
                            self.solve(board)
                            board[row][col] = 0
                    return
        self.print_board(board)

    def print_board(self, board):
        print("\n-------------------------")
        for row in range(9):
            print("| ", end="")
            for col in range(9):
                print(board[row][col], end=" ")
                if col % 3 == 2:
                    print("| ", end="")
            if row % 3 == 2:
                print("\n-------------------------")
            else:
                print()

    def possible(self, board, r, c, num):
        # sjekker opp og ned
        for row in range(9):
            if board[row][c] == num:
                return False
        for col in range(9):
            if board[r][col] == num:
                return False
        # Sjekker firkanten
        r0 = (r//3)*3
        c0 = (c//3)*3
        for i in range(3):
            for j in range(3):
                if board[r0+i][c0+j] == num:
                    return False
        return True

