import pyxel
from datetime import datetime

from lib.object import MovingObject

class Player(MovingObject):
    FRONT_SPRITE = (0, 0, 0)
    BACK_SPRITE = (0, 0, 8)
    LEFT_SPRITE = (0, 16, 8)
    RIGHT_SPRITE = (0, 16, 0)
    FRONT_WALKING_SPRITES = (
        (0, 8, 0),
        (0, 8, 8),
    )
    BACK_WALKING_SPRITES = (
        (0, 0, 16),
        (0, 8, 16),
    )
    LEFT_WALKING_SPRITES = (
        (0, 32, 0),
        (0, 32, 8),
    )
    RIGHT_WALKING_SPRITES = (
        (0, 24, 0),
        (0, 24, 8),
    )
    ATTACK_UP_SPRITE = (0, 32, 16)
    ATTACK_DOWN_SPRITE = (0, 24, 16)
    ATTACK_LEFT_SPRITE = (0, 16, 24)
    ATTACK_RIGHT_SPRITE = (0, 16, 16)

    WEAPON_SPRITE = (0, 24, 24)

    def __init__(self, *args):
        super().__init__(*args)
        self.height = self.game.PLAYER_HEIGHT
        self.width = self.game.PLAYER_WIDTH
        self.is_attacking = False
        self.last_attack_time = None
        self.attack_timer = .2

    def attack(self):
        if not self.is_attacking:
            self.last_attack_time = datetime.now().timestamp()
            self.is_attacking = True

    def _get_attack_sprite(self):
        if self.last_dir == self.game.DIR_UP:
            return self.ATTACK_UP_SPRITE + (self.width, self.height)
        if self.last_dir == self.game.DIR_DOWN:
            return self.ATTACK_DOWN_SPRITE + (self.width, self.height)
        if self.last_dir == self.game.DIR_LEFT:
            return self.ATTACK_LEFT_SPRITE + (self.width, self.height)
        if self.last_dir == self.game.DIR_RIGHT:
            return self.ATTACK_RIGHT_SPRITE + (self.width, self.height)
        return self.FRONT_SPRITE + (self.width, self.height)

    def get_sprite(self):
        if self.is_attacking:
            return self._get_attack_sprite()
        else:
            return self._get_sprite()

    def move(self):
        if not self.is_attacking:
            self._move()

    def draw_weapon(self):
        if self.is_attacking:
            if self.last_dir == self.game.DIR_LEFT:
                pyxel.blt(*((self.x-self.width, self.y,) + self.WEAPON_SPRITE  + (-self.width, self.height)))
            elif self.last_dir == self.game.DIR_RIGHT:
                pyxel.blt(*((self.x+self.width, self.y,) + self.WEAPON_SPRITE  + (self.width, self.height)))
            elif self.last_dir == self.game.DIR_UP:
                pyxel.blt(
                    *((self.x, self.y-self.height,) + self.WEAPON_SPRITE  + (-self.width, self.height)),
                    rotate=-90
                )
            elif self.last_dir == self.game.DIR_DOWN:
                pyxel.blt(
                    *((self.x, self.y+self.height,) + self.WEAPON_SPRITE  + (-self.width, self.height)),
                    rotate=90
                )

    def update(self):
        # handle various timed statuses
        now = datetime.now().timestamp()

        if self.is_attacking and now - self.last_attack_time > self.attack_timer:
            self.is_attacking = False
            self.last_attack_time = None

        