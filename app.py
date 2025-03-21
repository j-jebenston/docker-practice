import random

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid_move(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]
    for _ in range(10):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
    solve_sudoku(grid)
    return grid

def remove_numbers(grid, difficulty=40):
    for _ in range(difficulty):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        grid[row][col] = 0

def save_sudoku(grid, filename="sudoku.txt"):
    with open(filename, "w") as f:
        for row in grid:
            f.write(" ".join(str(num) if num != 0 else '.' for num in row) + "\n")

def load_sudoku(filename="sudoku.txt"):
    with open(filename, "r") as f:
        return [[int(num) if num != '.' else 0 for num in line.split()] for line in f]

def main():
    sudoku = generate_sudoku()
    remove_numbers(sudoku)
    print_grid(sudoku)
    save_sudoku(sudoku)

if __name__ == "__main__":
    main()

