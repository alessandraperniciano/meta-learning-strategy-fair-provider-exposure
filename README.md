# A Cost-Sensitive Meta-Learning Strategy for Fair Provider Exposure in Recommendation
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/gpl/gpl.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[Ludovico Boratto](https://www.ludovicoboratto.com/), [Giulia Cerniglia](https://github.com/gcerniglia1), [Mirko Marras](https://www.mirkomarras.com/), [Alessandra Perniciano](https://github.com/alessandraperniciano), [Barbara Pes](https://web.unica.it/unica/page/en/barbara_pes)
<br>University of Cagliari, Italy </br>

## Table of Contents
- [Elliot Base Preparation](#elliot-base-preparation)
- [Getting Started](#getting-started)
    - [Data Preparation](#data-preparation)
    - [Parameters Setting](#parameters-setting)
    - [Experiments Replication](#experiments-replication)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

## Elliot Base Preparation
The code was designed to be used with the [Elliot](https://dl.acm.org/doi/10.1145/3404835.3463245) framework. Because of this, you must download the [repository](https://github.com/sisinflab/elliot) and install all needed packages.
The code is written in Python 3.8 and it does not require additional packages (except for the ones required to run **Elliot**).


## Getting Started

### Elliot Base Customization
The modification of the Elliot framework is minimal. In particular, you have to replace the following files:
- *elliot/dataset/samplers/*```custom_sampler.py```
- *elliot/dataset/*```dataset.py```

with their modified homonymous provided in this repository.


In *elliot/recommender/latent_factor_models/BPRMF/*```BPRMF.py```, you have to replace the code at line 91 in the ```__init__``` function:
```python
self._sampler = cs.Sampler(self._data.i_train_dict)
```
with the following one:
```python
self._sampler = cs.Sampler(self._data.i_train_dict, self._data.probabilities, self._data.gender)
```

### Data Preparation
As mentioned in the paper, we used the datasets [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/) and [Coco](https://link.springer.com/chapter/10.1007/978-3-319-77712-2_133). 
Please contact us by e-mail, inserting all the co-authors in copy, to obtain a zip file with the already pre-processed data and splits, to be added in the corresponding subfolders within the Elliot framework.  If you desire to use your own dataset, you have to follow the same instruction provided inside the *elliot/dataset/*```dataset.py``` file.

### Parameters Setting
In addition, we provided the file ```configuration.yml``` that contains the configurations used for our experiments. For using this file, you have to insert it inside the folder ```config_files``` of the Elliot framework. 

To change the C parameter, you have to modify the file *elliot/dataset/*```dataset.py```. In particular, you have to modify the line 282 (```c = 2```) in the function ``` probabilities_gender(self)``` with the desired value. 

### Experiments Replication
Moreover, to run the experiment, we provided the file ```main.py``` that contains the setup for running the experiments with the datasets and the configuration file provided in this repository.

## Contributing
This code aims to facilitate reproduction of our results, and further research in this direction. We have done our best to document, refactor, and test the code before publication. If you find any bugs or would like to contribute new models, training protocols, etc, please let us know. Please feel free to file issues and pull requests on the repo and we will address them as we can.

## Citation
If you find this code useful in your work, please cite our papers:

```
Boratto, L., Cerniglia, G., Marras, M., Perniciano, A., & Pes, B. (2024).
A Cost-Sensitive Meta-Learning Strategy for Fair Provider Exposure in Recommendation.
In: Proc. of the 46th European Conference on IR Research, ECIR. ECIR 2024. Springer.

Marras, M., Boratto, L., Ramos, G., & Fenu, G. (2022).
Regulating Group Exposure for Item Providers in Recommendation.
In: Proc. of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR 2022. ACM.
```


## License
This code is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This software is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for details.

You should have received a copy of the GNU General Public License along with this source code. If not, go the following link: http://www.gnu.org/licenses/.

<More Information>
