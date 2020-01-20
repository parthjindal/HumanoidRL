'''

Humanoid RL Environment for simulation of a NAO-V40
Made according to OpenAI Gym Environments

'''
import Utility as ut
import gym
from gym import spaces
import numpy as np


class HumanoidEnv(gym.Env):
    def __init__(self):
        '''

        Initialising bot parameters, action space and observation space of the bot

        '''
        self.Nao = None
        self.freq = 240
        self.force_motor = 1000
        lows, highs = self.action_lowshighs()
        self.action_space = spaces.Box(low=np.array(lows),
                                       high=np.array(highs))
        high = 10 * np.ones([20, 20])
        low = -high
        self.observation_space = spaces.Box(low=low, high=high)

    def step(self, action):
        '''

        Making the bot moce according to the algorithm and returning observation and reward

    
        '''

        self.Nao.execute_frame(action)
        self.observation = self.Nao.get_observation()
        self.episode_steps += 1
        # reward algo
        reward = 0
        self.episode_over = False

        return self.observation, reward, self.episode_over, {}

    def reset(self):
        '''

        Resetting the params after each episode

        '''    

        self.Nao = ut.Utility()
        self.Nao.init_bot(self.freq, self.force_motor)
        self.Nao.init_joints()
        self.episode_over = False
        self.episode_steps = 0
        return self.Nao.get_observation()

    def render(self, mode='human', close=False):
        pass

    def action_lowshighs(self):
        '''
        
        Getting the action space i.e. min and max possible values to which a joint can move

        '''
        temp = ut.Utility()
        lows, highs = temp.getactionHighsLows()
        return (lows, highs)
