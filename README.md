[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

# NAO-V40 pybullets training environment

### Description

This is NAO-V40 training environment based OpenAI Gym standards. Pybullets is used as the simulationg environment.

### Repository structure

``` shell
├── baselines
│   ├── nao.py
│   └── test_walk.py
├── HumanoidRL
│   ├── envs
│   │   ├── humanoidRL.py
│   │   ├── __init__.py
│   │   ├── test_script.py
│   │   ├── Utility.py
│   │   └── walk_positions.pckl
│   ├── humanoid
│   │   ├── LICENSE.txt
│   │   ├── meshes
│   │   └── nao.urdf
│   └── __init__.py
├── README.md
├── setup.py
├── spinup_run.py
└── test_policy.py


```
- `baselines` contains the reference items.
- `envs` contains `humanoidRL` script which it the standard Gym environment. `Utility` class contains the basic functions for communicating with the simulator.
- `humanoid` contains the meshes and basic physics configrations for NAO V40. 

### Installation of Humanoid Environment

- Ensure that you are using Python3.

``` shell
git clone https://github.com/taapasX28/HumanoidRL
cd HumanoidRL/
pip install -e .
```

### Testing

- `test_script.py` is the testing script for utlity functions and the environment seperately.
- Use `python test_script --env=True` to test environment.
- Use `python test_script --util=True` to test utilities.

### Running training

- Run `spinup_run.py`. You need `spinningupai` installed for that.


### Loading models

- Run `python test_result.py --file <path_to_directory>` to load and run the saved model.
- BUG: Change the feed_dict input from `x[None,:]` to `x[None,:][0].T` in `spinup.utils`