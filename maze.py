from random import shuffle, randrange

def MakeMaze(w, h, ProgressCallback):
    visited = [[False] * w + [True] for _ in range(h)] + [[True] * (w + 1)]
    print(visited)
    horizontal = set()
    vertical = set()
    def walk(x, y):
        visited[y][x] = True
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)              # randomize neighbours
        for (neighbour_x, neighbour_y) in d:
            if visited[neighbour_y][neighbour_x]: # no action if visited
                continue
            if neighbour_x == x:
                vertical.add((x, max(y, neighbour_y)))
            elif neighbour_y == y:
                horizontal.add((max(x, neighbour_x), y))
            ProgressCallback(horizontal, vertical)
            walk(neighbour_x, neighbour_y)


    walk(randrange(w), randrange(h))
    return horizontal, vertical

if __name__ == "__main__":
    print("You should only see this text if you're debugging.")
    print(MakeMaze(4, 4, print))