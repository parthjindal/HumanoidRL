import pybullet as p
import pybullet_data
import numpy as np
import time
import pickle


class Utility:

    def __init__(self):

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
        self.bodyIndex = 0

        self.jointPos = np.zeros((len(self.jointIndex), 3))
        self.jointVel = np.zeros((len(self.jointIndex), 3))
        self.jointF = np.zeros((len(self.jointIndex), 3))
        self.jointT = np.zeros((len(self.jointIndex), 3))

        self.bodyPos = np.zeros((1, 3))
        self.bodyVel = np.zeros((1, 3))
        self.bodyF = np.zeros((1, 3))
        self.bodyT = np.zeros((1, 3))

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

        self.init_joints()

        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)

        self.timeStep = 1./freq

    def init_joints(self):
        for joint, index in self.jointIndex.items():
            p.setJointMotorControl2(
                self.nao, index[0], p.POSITION_CONTROL, targetPosition=0, force=1000)
            p.enableJointForceTorqueSensor(self.nao, index[0], enableSensor=1)

        shoulderPitch = np.pi / 2.
        shoulderRoll = 0.1

        p.setJointMotorControl2(
            self.nao, 56, p.POSITION_CONTROL, targetPosition=shoulderPitch, force=1000)
        p.setJointMotorControl2(
            self.nao, 39, p.POSITION_CONTROL, targetPosition=shoulderPitch, force=1000)
        p.setJointMotorControl2(
            self.nao, 57, p.POSITION_CONTROL, targetPosition=-shoulderRoll, force=1000)
        p.setJointMotorControl2(
            self.nao, 40, p.POSITION_CONTROL, targetPosition=shoulderRoll, force=1000)

    def execute_frame(self, action):
        try:
            for joint, index in self.jointIndex.items():
                pos = (np.pi / 2.) * action[index[1]]
                p.setJointMotorControl2(
                    self.nao, index[0], p.POSITION_CONTROL, targetPosition=pos)
            p.stepSimulation()
            time.sleep(self.timeStep)
        except Exception as e:
            return False
        return True

    def update_joints(self):
        for joint, index in self.jointIndex.items():
            temp = p.getJointState(index[0])
            self.jointPos[index[1], :] = temp[0]
            self.jointVel[index[1], :] = temp[1]
            self.jointF[index[1], :] = temp[2][:3]
            self.jointT[index[1], :] = temp[2][:-3]

        temp = p.getJointState(self.bodyIndex)

        self.bodyPos[index[1], :] = temp[0]
        self.bodyVel[index[1], :] = temp[1]
        self.bodyF[index[1], :] = temp[2][:3]
        self.bodyT[index[1], :] = temp[2][:-3]

    def kill_bot(self):
        p.disconnect()


# temp = Utility()
# temp.init_bot(50, 1000)
# x = input()


# def read_from_pickle(path):
#     poses = []
#     with open(path, 'rb') as file:
#         while True:
#             try:
#                 poses.append(pickle.load(file))
#             except EOFError:
#                 break

#     return poses


# path = "walk_positions.pckl"

# poses = read_from_pickle(path)[0]

# for configs in poses:

#     action = [configs[6], configs[1], configs[10], configs[2], configs[18], configs[12], configs[8], configs[4], configs[5], configs[14],
#               configs[0], configs[11], configs[19], configs[13], configs[9], configs[15], configs[3], configs[7], configs[16], configs[17]]

#     temp.execute_frame(action)
