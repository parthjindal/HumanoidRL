from spinup.utils.run_utils import ExperimentGrid
from spinup import ppo
import gym
import tensorflow as tf

def run_experiment(args):
    def env_fn():
        import HumanoidRL
        return gym.make(args.env_name)

    eg = ExperimentGrid(name=args.exp_name)
    eg.add('env_fn', env_fn)
    eg.add('seed', [10*i for i in range(args.num_runs)])
    eg.add('epochs', 500)
    eg.add('steps_per_epoch', 10000)
    eg.add('save_freq', 20)
    eg.add('max_ep_len', 200)
    eg.add('ac_kwargs:activation', tf.tanh, '')
    eg.run(ppo)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--cpu", type=int, default=1)
    parser.add_argument('--num_runs', type=int, default=5)
    parser.add_argument('--env_name', type=str, default="HumanoidRL-v0")
    parser.add_argument('--exp_name', type=str, default='ddpg-custom')
    args = parser.parse_args()

    run_experiment(args)