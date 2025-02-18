import pyxel

from lib.player import Player

class Game:
    PLAYER_HEIGHT = 8
    PLAYER_WIDTH = 8
    DEFAULT_HEIGHT = 8
    DEFAULT_WIDTH = 8
    DIR_UP = 180
    DIR_DOWN = 0
    DIR_LEFT = 270
    DIR_RIGHT = 90
    TILE_WIDTH = 8
    TILE_HEIGHT = 8
    SCREEN_WIDTH = 128
    SCREEN_HEIGHT = 88
    
    def __init__(self, x, y):
        pyxel.init(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        pyxel.load("PYXEL_RESOURCE_FILE.pyxres")
        self.player = Player(
            x, y, self,
        )
        self.angle = 0
        pyxel.run(self.update, self.draw)
    
    @property
    def up(self):
        return pyxel.btn(pyxel.KEY_UP)

    @property
    def down(self):
        return pyxel.btn(pyxel.KEY_DOWN)

    @property
    def left(self):
        return pyxel.btn(pyxel.KEY_LEFT)

    @property
    def right(self):
        return pyxel.btn(pyxel.KEY_RIGHT)

    def handle_player_input(self):
        if not self.player.is_attacking:
            if self.up and self.right:
                self.player.set_vel(135)
            elif self.up and self.left:
                self.player.set_vel(225)
            elif self.down and self.left:
                self.player.set_vel(315)
            elif self.down and self.right:
                self.player.set_vel(45)
            elif self.up:
                self.player.set_vel(self.DIR_UP)
                self.player.set_dir(self.DIR_UP)
            elif self.down:
                self.player.set_vel(self.DIR_DOWN)
                self.player.set_dir(self.DIR_DOWN)
            elif self.right:
                self.player.set_vel(self.DIR_RIGHT)
                self.player.set_dir(self.DIR_RIGHT)
            elif self.left:
                self.player.set_vel(self.DIR_LEFT)
                self.player.set_dir(self.DIR_LEFT)
            else:
                self.player.stop()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.player.attack()

    def update(self):
        self.handle_player_input()
        self.player.move()
        self.player.update()

    def draw_map(self):
        pyxel.bltm(0,0,0,0,0,self.SCREEN_WIDTH,self.SCREEN_HEIGHT)

    def draw(self):
        pyxel.cls(0)
        self.draw_map()
        self.player.draw()
        self.player.draw_weapon()

Game(50,50)