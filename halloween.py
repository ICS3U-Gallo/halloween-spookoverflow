import turtle
import pygame
import math
from time import *
from random import randrange

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("./image/block.gif")
        self.shape("./image/block.gif")
        self.color("white")
        self.penup()
        self.speed(3)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("./image/zombie.gif")
        self.shape("./image/zombie.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("./image/treasure.gif")
        self.shape("./image/treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            elif character == "P":
                player.goto(screen_x, screen_y)
            elif character == "T":
                treasures.append(Treasure(screen_x, screen_y))


def start_time():
    treasure.destroy()
    treasures.remove(treasure)
    wn.update()

    pygame.mixer.music.load("./Music/gameover.wav")
    pygame.mixer.music.play(4)

    start_timer = time()

    #struct = localtime(start_timer)

    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(10, 300)
    turtle.color("yellow")
    turtle.write(" It's a fake gold!!! In to laggy mode!!!", align="left", font=(10))
    turtle.goto(-50, 300)
    turtle.write("\nRespawn in 5 seconds", align="right", font=(0.0000001))
    turtle.goto(2000, 2000)

    i = 5
    while i > -1:
        i = i - 1
        x = turtle.Turtle()
        x.pencolor = ("blue")
        x.goto(0, 0)
        x.write(i + 1, font = (0.0000001))
        x.penup()
        x.goto(2000, 2000)
        sleep(1)
        wn.update()
        x.clear()
    #end_timer = time()
    pygame.mixer.music.load("./Music/halloween_music.wav")
    pygame.mixer.music.play(-1)
    turtle.clear()


def placing_gold(current_level):
    output = []
    gold_count = 0

    for i in range(0, len(current_level)):
        current_row = ""

        for j in range(0, len(current_level[i])):
            if current_level[i][j] == "X":
                current_row = current_row + "X"
            else:
                if randrange(10) < 1:
                    current_row = current_row + "T"
                else:
                    current_row = current_row + " "

        output.append(current_row)

    return output


def count_gold(current_level):
    count = 0

    for i in range(0, len(current_level)):
        for j in range(0, len(current_level[i])):
            if current_level[i][j] == "T":
                count = count + 1

    return count


''' Below is setting up game's configuration. '''
pygame.mixer.init()
pygame.mixer.music.load("./Music/halloween_music.wav")
pygame.mixer.music.play(-1)

wn_menu = turtle.Screen()
wn_menu.title("Halloween Maze 2019 - Game Menu")

wn = turtle.Screen()
wn.title("Halloween Maze 2019")
wn.bgcolor("black")
wn.setup(700, 700)
wn.tracer(0)
wn.bgpic("./image/giphy.gif")

level = []
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X XXXXXXX           XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X           XXXXXX  XXXXX",
    "X       XX  XXX XXX    XX",
    "XX XXXXXXX         XX  XX",
    "XX XXX  XX  XXXXXX    XXX",
    "XX      XX    XXXX  XXXXX",
    "XXXXXX  XX    XXXXP XXXXX",
    "XX      XXXXXXXXXXXXXXXXX",
    "X  XXXXXXXXXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX    XXX     X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    YXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXX  XXXXXXX      XXXXX",
    "X                   XXXXX",
    "XXXXXXXXXXX    XXXXXXXXXX",
    "X      XXXX    XXXXXXXXXX",
    "X XXXX XXXX    XXXXXXXXXX",
    "X XX               XXXXXX",
    "X XXXXXXXXXXXXXXXXXXXXXXX",
    "X                      XX",
    "XXXXXXXXXXXXX   XXXXXXXXX",
    "XXXXXXXXXXXXX   XXXXXXXXX",
    "XXXXX              XXXXXX",
    "XXXXXX  XXXXX  XXXXXXXXXX",
    "XXXXXX                  X",
    "XXXXXXXXXXXX   XXXXXXXX X",
    "XX     XXXXX   XXXXXXXX X",
    "XXXXX  XXXXX   XXXX  XX X",
    "XXXXX  XX            XXXX",
    "XXXXX  XXXXXXXXXXXX  XXXX",
    "XXX          XXXXX   XXXX",
    "XXXXXXX   XXXXXXX  XXXXXX",
    "X         XXXXXXX  XXXXXX",
    "XXXXXXX   XXXXXXX  XXXXXX",
    "XXX                  XXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXX  XXXXXXX      XXXXX",
    "X                   XXXXX",
    "XXXXXXXXXXX    XXXXXXXXXX",
    "X      XXXX    XXXX    XX",
    "X XXXX XXXX    XXXX XX XX",
    "X                   XX XX",
    "X   XX  XXXXXXXXXXXXXX XX",
    "XX  XX                 XX",
    "XX  XXXXXXXXX   XXXX  XXX",
    "XX  XXXXXXXXX   XXXX  XXX",
    "XX  X              X  XXX",
    "XX  XXXXXXX    XXXXX  XXX",
    "XX  XX                  X",
    "XX  XXXXXXXX   XXX  XX  X",
    "XX     XXXXX   XXX  XX  X",
    "XX XX  XXXXX   XXX   X  X",
    "XX XX  XX            XXXX",
    "XX XX  XXXXXXXXXXXX  XXXX",
    "XXX          XXXXX   XXXX",
    "XXXXXXX   XXXXXXX  XXXXXX",
    "XXXXXX             XXXXXX",
    "XXXXXXX   XXXXXXX  XXXXXX",
    "XXX                  XXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

current_level = None
gold_left = 0

if randrange(10) in [0, 1, 2, 3]:
    current_level = placing_gold(level_1)
    gold_left = count_gold(current_level)
    wn.title("Halloween Maze 2019 - Level 1")
elif randrange(10) in [4, 5, 6, 7]:
    current_level = placing_gold(level_2)
    gold_left = count_gold(current_level)
    wn.title("Halloween Maze 2019 - Level 2")
else:
    current_level = placing_gold(level_3)
    gold_left = count_gold(current_level)
    wn.title("Halloween Maze 2019 - Level 3")

level.append(current_level)

pen = Pen()
player = Player()

treasures = []
walls = []

setup_maze(level[0])

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
wn.tracer(0)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            gold_left = gold_left - 1
            print(gold_left)
            if player.gold == 100:
                start_time()
            else:
                turtle.clear()
                turtle.goto(-50, 300)
                turtle.write("Player Gold:{}".format(player.gold), align="right", font=(0.0000001))
                turtle.goto(2000, 2000)
                treasure.destroy()
                # treasures.remove(Treasure)
                wn.update()

        wn.update()
