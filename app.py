import tkinter as tk
from tkinter import messagebox
import random

def is_valid_move(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid_move(board, row, col, num):
            board[row][col] = num
    return board

def check_solution():
    user_board = [[int(cells[i][j].get() or 0) for j in range(9)] for i in range(9)]
    if solve_sudoku(user_board):
        messagebox.showinfo("Sudoku", "Correct Solution!")
    else:
        messagebox.showerror("Sudoku", "Incorrect Solution!")

def reset_board():
    global sudoku_board
    sudoku_board = generate_sudoku()
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            if sudoku_board[i][j] != 0:
                cells[i][j].insert(0, str(sudoku_board[i][j]))
                cells[i][j].config(state='disabled')
            else:
                cells[i][j].config(state='normal')

root = tk.Tk()
root.title("Sudoku")

sudoku_board = generate_sudoku()
cells = []

for i in range(9):
    row_cells = []
    for j in range(9):
        cell = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
        cell.grid(row=i, column=j, padx=5, pady=5)
        if sudoku_board[i][j] != 0:
            cell.insert(0, str(sudoku_board[i][j]))
            cell.config(state='disabled')
        row_cells.append(cell)
    cells.append(row_cells)

tk.Button(root, text="Check", command=check_solution).grid(row=9, column=3, columnspan=3, pady=10)
tk.Button(root, text="Reset", command=reset_board).grid(row=9, column=6, columnspan=3, pady=10)

root.mainloop()
