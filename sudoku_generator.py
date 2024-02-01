import math
import random


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        self.box_length=int(math.sqrt(self.row_length))
        row=[]
        for i in range(0, self.row_length):
            for i in range(0, self.row_length):
                row.append(0)
            self.board.append(row)
            row=[]


    def get_board(self):
        return self.board

    def print_board(self):
        index=0
        for row in self.board:
            print(*self.board[index])
            index+=1

    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True


    def valid_in_box(self, row_start, col_start, num):
        end_row = row_start + self.box_length
        end_col = col_start +self.box_length
        for r in range(row_start, end_row):
            for c in range(col_start, end_col):
                if self.board[r][c] == num:
                    return False
        return True


    def is_valid(self, row, col, num):
        return(
        self.valid_in_row(row, num) and
        self.valid_in_col(col, num) and
        self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num)
        )


    def fill_box(self, row_start, col_start):
        num_bank=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        store=col_start
        end=row_start
        end2=col_start
        while row_start < end+3:
            while col_start<end2+3:
                if self.board[row_start][col_start] == 0:
                    insert = random.choice(num_bank)
                    self.board[row_start][col_start] = insert
                    num_bank.remove(insert)
                col_start+=1
            col_start=store
            row_start+=1

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i,i)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        count = 0
        while count < self.removed_cells:
            x = random.randint(0,8)
            y = random.randint(0, 8)
            if self.board[x][y] == 0:
                continue
            else:
                self.board[x][y] = 0
                count += 1

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

