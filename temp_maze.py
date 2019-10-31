from random import shuffle, randrange
 
def MakeMaze(w = 5, h = 5):
    vis = [[False] * w + [True] for _ in range(h)] + [[1] * (w + 1)]
    ver = [[1] * w + [4] for _ in range(h)] + [[]]
    hor = [[0] * w + [5] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = True
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = 2
            if yy == y:
                ver[y][max(x, xx)] = 3
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
    
    for (a, b) in zip(hor, ver):
        print(a)
        print(b)

    for (a, b) in zip(hor, ver):
        for j in a:
            if j == 0:
                print('+--', end='')
            elif j == 5:
                print('+', end='')
            elif j == 3:
                print('   ', end='')
            elif j == 2:
                print('+  ', end='')
            elif j == 1:
                print('|  ', end='')
            elif j == 4:
                print('|', end='')

        print()

        for j in b:
            if j == 0:
                print('+--', end='')
            elif j == 5:
                print('+', end='')
            elif j == 3:
                print('   ', end='')
            elif j == 2:
                print('+  ', end='')
            elif j == 1:
                print('|  ', end='')
            elif j == 4:
                print('|', end='')
        print()

    return hor, ver
 
if __name__ == '__main__':
    print(MakeMaze())