import pyxel, math
from datetime import datetime

class MovingObject:
    FRONT_SPRITE = None
    LEFT_SPRITE = None
    RIGHT_SPRITE = None
    BACK_SPRITE = None
    FRONT_WALKING_SPRITES = None
    BACK_WALKING_SPRITES = None
    LEFT_WALKING_SPRITES = None
    RIGHT_WALKING_SPRITERS = None
    
    def __init__(self, x, y, game, vely=0, velx=0, speed=1, movement_timer=.2):
        self.x = x
        self.y = y
        self.game = game
        self.height = self.game.DEFAULT_HEIGHT
        self.width = self.game.DEFAULT_WIDTH
        self.vely = vely
        self.velx = velx
        self.speed = speed
        self.last_dir = self.game.DIR_DOWN
        self.last_move_time_stamp = datetime.now().timestamp()
        self.movement_timer = movement_timer
        self.movement_index = 0

    def _get_sprite_tuple(self):
        if self.last_dir == self.game.DIR_UP:
            return self.BACK_SPRITE if not self.is_moving else self.BACK_WALKING_SPRITES[self.movement_index]
        if self.last_dir == self.game.DIR_DOWN:
            return self.FRONT_SPRITE if not self.is_moving else self.FRONT_WALKING_SPRITES[self.movement_index]
        if self.last_dir == self.game.DIR_LEFT:
            return self.LEFT_SPRITE if not self.is_moving else self.LEFT_WALKING_SPRITES[self.movement_index]
        if self.last_dir == self.game.DIR_RIGHT:
            return self.RIGHT_SPRITE if not self.is_moving else self.RIGHT_WALKING_SPRITES[self.movement_index]
        return self.FRONT_SPRITE

    def _get_sprite(self):
        # overwrite in child class
        return self._get_sprite_tuple() + (self.width, self.height)

    def get_sprite(self):
        return self._get_sprite()

    def set_dir(self, d):
        self.last_dir = d

    def draw(self):
        pyxel.blt(self.x, self.y, *self.get_sprite())

    def set_vel(self, degrees):
        radians = math.radians(degrees)
        self.velx = self.speed * math.sin(radians)
        self.vely = self.speed * math.cos(radians)

    def stop(self):
        self.vely = 0
        self.velx = 0

    def _handle_movement_sprite_change(self):
        now = datetime.now().timestamp()
        if now - self.last_move_time_stamp > self.movement_timer:
            self.movement_index = 0 if self.movement_index else 1
            self.last_move_time_stamp = now

    def _move(self):
        self.x += self.velx
        self.y += self.vely
        self._handle_movement_sprite_change()

    def move(self):
        # overwrite in child class
        self._move()

    @property
    def is_moving(self):
        return self.velx or self.vely
        