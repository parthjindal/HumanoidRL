import Utility as ut
import gym
from gym import spaces
import numpy as np

class HumanoidEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    def __init__(self):

        self.jointLimits = {
            'LHipYawPitch': (-10, 10),
            'LHipRoll': (-10, 10),
            'LHipPitch': (-10, 10),
            'LKneePitch': (-10, 10),
            'LAnklePitch': (-10, 10),
            'LAnkleRoll': (-10, 10),
            'RHipYawPitch': (-10, 10),
            'RHipRoll': (-10, 10),
            'RHipPitch': (-10, 10),
            'RKneePitch': (-10, 10),
            'RAnklePitch': (-10, 10),
            'RAnkleRoll': (-10, 10),
            'LShoulderPitch': (-10, 10),
            'LShoulderRoll': (-10, 10),
            'LElbowYaw': (-10, 10),
            'LElbowRoll': (-10, 10),
            'RShoulderPitch': (-10, 10),
            'RShoulderRoll': (-10, 10),
            'RElbowYaw': (-10, 10),
            'RElbowRoll': (-10, 10)
        }
        jointLimit = list(self.jointLimits.values())
        self.Nao  = None
        self.freq = 240 
        self.force_motor = 1000
        self.action_space = spaces.Box(
            low=np.array([limit[0] for limit in jointLimit]),
            high=np.array([limit[1] for limit in jointLimit]))
        high = 10 * np.ones([20, 20])
        low = -high
        self.observation_space = spaces.Box(low=low, high=high)    


    def step(self, action):
        self.Nao.execute_frame(action)    
        self.observation = self.Nao.get_observation()
        self.episode_steps += 1
        # reward algo
        reward = 0
        self.episode_over = False

        return self.observation, reward, self.episode_over, {}

    def reset(self):
        self.Nao = ut.Utility()
        self.Nao.init_bot(self.freq, self.force_motor)
        self.Nao.init_joints()
        self.episode_over = False
        self.episode_steps = 0
        return self.Nao.get_observation()

    def render(self, mode='human', close=False):
        pass 
