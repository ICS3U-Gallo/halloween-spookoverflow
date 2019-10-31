# main.py

import random
import arcade
import os
from temp_maze import MakeMaze
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Halloween Maze - SpookOverflow"

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """ Initialize """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.

        # Show the mouse cursor
        self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)
            
    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("jaco-o-lantern.png", scale=0.1)
        self.player_sprite.center_x = 850
        self.player_sprite.center_y = 150
        self.player_list.append(self.player_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        """ Set up the game and initialize the variables. """
        arcade.set_background_color(arcade.color.WHITE)
        self._screen = 0
        self.maze_1 = [
            [True , False , True , True , True , True , True, True , True , True],
            [True , False , True , False , False , False , False, False , False , True],
            [True , False , True , False , True , False , True, True , False , True],
            [True , False , False , False , True , True , True, False , False , True],
            [True , False , True , False , False , False , True, False , False , True],
            [True , True , True , True , True , True , True, True , True , True],
        ]
        self.maze_2 = [
            [True , False , True , True , True , True , True, True , True , True],
            [True , False , True , False , True , False , False, False , False , True],
            [True , False , True , False , True , False , False, True , False , True],
            [True , False , False , False , True , False , False, True , False , True],
            [True , False , True , False , False , False , False, True , False , True],
            [True , True , True , True , True , True , True, True , True , True],
        ]
        self.maze_3 = [
            [True , False, True , True , True , True , True , True , True , True],
            [True , False, False, False, False, False, True , False, False, True],
            [True , True , True , True , False, False, True , False, False, True],
            [True , False, False, True , True , False, False, False, False, True],
            [True , False, False, False, False, False, True , True , False, True],
            [True , True , True , True , True , True , True , True , True , True],
        ]
        self.ShowMaze(self.maze_1)
        self.do_jumpscare = None
        self.jumpscare = arcade.sound.load_sound('harmless_sound_file2.mp3')
        self.background_audio = arcade.sound.load_sound('Splashing_Around2.m4a')
        arcade.sound.play_sound(self.background_audio)
        self.play_button = arcade.load_texture("./assets/play_button.png")
        self.jumpscare_img = arcade.load_texture('./innocent_picture.jpg')
        self.take_pic = None


    def ShowMaze(self, maze_grid):
        for idx_y, i in enumerate(maze_grid):
            for idx_x, j in enumerate(i):
                if j:
                    wall = arcade.Sprite("black.png", scale=100)
                    wall.center_x = idx_x * 100 + 50
                    wall.center_y = SCREEN_HEIGHT - idx_y * 100 - 50
                    self.wall_list.append(wall)
                    #arcade.draw_rectangle_filled(idx_x * 100 + 50, SCREEN_HEIGHT - idx_y * 100 - 50, 100, 100, arcade.color.BLACK)


    def TakePic(self):
        if self.take_pic is None:
            self.take_pic = True
            pass
            """            arcade.pause(0.5)
                        _, frame = self.capture.read()
                        cv2.imshow('frame',frame)"""

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        if self._screen == 0:
            pass
              # Load play button here
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 400, 300, self.play_button)

            
        elif self._screen == 1:
              # Load disclaimer here
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 400, 300, self.play_button)
            arcade.draw_text('Disclaimer', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200 , arcade.color.RED, font_size = 100, anchor_x = "center")
            arcade.draw_text('Please prepare yourself', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200, arcade.color.WHITE, font_size = 50, anchor_x = "center" )

        elif 2 <= self._screen <= 4 :
            arcade.set_background_color(arcade.color.WHITE)
            self.wall_list.draw()
            self.player_list.draw()
        elif self._screen == 5:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.jumpscare_img)
            self.TakePic()
        else:
              raise ValueError(f"self.screen should not be {self.screen}!")
        
    def on_mouse_motion(self, x, y, dx, dy):
        if self._screen == 4 and self.do_jumpscare is None:
            self.do_jumpscare = True
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        if self._screen == 2:
            self.physics_engine.update()
            if 125 <= self.player_sprite.center_x <= 175 and 525 <= self.player_sprite.center_y <= 575:
                self.player_sprite.center_x = 850
                self.player_sprite.center_y = 150
                del self.wall_list
                self.wall_list = arcade.SpriteList()
                self.ShowMaze(self.maze_2)
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


                self._screen += 1

        elif self._screen == 3:

            self.physics_engine.update()
            if 125 <= self.player_sprite.center_x <= 175 and 525 <= self.player_sprite.center_y <= 575:
                self.player_sprite.center_x = 850
                self.player_sprite.center_y = 150
                del self.wall_list
                self.wall_list = arcade.SpriteList()
                self.ShowMaze(self.maze_3)
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

                self._screen += 1

        if self.do_jumpscare:
            self.do_jumpscare = False
            # arcade.sound.stop_sound(self.background_audio)
            arcade.sound.play_sound(self.jumpscare)
            self._screen = 5
            print('X')



    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self._screen == 0 or self._screen == 1:
            if 372 <= x <= 638 and 265 <= y <= 338:
                self._screen += 1
        
      


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()