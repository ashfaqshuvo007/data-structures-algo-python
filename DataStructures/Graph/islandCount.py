
def islandCount(grid):
    #visited
    visited = []
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (explore(grid,row,col,visited) ) == True:
                count += 1
    #Not complete work to be done here
    return count


def explore(grid,row,col,visited):

    # out of bound error fix
    rowInbound =  0 <= row and row < len(grid)
    colInbound = 0 <= row and row < len(grid)

    if(not rowInbound and  not colInbound): return False
    #No need to traverse water nodes
    if grid[row][col] == 'w': return False

    # Avoid Cycle
    pos = str(row) + "," + str(col)
    if pos in visited: return False
    visited.append(pos)

    # Four Recursion calls for four direction
    explore(grid,row - 1,col,visited)
    explore(grid,row + 1,col,visited)
    explore(grid,row,col - 1,visited)
    explore(grid,row,col + 1,visited)

    return True





if __name__ == '__main__':
    grid = [
        ['w','l','w','w','w'],
        ['w','l','w','w','w'],
        ['w','w','w','l','w'],
        ['w','w','l','l','w'],
        ['l','w','w','l','l'],
        ['l','l','l','l','l'],
    ]

    print("The island count : ", islandCount(grid))