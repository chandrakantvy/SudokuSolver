import numpy as np


def isAnyZero(sudoku, r_c):
    m, n = sudoku.shape
    for i in range(m):
        for j in range(n):
            if sudoku[i][j] == 0:
                r_c[0] = i
                r_c[1] = j
                return True
    return False


def isValid(sudoku, value, r, c):
    for i in range(9):
        if sudoku[i][c] == value or sudoku[r][i] == value:
            return False
    p = (r // 3) * 3
    q = (c // 3) * 3
    p1 = p + 3
    q1 = q + 3
    while p < p1:
        while q < q1:
            if sudoku[p][q] == value:
                return False
            q += 1
        p += 1
    return True


def solveSudoku(sudoku):
    r_c = [0, 0]
    while isAnyZero(sudoku, r_c):
        r = r_c[0]
        c = r_c[1]
        for value in range(1, 10):
            if isValid(sudoku, value, r, c):
                sudoku[r][c] = value
                if solveSudoku(sudoku):
                    return True
        sudoku[r][c] = 0
        return False
    else:
        return True


if __name__ == "__main__":
    sudoku = np.zeros((9, 9), dtype=np.uint8)

    with open("sudoku.txt", "r") as sudoku_matrix:
        line = sudoku_matrix.readline()
        i = 0
        while line:
            sudoku[i] = line.split(" ")
            i += 1
            line = sudoku_matrix.readline()
    solved = solveSudoku(sudoku)
    if solved:
        print(sudoku)
    else:
        print("No solution")
