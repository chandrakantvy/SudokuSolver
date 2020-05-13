import tkinter as tk
import numpy as np

def createGrid(win, margin, side, width, height):
    for i in range(10):
        color = "blue" if i % 3 == 0 else "gray"
        x0 = margin
        y0 = margin + side * i
        x1 = width - margin
        y1 = side * i + margin
        sudokuFrame.create_line(x0, y0, x1, y1, fill=color)

        x0 = side * i + margin
        y0 = margin
        x1 = side * i + margin
        y1 = height - margin
        sudokuFrame.create_line(x0, y0, x1, y1, fill=color)


def getPuzzle(path, puzzle):
    with open("sudoku.txt", "r") as sudoku_matrix:
        line = sudoku_matrix.readline()
        i = 0
        while line:
            puzzle[i] = line.split(" ")
            i += 1
            line = sudoku_matrix.readline()


def getSolution(path, solution):
    pass


if __name__ == '__main__':
    win = tk.Tk()
    win.title("Sudoku")
    win.geometry('600x800')
    win.resizable(width=False, height=False)
    sudokuFrame = tk.Canvas(win, width=560, height=560)
    sudokuFrame.pack()
    createGrid(sudokuFrame, 10, 60, 560, 560)

    path = "sudoku.txt"
    puzzle = np.zeros((9, 9), dtype=np.uint8)
    getPuzzle(path, puzzle)
    solution = np.zeros((9, 9), dtype=np.uint8)
    getSolution(path, solution)
    
    win.mainloop()