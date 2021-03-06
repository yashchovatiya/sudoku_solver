def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row(arr, row, num):
    for i in range(9):
        if (arr[row][i] == num):
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(9):
        if (arr[i][col] == num):
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)


def solve_sudoku(arr):
    l = [0, 0]
    if not find_empty_location(arr, l):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if (check_location_is_safe(arr, row, col, num)):
            arr[row][col] = num
            if (solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False


if __name__ == "__main__":
    grid = [[0 for x in range(9)] for y in range(9)]
x = True
while x == True:
    M = 0
    input_from_user = input("Enter your Sudoku`:")
    if input_from_user == 'quit':
        break
    for a in range(0, 9):
        for b in range(0, 9):
            grid[a][b] = int(input_from_user[M])
            M = M + 1
    print('your sudoku')
    print_board(grid)
    if (solve_sudoku(grid)):
        print('solved sudoku')
        print_board(grid)
    else:
        print("No solution exists")
