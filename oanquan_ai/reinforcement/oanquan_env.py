"""OpenAI Gym environment for O An Quan game."""

import gymnasium as gym
import numpy as np
from gymnasium import spaces

from oanquan_ai.oanquan import (
    BOARD_SIZE,
    COMPUTER_FIELDS,
    Direction,
    Move,
    OAnQuan,
    Player,
)


class OAnQuanEnv(gym.Env):
    """Custom OpenAI Gym environment definition for O An Quan game."""

    def __init__(self, game: OAnQuan | None = None):
        self.game = game or OAnQuan.start_game()
        self.action_space = spaces.MultiDiscrete([len(COMPUTER_FIELDS), 2])

        self.observation_space = spaces.Dict(
            {
                "board": spaces.Box(
                    low=0, high=70, shape=(BOARD_SIZE,), dtype=np.int32
                ),
                "score": spaces.Box(
                    low=0, high=70, shape=(2,), dtype=np.int32
                ),
            }
        )

    def reset(self, seed=None, options=None):
        self.game = OAnQuan.start_game()
        return {
            "board": np.array(self.game.board, dtype=np.int32),
            "score": np.array(
                [
                    self.game.score[Player.PLAYER.name],
                    self.game.score[Player.COMPUTER.name],
                ],
                dtype=np.int32,
            ),
        }, {}

    def step(self, action):
        pos, direction = action
        direction = (
            Direction.COUNTER_CLOCKWISE
            if direction == 0
            else Direction.CLOCKWISE
        )
        move = Move(pos=pos, direction=direction)
        self.game.make_move(move)

        observation = {
            "board": np.array(self.game.board, dtype=np.int32),
            "score": np.array(
                [
                    self.game.score[Player.PLAYER.name],
                    self.game.score[Player.COMPUTER.name],
                ],
                dtype=np.int32,
            ),
        }

        done = self.game.check_end()

        reward = (
            self.game.score[Player.COMPUTER.name]
            - self.game.score[Player.PLAYER.name]
        )

        return observation, reward, done, False, {}

    def render(self):
        print(self.game)
