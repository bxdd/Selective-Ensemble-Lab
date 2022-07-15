import numpy as np

from typing import Set, List, Union
from itertools import combinations
class BaseMetric:
    PAIRWISE = 0
    NON_PAIRWISE = 1
    def __init__(self, inds:Union[Set, List], type=PAIRWISE):
        self.inds = inds
        self.type = type

    @staticmethod
    def cal_pairwise_distance(ind1, ind2):
        pass

    @staticmethod
    def cal_set_distance(inds:Union[Set, List]):
        pass

    def cal_mean_distance(self):
        if self.type == self.PAIRWISE:
            return np.mean([self.cal_pairwise_distance(self.inds[i], self.inds[j]) for i, j in combinations(len(self.inds), 2)])
        elif self.type == self.NON_PAIRWISE:
            return self.cal_set_distance(self.inds)

class PairWiseMetric(BaseMetric):
    def __init__(self, inds:Union[Set, List]):
        super(PairWiseMetric, self).__init__(inds, BaseMetric.PAIRWISE)

class SetMetric(BaseMetric):
    def __init__(self, inds:Union[Set, List]):
        super(PairWiseMetric, self).__init__(inds, BaseMetric.NON_PAIRWISE)
