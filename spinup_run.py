from spinup.utils.run_utils import ExperimentGrid
from spinup import ppo_pytorch
import gym
import torch


def run_experiment(args):
    def env_fn():
        import HumanoidRL
        return gym.make(args.env_name)

    eg = ExperimentGrid(name=args.exp_name)
    eg.add('env_fn', env_fn)
    eg.add('seed', [10*i for i in range(args.num_runs)])
    eg.add('epochs', 100000)
    eg.add('steps_per_epoch', 5000)
    eg.add('save_freq', 20)
    eg.add('max_ep_len', 200)
    eg.add('ac_kwargs:activation', torch.nn.Tanh, '')
    eg.run(ppo_pytorch, data_dir=args.data_dir, num_cpu=args.cpu)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--cpu", type=int, default=1)
    parser.add_argument('--num_runs', type=int, default=5)
    parser.add_argument('--env_name', type=str, default="HumanoidRL-v0")
    parser.add_argument('--exp_name', type=str, default='ddpg-custom')
    parser.add_argument('--data_dir', type=str, default='.')
    args = parser.parse_args()

    run_experiment(args)
