from ..base import PairWiseMetric
from ...ensemble.forest.tree import BaseDecisionTree

class TreeEditMetric(PairWiseMetric):
    @staticmethod
    def cal_pairwise_distance(ind1:BaseDecisionTree, ind2:BaseDecisionTree):
        pass