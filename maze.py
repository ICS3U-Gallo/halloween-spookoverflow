import random
import math
import bisect
X = 31
Y = 31

# maze = [[False]*X]*Y DO NOT DO THIS
maze = [[False]*X for _ in range(Y)]

V_walls = []
H_walls = []

def random_odd(lower_bound, upper_bound):
    if lower_bound % 2 == 0:
        lower_bound += 1
    return random.randrange(lower_bound, upper_bound+1, 2)

def show_maze():
    pass
    print('#'*(X+2))
    for i in maze:
        print('#', end='')
        for j in i:
            if j == True:
                print('X', end='')
            else:
                print(' ', end='')
        print('#', end='')
        print()
    print('#'*(X+2))

def gen_maze_chamber(lower_bound_x, upper_bound_x, lower_bound_y, upper_bound_y):
    global V_walls, H_walls, maze
    random_split_x = random_odd(lower_bound_x, upper_bound_x)
    random_split_y = 29 # random_odd(lower_bound_y, upper_bound_y)

    for i in range(upper_bound_y - lower_bound_y + 1):
        maze[i + lower_bound_y][random_split_x] = True

    for i in range(upper_bound_x - lower_bound_x + 1):
        maze[random_split_y][i + lower_bound_x] = True
    



    chambers = [
        (lower_bound_x, random_split_x, lower_bound_y, random_split_y),  # upper left corner
        (random_split_x, upper_bound_x, lower_bound_y, random_split_y),  # Upper right corner
        (lower_bound_x, random_split_x, random_split_y, upper_bound_y),  # Lower left corner
        (random_split_x, upper_bound_x, random_split_y, upper_bound_y),  # Lower right corner
    ]

    random_hole_b = random.randint(random_split_y+1, upper_bound_y)
    random_hole_t = random.randint(lower_bound_y, random_split_y-1)
    random_hole_l = random.randint(lower_bound_x, random_split_x-1)
    random_hole_r = random.randint(random_split_x+1, upper_bound_x)
    print(f"Random Hole B: {random_hole_b}")
    print(f"Random Hole T: {random_hole_t}")
    print(f"Random Hole L: {random_hole_l}")
    print(f"Random Hole R: {random_hole_r}")
    maze[random_split_y][random_hole_l] = False
    maze[random_split_y][random_hole_r] = False
    maze[random_hole_t][random_split_x] = False
    maze[random_hole_b][random_split_x] = False

    show_maze()
    for i in chambers:
        if abs(i[0] - i[1]) > 2 and abs(i[2] - i[3]) > 2:
            print(i)
            gen_maze_chamber(*i)


gen_maze_chamber(0, 30, 0, 30)

