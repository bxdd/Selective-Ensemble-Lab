import numpy as np
import graphviz

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import tree


from selab.ensemble.forest.tree import DecisionTreeClassifier
from selab.ensemble.forest import RandomForestClassifier


def view_tree(clf, dataset, name):
    r = tree.export_text(clf, feature_names=dataset["feature_names"])
    dot_data = tree.export_graphviz(
        clf,
        out_file=None,
        # feature_names=dataset.feature_names,
        # class_names=dataset.target_names,
        filled=True,
        rounded=True,
        special_characters=True,
    )
    graph = graphviz.Source(dot_data)
    graph.render(f"decison_tree_{name}.pdf")


breast = load_digits()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(breast.data, breast.target, test_size=0.2)

rfc = RandomForestClassifier(n_estimators=200, random_state=997, bootstrap=False, max_features="auto")
rfc = rfc.fit(Xtrain, Ytrain)
print("Random Forest Train:{}".format(rfc.estimators_[0].score(Xtrain, Ytrain)))
print("Random Forest Test:{}".format(rfc.estimators_[0].score(Xtest, Ytest)))
view_tree(rfc.estimators_[0], breast, "rf_0")

tfc = DecisionTreeClassifier(random_state=997)
tfc = tfc.fit(Xtrain, Ytrain)
print("Decision Tree Train:{}".format(tfc.score(Xtrain, Ytrain)))
print("Decision Tree Test:{}".format(tfc.score(Xtest, Ytest)))
