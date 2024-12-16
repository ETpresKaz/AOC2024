







with open('Day_6.txt') as f:
    data = f.read()









def m(data):
    grid = [list(i) for i in data.split('\n')]
    x = len(grid)
    y = len(grid[0])
    print(x, y)







    player = None
    for i in range(x):
        for j in range(y):
            if grid[i][j] == '^':
                player = (i, j)
                print(i, j)
                break


        if player:
            break

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
    current_dirc = 0  

    def move():
        nonlocal player
        nonlocal current_dirc
        i, j = player
        dirc = directions[current_dirc]
        new_i = i + dirc[0]
        new_j = j + dirc[1]





        if 0 <= new_i < x and 0 <= new_j < y:
            if grid[new_i][new_j] == '.' or grid[new_i][new_j] == 'X':
                grid[i][j] = 'X'
                grid[new_i][new_j] = '^'
                player = (new_i, new_j)
                return True  
            
            



            else:
                current_dirc = (current_dirc + 1) % 4  
                return True  
        return False  

    steps = 100000
    for r in range(steps):
        if not move():  
            break  

    return grid


new_grid = m(data)
print(new_grid)


def count_X(grid):
    count = 0
    for row in grid:
        count += row.count('X')
    return count

print(count_X(new_grid) + 1)  
print(data)  




def grid_to_string(grid):
    return '\n'.join([''.join(row) for row in grid])



print(grid_to_string(new_grid))