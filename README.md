[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

####NAO V40 pybullets training environment

# Description

This is NAO-V40 training environment based OpenAI Gym standards. Pybullets is used as the simulationg environment.

#Repository structure

``` shell
├── baselines
│   ├── nao.py
│   └── test_walk.py
├── envs
│   ├── humaniodRL.py
│   ├── test_script.py
│   ├── Utility.py
│   └── walk_positions.pckl
├── humanoid
│   ├── LICENSE.txt
│   ├── meshes
│   └── nao.urdf
├── Pipfile
└── README.md
```
- `baselines` contains the reference items.
- `envs` contains `humanoidRL` script which it the standard Gym environment. `Utility` class contains the basic functions for communicating with the simulator.
- `humanoid` contains the meshes and basic physics configrations for NAO V40. 

### Using the environment

- Run `humanoidRL.py` script with Python3.

#Testing
- `test_script.py` is the testing script for utlity functions and the environment seperately.
``` shell
 use python test_script --env=True to test environment
 use python test_script --util=True to test utilities
```