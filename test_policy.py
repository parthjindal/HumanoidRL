from spinup.utils.test_policy import load_pytorch_policy, load_tf_policy, run_policy
from spinup.utils.plot import make_plots
import HumanoidRL
import gym
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        type=str,
        default="",
    )
    parser.add_argument(
        "--plot",
        type=bool,
        default=False,
    )
    parser.add_argument(
        "--run",
        type=str,
        default=None,
        choices={"pytorch", "tf"}
    )
    args = parser.parse_args()
    if args.plot:
        make_plots([args.file], xaxis="TotalEnvInteracts", values="Performance")
    if args.run:
        get_action = load_pytorch_policy(args.file, itr='') if args.run == "pytorch" else load_tf_policy(args.file, itr='')
        env = gym.make('HumanoidRL-v0')
        run_policy(env, get_action)