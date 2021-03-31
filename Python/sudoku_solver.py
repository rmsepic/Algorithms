from typing import List
from enum import Enum

class Cell(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    EMPTY = "."

class Sudoku: 
    LENGTH = 9

    def __init__(self, board: List[List[Cell]]):
        self.board = board
        
    def dfs(self, row: int, col: int) -> bool:
        for i in range(row, self.LENGTH):
            col = 0
            for j in range(col, self.LENGTH):
                if (self.board[i][j] == Cell.EMPTY.value):
                    # Try to place 1-9 in the empty cell
                    for s in Cell:
                        if s.value not in self.board[i] and s.value not in self.getCol(j) and self.notInBox(s.value, i,j):
                            self.board[i][j] = s.value
                            flag = self.dfs(i, j)

                            if flag is True:
                                return True
 
                            self.board[i][j] = Cell.EMPTY.value

                    return False

        return True

    def getCol(self, col: int) -> List[Cell]:
        return [row[col] for row in self.board]

    def notInBox(self, value: int, i: int, j: int) -> bool:
        row = i - i % 3
        col = j - j % 3

        for x in range(row, row + 3):
            for y in range(col, col + 3):
                if (self.board[x][y] == value):
                    return False 

        return True

    def printBoard(self):
        for row in self.board:
            print(row)

        print()

    # This function can be called from anywhere
    # Call this function on some board that needs to be solved
    def solve(board: List[List[Cell]]) -> None:
        sudoku = Sudoku(board)
        sudoku.dfs(0, 0)


if __name__ == "__main__":
    #board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Sudoku.solve(board)

    print("Answer: ")
    for row in board:
        print(row)