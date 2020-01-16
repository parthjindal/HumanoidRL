import humaniodRL as env
import Utility
import pickle

def read_from_pickle(path):
    poses = []
    with open(path, 'rb') as file:
        while True:
            try:
                poses.append(pickle.load(file))
            except EOFError:
                break
    return poses

path = "walk_positions.pckl"
poses = read_from_pickle(path)[0]


a = env.HumanoidEnv()
a.reset()   

for configs in poses:
    action = [configs[6], configs[1], configs[10], configs[2], configs[18], configs[12], configs[8], configs[4], configs[5], configs[14],
              configs[0], configs[11], configs[19], configs[13], configs[9], configs[15], configs[3], configs[7], configs[16], configs[17]]

    x, y, z, w = a.step(action)



# temp = Utility()
# temp.init_bot(240, 1000)
# temp.get_observation()
# print(temp.observation)

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
#     temp.update_joints()
#     print("bodyPos\n", temp.bodyPos, "\n")
#     print("bodyAng\n", temp.bodyAng, "\n")
#     print("bodyVel\n", temp.bodyVel, "\n")
#     print("bodyAngVel\n", temp.bodyAngVel, "\n")

#     print("jointPos\n", temp.jointPos, "\n")
#     print("jointVel\n", temp.jointVel, "\n")
#     print("jointF\n", temp.jointF, "\n")
#     print("jointT\n", temp.jointT, "\n")
