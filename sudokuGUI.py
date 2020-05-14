import tkinter as tk
import numpy as np
from tkinter import messagebox as mbox
import random


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


def getPuzzleSolution(path, puzzle, solution):
    n = random.randint(1, 1000001)
    fp = open(path, "r")
    for i, line in enumerate(fp):
        if i == n:
            quiz, sol = line.split(',')

    for i in range(9):
        q = quiz[i*9:i*9+9]
        s = sol[i*9:i*9+9]
        for j in range(9):
            puzzle[j][i] = int(q[j])
            solution[j][i] = int(s[j])
    fp.close()



def createPuzzle(sudokuFrame, puzzle, col_arr, **kwargs):
    margin = kwargs['margin'] 
    length = kwargs['length']
    for i in range(9):
        for j in range(9):
            num = puzzle[i][j]
            if num != 0:
                x = margin + i * length + length // 2
                y = margin + j * length + length // 2
                if col_arr[i][j] == "black":
                    alreadyExisting.append((margin + i * length, margin + j * length))      
                sudokuFrame.create_text(x, y, text=num, tags='numbers', font=("Pursia", 20), fill=col_arr[i][j])



def createCursor(x, y, length):
    sudokuFrame.delete("cursor")
    if (x, y) not in alreadyExisting:
        sudokuFrame.create_rectangle(x, y, x+length, y+length, outline='red', width=2, tags="cursor")


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


def isAnyZero(sudoku):
    m, n = sudoku.shape
    for i in range(m):
        for j in range(n):
            if sudoku[i][j] == 0:


def zeroPresent(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return True
    return False


def isWon(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != solution[i][j]:
                return False
    return True


def keyEvent(event):
    global x, y
    xc = x // 60
    yc = y // 60
    if event.char in '123456789':
        color = "blue" if isValid(puzzle, int(event.char), xc, yc) else "red"
        puzzle[xc][yc] = int(event.char)
        col_arr[xc][yc] = color
        sudokuFrame.delete("numbers")
        createPuzzle(sudokuFrame, puzzle, col_arr, margin=10, length=60)
        if not zeroPresent(puzzle):
            if isWon(puzzle):
                mbox.showinfo("Victory", "YOU HAVE WON!!!")
                exit()


def clickEvent(event):
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
    createCursor(x, y, length=60)
    if (x, y) not in alreadyExisting:
        sudokuFrame.bind_all("<Key>", keyEvent)
    else:
        sudokuFrame.unbind_all("<Key>")


def isWin(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != solution[i][j]:
                return False
    return True


def keyEvent(event):
    global x, y
    xc = x // 60
    yc = y // 60
    num = event.char
    if num in '123456789':
        # color = "blue" if isValid(puzzle, int(num), xc, yc) else "red"
        puzzle[xc][yc] = int(num)
        sudokuFrame.delete("numbers")
        createPuzzle(sudokuFrame, puzzle, margin=10, length=60)
        if not isAnyZero(puzzle):
            if isWin(puzzle):
                mbox.showinfo("you won")
                exit()
                
        
if __name__ == '__main__':
    x = y = 0
    win = tk.Tk()
    win.title("Sudoku")
    win.geometry('600x600')
    win.resizable(width=False, height=False)
    sudokuFrame = tk.Canvas(win, width=560, height=560)
    sudokuFrame.pack()
    sudokuFrame.bind("<Button-1>", clickEvent)
    createGrid(sudokuFrame, margin=10, length=60, w=560, h=560)

    path = "sudoku.csv"
    puzzle = np.zeros((9, 9), dtype=np.uint8)
    col_arr = np.full((9, 9), "black")
    solution = np.zeros((9, 9), dtype=np.uint8)
    getPuzzleSolution(path, puzzle, solution)

    alreadyExisting = []
    createPuzzle(sudokuFrame, puzzle, col_arr, margin=10, length=60)

    win.mainloop()