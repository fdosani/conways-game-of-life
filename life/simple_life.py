import sys
import time


def neighbours(x, y, grid):
    """
    takes in the cells x,y coordinates and the grid.
    based on this it will return the surrounding cells by validating them first.
    If the cells are not valid (out of range) it will just return a dead cell "."

    The returned output is a list of the 8 (minus the actual cell itself)
    coordinates representing alive or dead
    """
    output = []
    output.append(grid[x-1][y-1]) if validate_cell(x-1, y-1) else output.append('.')
    output.append(grid[x-1][y]) if validate_cell(x-1, y) else output.append('.')
    output.append(grid[x-1][y+1]) if validate_cell(x-1, y+1) else output.append('.')
    output.append(grid[x][y-1]) if validate_cell(x, y-1) else output.append('.')
    output.append(grid[x][y+1]) if validate_cell(x, y+1) else output.append('.')
    output.append(grid[x+1][y-1]) if validate_cell(x+1, y-1) else output.append('.')
    output.append(grid[x+1][y]) if validate_cell(x+1, y) else output.append('.')
    output.append(grid[x+1][y+1]) if validate_cell(x+1, y+1) else output.append('.')
    return output


def validate_cell(x, y):
    """
    quick validation to see if cell is out of bounds
    """
    return 0 <= x <= X-1 and 0 <= y <= Y-1


def initalizeGrid(x, y):
    """
    initialize an empyt grid with all dead cells "."
    """
    return [['.' for cols in range(y)] for rows in range(x)]


def isGridEmpty():
    pass


def cellState(neighbours):
    """
    report on the state of a cells surroundings.
    can return a number between 0 and 8
    """
    numAlive = 0
    for cell in neighbours:
        if cell == '*':
            numAlive += 1
    return numAlive


def printGrid(grid):
    """
    print out our basic grid to the terminal
    after writing it out will put the cursor back to the top so we can re-write
    (makes it look pretty)
    """
    output = []
    for row in grid:
        for col in row:
            output.append(col)
        output.append('\n')
    sys.stdout.write('\r'+''.join(output))
    sys.stdout.flush()

    for row in grid:
        sys.stdout.write("\033[F") # Cursor up one line



def play(grid):
    """
    run the sumulation
        1. create the new state grid
        2. iterate over our current grid
        3. get the neighbours and the state of the cell
        4. apply the logic (if dead then 3 / if alive then 2 or 3)
        5. return the new state grid
    """
    nextState = initalizeGrid(X, Y)
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            n = neighbours(x, y, grid)
            c = cellState(n)
            #if cell is dead
            if grid[x][y] == '.':
                if c == 3:
                    nextState[x][y] = '*'
                else:
                    nextState[x][y] = '.'
            #if cell is alive
            elif grid[x][y] == '*':
                if c == 3 or c == 2:
                    nextState[x][y] = '*'
                else:
                    nextState[x][y] = '.'
    return nextState


def glider(grid):
    """
    sets up the glider in the grid
    note: does not error check to make sure in bounds
    """
    grid[1][5] = '*'
    grid[2][6] = '*'
    grid[3][4] = '*'
    grid[3][5] = '*'
    grid[3][6] = '*'
    return grid



if __name__ == '__main__':
    #setup basic variables
    X, Y = 20, 20
    iterations = 60

    #init grid and print for the first iteration
    grid = initalizeGrid(X, Y)
    grid = glider(grid)
    printGrid(grid)
    #loop though n iterations calling play and print
    #sleep for a half second to see the animation
    for loop in range(iterations):
        grid = play(grid)
        printGrid(grid)
        time.sleep(0.5)
