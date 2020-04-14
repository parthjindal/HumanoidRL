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
    eg.add('seed', [i for i in range(args.num_runs)])
    eg.add('epochs', args.epochs)
    eg.add('steps_per_epoch', args.steps_per_epoch)
    eg.add('save_freq', args.save_freq)
    eg.add('max_ep_len', args.max_ep_len)
    eg.add('ac_kwargs:activation', torch.nn.Tanh, '')
    eg.run(ppo_pytorch, data_dir=args.data_dir, num_cpu=args.cpu)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--cpu", type=int, default=1)
    parser.add_argument('--num_runs', type=int, default=5)
    parser.add_argument('--env_name', type=str, default="HumanoidRL-v0")
    parser.add_argument('--exp_name', type=str, default='ddpg-custom')
    parser.add_argument('--data_dir', type=str, default='results')
    parser.add_argument('--epochs', type=int, default=100000)
    parser.add_argument('--steps_per_epoch', type=int, default=10000)
    parser.add_argument('--max_ep_len', type=int, default=200)
    parser.add_argument('--save_freq', type=int, default=20)
    args = parser.parse_args()

    run_experiment(args)
