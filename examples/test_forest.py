import numpy as np
import graphviz

from sklearn.datasets import load_digits, load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree


from selab.ensemble.forest.tree import DecisionTreeClassifier
from selab.ensemble.forest import RandomForestClassifier


def view_tree(clf, dataset, name):
    dot_data = tree.export_graphviz(
        clf,
        out_file=None,
        feature_names=dataset.feature_names,
        class_names=[str(_target_name) for _target_name in dataset.target_names],
        filled=True,
        rounded=True,
        special_characters=True,
    )
    graph = graphviz.Source(dot_data)
    graph.render(f"pics/{name}")


breast = load_iris()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(breast.data, breast.target, test_size=0.2)

rfc = RandomForestClassifier(n_estimators=1, criterion="entropy", random_state=233, bootstrap=False, max_features="auto")
rfc = rfc.fit(Xtrain, Ytrain)
print("Random Forest Train:{}".format(rfc.estimators_[0].score(Xtrain, Ytrain)))
print("Random Forest Test:{}".format(rfc.estimators_[0].score(Xtest, Ytest)))
view_tree(rfc.estimators_[0], breast, "random_forest_estimator")

tfc = DecisionTreeClassifier(random_state=996, criterion="entropy", max_features="auto")
tfc = tfc.fit(Xtrain, Ytrain)
print("Decision Tree Train:{}".format(tfc.score(Xtrain, Ytrain)))
print("Decision Tree Test:{}".format(tfc.score(Xtest, Ytest)))
view_tree(tfc, breast, "decision_tree")
print(rfc.estimators_[0], tfc)