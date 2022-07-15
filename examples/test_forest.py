import numpy as np
import graphviz

from sklearn.datasets import load_digits, load_iris, make_multilabel_classification
from sklearn.model_selection import train_test_split
from sklearn import tree


from selab.ensemble.forest.tree import DecisionTreeClassifier
from selab.ensemble.forest import RandomForestClassifier


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
    graph.render(f"pics/{name}")


X, Y = make_multilabel_classification(n_samples=20480, n_features=64, n_classes=13, n_labels=1)
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.3)


result = []
for i in range(100):
    scores = []
    for j in range(1):
        rfc = RandomForestClassifier(n_estimators=100, criterion="entropy", bootstrap=False, max_samples=0.8, max_features="auto")
        rfc = rfc.fit(Xtrain, Ytrain)
        print("Round {}: Random Forest Train:{}".format(i, rfc.estimators_[0].score(Xtrain, Ytrain)))
        print("Round {}: Random Forest Test:{}".format(i, rfc.estimators_[0].score(Xtest, Ytest)))
        print("Round {}: Random Forest Test:{}".format(i, rfc.score(Xtest, Ytest)))
        scores.append(rfc.score(Xtest, Ytest))
    result.append(np.mean(scores))

print(result)
import matplotlib.pyplot as plt

plt.plot(range(len(result)), result)
plt.savefig("ret.jpg")

# view_tree(rfc.estimators_[0], breast, "random_forest_estimator")


# rfc = RandomForestClassifier(n_estimators=200, criterion="entropy", bootstrap=True, max_features="auto")
# rfc = rfc.fit(Xtrain, Ytrain)
# print("Random Forest Train:{}".format(rfc.estimators_[0].score(Xtrain, Ytrain)))
# print("Random Forest Test:{}".format(rfc.score(Xtest, Ytest)))
# view_tree(rfc.estimators_[0], breast, "random_forest_estimator")
# 
# 
# tfc = DecisionTreeClassifier(criterion="entropy", max_features="auto")
# tfc = tfc.fit(Xtrain, Ytrain)
# print("Decision Tree Train:{}".format(tfc.score(Xtrain, Ytrain)))
# print("Decision Tree Test:{}".format(tfc.score(Xtest, Ytest)))
# view_tree(tfc, breast, "decision_tree")
# print(rfc.estimators_[0], tfc)
