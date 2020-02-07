import pybullet as p
import pybullet_data
import time

# in order to run this, you need to pip/conda install pybullet

# There are 2 ways of running PyBullet - with a debug visualizer (slower but easy to debug) and headless.
# The option "p.GUI" means with debug visualizer
p.connect(p.GUI)

# you need this to find the floor, "plane.urdf"
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

startPos = [0, 0, .35]

# turn off rendering for a second to speed up loading
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)

# load teh nao model at this position

#flags can also use p.URDF_USE_SELF_COLLISION_EXCLUDE_ALL_PARENTS
#don't use URDFpyt_USE_SELF_COLLISION, since some connected body parts overlap
nao = p.loadURDF(
    "nao.urdf",
    startPos,
    flags=p.URDF_USE_SELF_COLLISION_EXCLUDE_PARENT)


# for all joints set the way of controlling them to position control which means you tell it to be at an angle and it'll go there via an internal PID controller. There are also other ways of controlling each joint
for i in range(p.getNumJoints(nao)):
    info = p.getJointInfo(nao, i)
    print(info [0],info[1])
    p.setJointMotorControl2(
        nao, i, p.POSITION_CONTROL, targetPosition=0, force=1000)

# x = input()
# get info from all joints (if you want to actuate more joints than only his head and left leg, then you need to go over this list and find the numbers of the other joints, like 59 right elbow
# for i in range(p.getNumJoints(nao)):
a = p.getJointInfo(nao, 13)
print(a)

# turn rendering back on
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)

# could've gotten this from numpy.pi too
pi = 3.1415

shoulderPitch = pi / 2
shoulderRoll = 0.1

# this makes the arms hang down and not forward (default pos in teh URDF file)
p.setJointMotorControl2(
    nao, 56, p.POSITION_CONTROL, targetPosition=shoulderPitch, force=1000)
p.setJointMotorControl2(
    nao, 39, p.POSITION_CONTROL, targetPosition=shoulderPitch, force=1000)
#p.setJointMotorControl2(
#    nao, 57, p.POSITION_CONTROL, targetPosition=-shoulderRoll, force=1000)
#p.setJointMotorControl2(
#    nao, 40, p.POSITION_CONTROL, targetPosition=shoulderRoll, force=1000)

# this can be anywhere in the file
p.setGravity(0, 0, -10)

# set the simulator frequency to 240Hz. In practice that's a lot. I'd go higher than 50Hz (stability) and probably around 100Hz (good accuracy-speed tradeoff)
timeStep = 1. / 240.
p.setTimeStep(timeStep)


# add motors that you wanna actuate to this list. You find them by looking at the terminal output from line 38-39
motors = [1, 2, 13, 14, 15, 16, 17, 18]
debugParams = []
# motors = [3, 4, 6, 8, 10, 14]

import math

# make it so that  for each one of the motors we add a slider to we can test each motor
for i in range(len(motors)):
    motor = p.addUserDebugParameter("motor{}".format(i + 1), -1, 1, 0)
    debugParams.append(motor)

# in this loop, we query each user debug slider and set the motor to that value. In practice, these motor signals would come from your policy
while (1):
    for j in range(len(motors)):
        pos = (math.pi / 2) * p.readUserDebugParameter(debugParams[j])
        p.setJointMotorControl2(
            nao, motors[j], p.POSITION_CONTROL, targetPosition=pos)
    p.stepSimulation()

    time.sleep(timeStep)
