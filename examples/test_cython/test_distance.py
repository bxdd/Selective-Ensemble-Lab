import graphviz
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree

from selab.metrics.tree_edit._libs.distance import DisTree
from selab.ensemble.forest.tree import DecisionTreeClassifier


dataset = load_iris()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(dataset.data, dataset.target, test_size=0.3)
dtc = DecisionTreeClassifier(random_state=233)
dtc = dtc.fit(Xtrain, Ytrain)

def view_tree(name, clf, dataset=None):
    dot_data = tree.export_graphviz(
        clf,
        out_file=None,
        feature_names=[str(_target_name) for _target_name in dataset.feature_names] if dataset else None,
        class_names=[str(_target_name) for _target_name in dataset.target_names] if dataset else None,
        filled=True,
        rounded=True,
        special_characters=True,
    )
    graph = graphviz.Source(dot_data)
    graph.render(f"{name}")


view_tree("233", dtc, dataset)
#print(dtc.tree_.feature, dtc.tree_.children_left)
#print(dtc.tree_.node_count, dtc.tree_.capacity)

distree = DisTree(decision_tree=dtc.tree_)
