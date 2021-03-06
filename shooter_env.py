import numpy as np
from gym import Env
from gym.spaces import Discrete, Box

from constants import *
from game_scene import GameScene


class StateMode(Enum):
    SCREENSHOT_MODE = 0
    VECTOR_MODE_1 = 1
    VECTOR_MODE_2 = 2


class ShooterEnv(Env):
    """
    The custom environment class for our shooter game.
    """

    def __init__(self, state_mode: StateMode = StateMode.SCREENSHOT_MODE):
        self.game_scene = GameScene()
        self.action_space = Discrete(self.game_scene.ActionCount())
        self.state_mode = state_mode
        # self.observation_space = self.game_scene.ScreenShot()
        self.observation_shape = (WIDTH, HEIGHT, 3)
        self.observation_space = Box(low=np.zeros(self.observation_shape),
                                     high=np.full(self.observation_shape, 255),
                                     dtype=np.uint8)
        if self.state_mode == StateMode.SCREENSHOT_MODE:
            self.state = self.game_scene.ScreenShot()
        else:
            self.state = self.game_scene.StateVector(self.state_mode == StateMode.VECTOR_MODE_2)

        self.reward = 0
        self.done = self.game_scene.Done()
        self.info = self.game_scene.AdditionalState()

        # * add player_action_num
        self.player_action_num = 0

    def step(self, action_num: int):
        # More return values
        self.done = self.game_scene.Play(action_num)
        self.reward = self.game_scene.Reward()
        if self.state_mode == StateMode.SCREENSHOT_MODE:
            self.state = self.game_scene.ScreenShot()
        else:
            self.state = self.game_scene.StateVector(self.state_mode == StateMode.VECTOR_MODE_2)
        self.info = self.game_scene.AdditionalState()

        # * add player_action_num
        self.player_action_num = self.game_scene.player_action_num

        return self.state, self.reward, self.done, self.info

    def render(self, mode="human"):
        pass

    def reset(self):
        self.game_scene.Reset()
        if self.state_mode == StateMode.SCREENSHOT_MODE:
            self.state = self.game_scene.ScreenShot()
        else:
            self.state = self.game_scene.StateVector(self.state_mode == StateMode.VECTOR_MODE_2)
        self.done = self.game_scene.Done()
        self.info = self.game_scene.AdditionalState()
        return self.state

    def player_action_num(self):
        return self.player_action_num


if __name__ == '__main__':
    env = ShooterEnv(StateMode.VECTOR_MODE_2)

    action_list = [
        0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7
    ]

    score = 0

    while True:
        state, reward, done, info = env.step(-1)
        score += reward
        print("State vec: " + str(state))
        if done:
            score = 0
            env.reset()
        # print(env.info)
