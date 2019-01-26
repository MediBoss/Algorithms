N = 4 # the size of the maze

def printPath(path):

    for i in range(len(path)):
        for j in range(len(path)):
            print(i,j)

def isBlockSafe(maze,x,y):
    ''' Helper function to check if a block is safe to go'''
    # make sure it coordinates are inbound
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] != 0: return True
    return False

def solveMaze(maze):
    initial_path = [[0 for j in range(4)] for i in range(4)]
    if solveMazeUtil(maze,0,0, initial_path) == False:
        print("No Way out of the maze")
        return False

    printPath(initial_path)
    return True


def solveMazeUtil(maze, rat_x, rat_y, path):
    '''
    Return a boolean on wheter or not there's possible path to reach the destiation
    @params:
        - maze: the matrix with blocked and unblocked blocks in the maze
        - rat_x: the x position of the rat
        - rat_y: the y position of the rat
        - path: The current path traveled by the rat
    '''

    # Base Case : check if rat is on destination
    if rat_x == N-1 and rat_y == N-1:
        path[rat_x][rat_y] = 1
        return True
    # Recursive case

    # check if cur position is within bounds and safe to go to
    if isBlockSafe(maze, rat_x, rat_y) ==  True:
        # add current location to path
        path[rat_x][rat_y] = 1
        # Go to x direction if that block is safe, else go to y
        if solveMazeUtil(maze, rat_x+1, rat_y, path) == True: return True
        if solveMazeUtil(maze, rat_x, rat_y+1, path) ==  True: return True

    # if no path is found, return false and backtrack
    path[rat_x][rat_y] = 0
    return False




def main():

    maze = [
        [1,0,0,0],
        [1,1,1,1],
        [0,1,0,0],
        [1,1,1,1]
    ]

    solveMaze(maze)


if __name__ == "__main__":
    main()
