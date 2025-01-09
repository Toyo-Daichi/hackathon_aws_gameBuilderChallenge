import pyxel
import random
from typing import Optional

from ..context.db import Db
from ..context.gamestate import GameState
from ..model.ui.player import Player
from ..model.ui.enemy import Enemy
from ..model.ui.bullet import Bullet
from ..model.ui.blast import Blast
from ..service.character import Character
from ..service.score import Score

from ..util.state import *
from ..util.logger import Logger
from src.context import gamestate
logging = Logger(__name__, "INFO")

PLAYER_INITIAL_X = 142
PLAYER_INITIAL_Y = 200

class GameInfo:
    mode: str
    emeny_index: int

    def __init__(self, mode: str, enemy_sum: int) -> None:
        self.mode = mode
        self.enemy_index = random.randint(0, enemy_sum - 1)

    def get_enemy_index(self):
        return self.enemy_index

    def get_initial_enemy_num(self):
        initial_enemy_num = 0
        if self.mode == 'Normal':
            initial_enemy_num = 5
        elif self.mode == 'DoS':
            initial_enemy_num = 15
        elif self.mode == 'DDoS':
            initial_enemy_num = 30

        return initial_enemy_num

    def get_frame_count(self):
        frame_count = 0
        if self.mode == 'Normal':
            frame_count = 100
        elif self.mode == 'DoS':
            frame_count = 30
        elif self.mode == 'DDoS':
            frame_count = 15

        return frame_count

class Play:
    gamestate: GameState
    database: Db
    score: int
    player: Player
    enemies: list[Enemy]
    bullets: list[Bullet]
    blasts: list[Blast]
    #
    gameinfo: GameInfo

    def __init__(self):
        self.gamestate = GameState()
        self.database = Db()
        self.score = 0
        self.bullets = []
        self.blasts = []

        character = Character(self.database)
        player_names = ['Basic1', 'Mario', 'Luigi']
        player_name = random.choice(player_names)
        logging.info(f"Character of Player is {player_name}")

        _player = character.find_character_by_name(random.choice(player_names))
        self.player = Player(
            PLAYER_INITIAL_X,
            PLAYER_INITIAL_Y,
            _player.x_coord,
            _player.y_coord,
            self.bullets,
            self.blasts
        )
        _enemies = character.find_character_by_role('Enemy')
        self.enemies = []

        self.gameinfo = GameInfo(self.gamestate.get_mode(), len(_enemies))

        if self.gamestate.get_mode() == 'Normal' or self.gamestate.get_mode() == 'DoS':
            for _ in range(self.gameinfo.get_initial_enemy_num()):
                self.enemies.append(Enemy(
                    random.randint(0, pyxel.width),
                    random.randint(0, 100),
                    _enemies[self.gameinfo.get_enemy_index()].x_coord,
                    _enemies[self.gameinfo.get_enemy_index()].y_coord
                ))

    def update(self):
        self.update_play_scene()
        update_state(self.player)
        update_states(self.enemies)
        update_states(self.bullets)
        update_states(self.blasts)
        cleanup_states(self.enemies)
        cleanup_states(self.bullets)
        cleanup_states(self.blasts)

        if pyxel.btnp(pyxel.KEY_Q):
            logging.info("Game Quit")
            score = Score(self.database)
            score.write_score(1, self.gamestate.get_mode(), self.score)
            self.gamestate.set_state('RESULT')
            self.gamestate.set_score(self.score)

    def update_play_scene(self):
        if self.gamestate.get_mode() == 'Normal' or self.gamestate.get_mode() == 'DoS':
            if pyxel.frame_count %  self.gameinfo.get_frame_count() == 0:
                self.enemies.append(Enemy(
                    random.randint(0, pyxel.width - 16),
                    0,
                    self.enemies[0].x_coord,
                    self.enemies[0].y_coord
                ))

        for enemy in self.enemies:
            for bullet in self.bullets:
                if (
                    enemy.x + enemy.width > bullet.x
                    and bullet.x + bullet.radius > enemy.x
                    and enemy.y + enemy.height > bullet.y
                    and bullet.y + bullet.radius > enemy.y
                ):
                    enemy.is_alive = False
                    bullet.is_alive = False
                    self.blasts.append(Blast(enemy.x + enemy.width/2, enemy.y + enemy.height/2))
                    update_states(self.blasts)
                    self.score += 10

    def draw(self):
        pyxel.text(0, 0, f"{self.gamestate.get_mode()}", 1)
        pyxel.text(0, 8, f"{self.score}", 1)
        draw_state(self.player)
        draw_states(self.enemies)
        draw_states(self.blasts)
