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
        self.jointPos = np.zeros((len(self.jointIndex), 1))
        self.jointVel = np.zeros((len(self.jointIndex), 1))
        self.jointF = np.zeros((len(self.jointIndex), 3))
        self.jointT = np.zeros((len(self.jointIndex), 3))

        self.bodyPos = np.zeros((1, 3))
        self.bodyAng = np.zeros((1, 3))
        self.bodyVel = np.zeros((1, 3))
        self.bodyAngVel = np.zeros((1, 3))

        self.nao = None

    def init_bot(self, freq, ep_length):

        p.connect(p.GUI)
        p.setTimeOut(ep_length)
        p.setGravity(0, 0, -9.81)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.loadURDF("plane.urdf")
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)

        startPos = [0, 0, .35]
        self.nao = p.loadURDF(
            "/home/taapas/KRSSG/HumanoidRL/humanoid/nao.urdf",
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

###Delete get_observation once update joints ios updated.
    def get_observation(self):
        self.observation = np.zeros([20, 20])

        for joint, index in self.jointIndex.items():
            l = p.getJointInfo(self.nao, index[0])
            l = list(l)
            a = list(l[13])
            b = list(l[14])
            c = list(l[15])
            l.remove(l[0])
            l.remove(l[0])
            l.remove(l[10])
            l.remove(l[10])
            l.remove(l[10])
            l.remove(l[10])
            for i in range(3):
                l.append(a[i])
            for i in range(3):
                l.append(b[i])
            for i in range(3):
                l.append(c[i])
            print(len(l))
            self.observation[index[1]] = [x for x in l]

    def update_joints(self):
        for joint, index in self.jointIndex.items():
            temp = p.getJointState(self.nao, index[0])
            self.jointPos[index[1], :] = temp[0]
            self.jointVel[index[1], :] = temp[1]
            print("temp", temp[1])
            self.jointF[index[1], :] = temp[2][:3]
            self.jointT[index[1], :] = temp[2][:-3]

        self.bodyPos[:, :], temp = p.getBasePositionAndOrientation(self.nao)
        self.bodyAng[:, :] = p.getEulerFromQuaternion(temp)
        self.bodyVel[:, :], self.bodyAngVel[:, :] = p.getBaseVelocity(self.nao)  

    def kill_bot(self):
        p.disconnect()