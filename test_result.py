from spinup.utils.test_policy import load_policy, run_policy
import HumanoidRL
import gym
import argparse

def main() :
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        type=str,
        default="",
    )
    args = parser.parse_args()
    _, get_action = load_policy(args.file)
    env = gym.make('HumanoidRL-v0')
    run_policy(env, get_action)

main()