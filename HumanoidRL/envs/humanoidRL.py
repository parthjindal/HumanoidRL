from HumanoidRL.envs import Utility as ut
import gym
from gym import spaces
import numpy as np


class HumanoidEnv(gym.Env):
    """Humanoid RL Environment for simulation of a NAO-V40"""

    def __init__(self):
        self.Nao = None
        self.freq = 240
        self.force_motor = 1000
        lows = [-1.14529, -0.379435, -1.53589, -0.0923279, -1.18944,
                -0.397761, -1.14529, -0.79046, -1.53589, -0.0923279,
                -1.1863, -0.768992, -2.08567, -0.314159, -2.08567,
                -1.54462, -2.08567, -1.32645, -2.08567, 0.0349066]
        highs = [0.740718, 0.79046, 0.48398, 2.11255, 0.922581, 0.768992,
                 0.740718, 0.379435, 0.48398, 2.11255, 0.932006, 0.397761,
                 2.08567, 1.32645, 2.08567, -0.0349066, 2.08567, 0.314159,
                 2.08567, 1.54462]
        self.action_space = spaces.Box(low=np.array(lows),
                                       high=np.array(highs))
        lows.extend([-10, -10, -10])
        highs.extend([10, 10, 10])
        obs_low = np.array(lows)
        obs_high = np.array(highs)
        self.observation_space = spaces.Box(low=obs_low, high=obs_high)
        self.Nao = ut.Utility()

    def step(self, action):
        self.Nao.execute_frame(action)
        self.observation = self.Nao.get_observation()
        self.episode_steps += 1
        # reward algo
        reward = 0
        self.episode_over = False if self.episode_steps < self.force_motor else True

        return self.observation, reward, self.episode_over, {}

    def reset(self):
        if self.Nao.nao is None:
            self.Nao.init_bot(self.freq)
        # self.Nao.init_joints()
        self.Nao.reset_bot()
        self.episode_over = False
        self.episode_steps = 0
        return self.Nao.get_observation()

    def render(self, mode='human', close=False):
        pass
