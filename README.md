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
├── results
├── setup.py
├── spinup_run.py
└── test_policy.py


```
- `baselines` contains the reference items.
- `envs` contains `humanoidRL` script which it the standard Gym environment. `Utility` class contains the basic functions for communicating with the simulator.
- `humanoid` contains the meshes and basic physics configrations for NAO V40. 
- `results` default directory for results.

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

- Run the following command
``` shell 
python spinup_run.py --exp_name <exp_name> --cpu <num_cpus> --data_dir <directory to save results> --epochs <epochs> --steps_per_epoch <steps> --max_ep_len  <max len> --save_freq <save freq> 
``` 

You need `spinningupai` installed for that.


### Loading models

- Run `python test_result.py --plot True/False --run pytorch/tf --file <path_to_directory>` to load and plot and/or run the saved model.