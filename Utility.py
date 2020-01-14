import pybullet as p
import pybullet_data
import numpy as np


class Utility:

    def __init_(self, freq):
        self.jointIndex = {
            'LHipYawPitch': (13, 0),
            'LHipRoll': (14, 1),
            'LHipPitch': (15, 2),
            'LKneePitch': (16, 3),
            'LAnklePitch': (17, 4),
            'LAnkleRoll': (18, 5),
            'RHipYawPitch': (26, 6),
            'RHipRoll': (27, 7),
            'RHipPitch': (28, 8),
            'RKneePitch': (29, 9),
            'RAnklePitch': (30, 10),
            'RAnkleRoll': (31, 11),
            'LShoulderPitch': (39, 12),
            'LShoulderRoll': (40, 13),
            'LElbowYaw': (41, 14),
            'LElbowRoll': (42, 15),
            'RShoulderPitch': (56, 16),
            'RShoulderRoll': (57, 17),
            'RElbowYaw': (58, 18),
            'RElbowRoll': (59, 19)
        }
        self.jointPos = np.zeros((len(self.jointIndex), 3))
        self.jointVel = np.zeros((len(self.jointIndex), 3))
        self.jointF = np.zeros((len(self.jointIndex), 3))
        self.jointT = np.zeros((len(self.jointIndex), 3))
        self.body = np.zeros((2, 3))
        self.nao = None

    def init_bot(self, freq, ep_length):

        p.connect(p.GUI)
        p.setTimeOut(ep_length)
        p.setGravity(0, 0, -10)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.loadURDF("plane.urdf")
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)

        startPos = [0, 0, .35]
        self.nao = p.loadURDF(
            "humanoid/nao.urdf",
            startPos,
            flags=p.URDF_USE_SELF_COLLISION_EXCLUDE_PARENT)
        
        self.timeStep = 1./freq

    # def make_observation(self) :

    def execute_frame(self, action):
        try:
            for joint,index in self.jointIndex.items():
                pos = (np.pi / 2.) * action[index]
                p.setJointMotorControl2(
                    self.nao, joint, p.POSITION_CONTROL, targetPosition=pos)
            p.stepSimulation()
            time.sleep(self.timeStep)
        except Exception as e:
            return False
        return True

    def kill_bot(self):
        p.disconnect()



