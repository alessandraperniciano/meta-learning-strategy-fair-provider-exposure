"""
Module description:

"""

__version__ = '0.3.1'
__author__ = 'Vito Walter Anelli, Claudio Pomo'
__email__ = 'vitowalter.anelli@poliba.it, claudio.pomo@poliba.it'

import numpy as np
import random


class Sampler:
    def __init__(self, indexed_ratings, probabilities, gender):
        random.seed(42)
        np.random.seed(42)
        self._indexed_ratings = indexed_ratings
        self._users = list(self._indexed_ratings.keys())
        self._nusers = len(self._users)
        self._items = list({k for a in self._indexed_ratings.values() for k in a.keys()})
        self._nitems = len(self._items)
        self.c = probabilities['c']
        probabilities.pop('c')
        self.p1 = int(100 // (self.c + 1))
        self.p2 = 100 - self.p1
        self.probabilities = list(probabilities.values())
        self.gender = gender
        self._ui_dict = {u: list(set(indexed_ratings[u])) for u in indexed_ratings}
        self._lui_dict = {u: len(v) for u, v in self._ui_dict.items()}

    def step(self, events: int, batch_size: int):
        r_int = np.random.randint

        n_users = self._nusers
        n_items = self._nitems
        ui_dict = self._ui_dict
        lui_dict = self._lui_dict

        def sample():

            modified_negative = False
            modified_positive = True
            u = r_int(n_users)
            ui = ui_dict[u]
            lui = lui_dict[u]
            probabilities_positive = []

            if lui == n_items:
                sample()

            if modified_positive:
                # female represented as number 2 or letter 'f'
                f = 1 if type(list(self.gender[0].values())[0]) is np.dtype(np.int64) else 'f'
                for item in ui:
                    p = self.p2 if list(self.gender[item].values())[0] == f else self.p1
                    probabilities_positive.append(p)
                i = random.choices(ui, probabilities_positive)[0]
                y = ui[r_int(lui)]
            else:
                i = ui[r_int(lui)]


            if modified_negative:
                x = r_int(n_items)
                j = random.choices(list(self.gender), weights=self.probabilities)[0]
            else:
                j = r_int(n_items)

            while j in ui:
                if modified_negative:
                    j = random.choices(list(self.gender), weights=self.probabilities)[0]
                else:
                    j = r_int(n_items)

            if modified_negative:
                while x in ui:
                    x = r_int(n_items)


            return u, i, j

        for batch_start in range(0, events, batch_size):
            bui, bii, bij = map(np.array, zip(*[sample() for _ in range(batch_start, min(batch_start + batch_size, events))]))
            yield bui[:, None], bii[:, None], bij[:, None]