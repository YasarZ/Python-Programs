def is_valid_move(grid, row, column, number):
    #checking the row and column and seeing if the number exists already
    for x in range (9):
        if grid[row][x] == number:
            return False
        
    for x in range (9):    
        if grid[x][column] == number:
            return False

    cornerRow = row - row % 3
    cornerColumn = column - column % 3
    #checking the box to see if the number exists within the box already
    for x in range(3):
        for y in range(3):
            if grid[cornerRow + x][cornerColumn + y] == number:
                return False

    return True


def solve(grid, row, column):
    if column == 9: #checking to see if we went past the number of columns allowed
        if row == 8: #checking to see if we hit the end of the rows
            return True #we have already reached the solution
        row += 1 #increasing the row
        column = 0 #reseting to the start of the column
    
    if grid[row][column] > 0:
        return solve(grid, row, column + 1)

    for num in range(1,10):
        if is_valid_move(grid, row, column, num): #is it valid, True or Fase
            grid[row][column] = num #set it to that value if it's true
            
            if solve(grid, row, column + 1):
                return True

        grid[row][column] = 0

    return False



grid = [[0, 0, 6, 1, 5, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [7, 0, 0, 0, 8, 4, 0, 0, 0],
        [3, 0, 0, 9, 0, 8, 5, 6, 1],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 0, 8],
        [0, 0, 7, 0, 0, 0, 6, 0, 3],
        [5, 3, 0, 6, 0, 0, 9, 8, 4],
        [0, 4, 0, 0, 0, 1, 0, 0, 7]]


if solve(grid, 0, 0):
    for i in range (9):
        for j in range(9):
            if (j == 2 or j == 5 or j == 8):
                print (grid[i][j], end = "      ")
            else:
                print (grid[i][j], end = " ")
            if ((i == 2 or i == 5 or i == 8) and j == 8):
                print()
            
        print()
else:
    print("No solution")