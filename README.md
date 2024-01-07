# A Cost-Sensitive Meta-Learning Strategy for Fair Provider Exposure in Recommendation
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/gpl/gpl.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[Ludovico Boratto](https://www.ludovicoboratto.com/), [Giulia Cerniglia](https://github.com/gcerniglia1), [Mirko Marras](https://www.mirkomarras.com/), [Alessandra Perniciano](https://github.com/alessandraperniciano), [Barbara Pes](https://web.unica.it/unica/page/en/barbara_pes)
<br>University of Cagliari, Italy </br>

## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
    - [Additional files](#additional-files)
- [Contribution](#contribution)
- [License](#license)

## Installation
The code was designed to be used with the [Elliot](https://dl.acm.org/doi/10.1145/3404835.3463245) framework. Because of this, you must download the [repository](https://github.com/sisinflab/elliot) and install all needed packages.
The code is written in Python 3.8 and it does not require additional packages (except the ones for running **Elliot**).


## Getting Started

### Modify the Elliot framework
The modification of the Elliot framework is minimal. In particular, you have to replace the following files:
- *elliot/dataset/samplers/*```custom_sampler.py```
- *elliot/dataset/*```dataset.py```

with their modified homonymous provided in this repository.


In ```BPRMF.py```, you have to replace the following line of code in the ```__init__``` function:
```python
self._sampler = cs.Sampler(self._data.i_train_dict)
```
with the following one:
```python
self._sampler = cs.Sampler(self._data.i_train_dict, self._data.probabilities, self._data.gender)
```

### Additional files
As mentioned in the paper, we used the datasets [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/) and [Coco](https://link.springer.com/chapter/10.1007/978-3-319-77712-2_133). The files are already preprocessed and available in the ```data``` folder. 

Furthermore, we provided the splitting of the datasets which can be found in ```splits``` subfolder. If you desire to use these files, you have to insert inside the folder data in the Elliot framework, the  ```folder coco``` and ```folder movielens_1m```. If you desire to use your own dataset, you have to follow the same instruction provided inside the *elliot/dataset/*```dataset.py``` file.

In addition, we provided the file ```configuration.yml``` that contains the configurations used for our the experiments. For using this file, you have to insert it inside the folder ```config_files``` of the Elliot framework. 

Moreover, to run the experiment, we provided the file ```main.py``` that contains the setup for running the experiments with the datasets and the configuration file provided in this repository.


### The C parameter
To change the C parameter, you have to modify the file *elliot/dataset/*```dataset.py```. In particular, you have to modify ```c = 2``` in the function ``` probabilities_gender(self)``` with the desired value. 

## Contribution


## License
This code is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This software is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for details.

You should have received a copy of the GNU General Public License along with this source code. If not, go the following link: http://www.gnu.org/licenses/.

<More Information>
