import humaniodRL as env
import Utility as ut
import pickle
import argparse


path = "walk_positions.pckl"


def read_from_pickle(path):
    poses = []
    with open(path, 'rb') as file:
        while True:
            try:
                poses.append(pickle.load(file))
            except EOFError:
                break
    return poses


def test_env():
    poses = read_from_pickle(path)[0]
    Bot = env.HumanoidEnv()
    Bot.reset()
    for configs in poses:
        action = [configs[6], configs[1], configs[10], configs[2], configs[18],
                  configs[12], configs[8], configs[4], configs[5], configs[14],
                  configs[0], configs[11], configs[19], configs[13],
                  configs[9], configs[15], configs[3], configs[7],
                  configs[16], configs[17]]
    obs, rew, done, w = Bot.step(action)


def test_utility():
    poses = read_from_pickle(path)[0]

    Bot = ut.Utility()
    Bot.init_bot(240, 1000)
    Bot.get_observation()
    print("Observation:\n", Bot.observation)
    for configs in poses:
        action = [configs[6], configs[1], configs[10], configs[2], configs[18],
                  configs[12], configs[8], configs[4], configs[5], configs[14],
                  configs[0], configs[11], configs[19], configs[13],
                  configs[9], configs[15], configs[3], configs[7],
                  configs[16], configs[17]]
    Bot.execute_frame(action)
    Bot.update_joints()
    Bot.get_observation()
    print(Bot.observation)
    # print("bodyPos\n", Bot.bodyPos, "\n")
    # print("bodyAng\n", Bot.bodyAng, "\n")
    # print("bodyVel\n", Bot.bodyVel, "\n")
    # print("bodyAngVel\n", Bot.bodyAngVel, "\n")

    # print("jointPos\n", Bot.jointPos, "\n")
    # print("jointVel\n", Bot.jointVel, "\n")
    # print("jointF\n", Bot.jointF, "\n")
    # print("jointT\n", Bot.jointT, "\n")


def main():
    """
    use python test_script --env=True to test environment
    use python test_script --util=True to test utilities
    """
    parser = argparse.ArgumentParser(description="Test framework")
    parser.add_argument(
        "--env",
        type=bool,
        default=False,
        help="set True to test the Gym Environment"
    )
    parser.add_argument(
        "--util",
        type=bool,
        default=False,
        help="set True to test the Utility Class"
    )
    args = parser.parse_args()
    if (args.env and args.util):
        print("Cannot test both envionment and "
              "Utility at once")
    if args.env:
        test_env()
    elif args.util:
        test_utility()
    else:
        print("No flag given try -h for help")


main()
