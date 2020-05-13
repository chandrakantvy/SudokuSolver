import tkinter as tk
import numpy as np

def createGrid(sudokuFrame, **kwargs):
    margin = kwargs['margin']
    side = kwargs['length']
    width = kwargs['w']
    height = kwargs['h']
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


def createPuzzle(sudokuFrame, puzzle, **kwargs):
    for i in range(9):
        for j in range(9):
            x = kwargs['margin'] + i * kwargs['length'] + kwargs['length'] // 2
            y = kwargs['margin'] + j * kwargs['length'] + kwargs['length'] // 2
            num = puzzle[i][j]
            if num != 0:
                sudokuFrame.create_text(x, y, text=num, tags='numbers', font=("Pursia", 20))


def click(event):
    global x, y
    x = event.x
    for i in range(9):
        if i * 60 + 10 < x < i * 60 + 70:
            x = i * 60 + 10
            break
    
    y = event.y
    for i in range(9):
        if i * 60 + 10 < y < i * 60 + 70:
            y = i * 60 + 10
            break
    


def move(event):
    pass


if __name__ == '__main__':
    x = y = 0
    win = tk.Tk()
    win.title("Sudoku")
    win.geometry('600x800')
    win.resizable(width=False, height=False)
    sudokuFrame = tk.Canvas(win, width=560, height=560)
    sudokuFrame.pack()
    sudokuFrame.bind("<Button-1>", click)
    sudokuFrame.bind("<Enter>", move)
    createGrid(sudokuFrame, margin=10, length=60, w=560, h=560)

    path = "sudoku.txt"
    puzzle = np.zeros((9, 9), dtype=np.uint8)
    getPuzzle(path, puzzle)
    solution = np.zeros((9, 9), dtype=np.uint8)
    getSolution(path, solution)

    createPuzzle(sudokuFrame, puzzle, margin=10, length=60)
    
    win.mainloop()