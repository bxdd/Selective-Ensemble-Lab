import numpy as np

from sklearn.datasets import load_digits

from selab.ensemble.forest.tree import DecisionTreeClassifier
from selab.ensemble.forest import RandomForestClassifier

breast = load_digits()

from sklearn.model_selection import train_test_split

Xtrain, Xtest, Ytrain, Ytest = train_test_split(breast.data, breast.target, test_size=0.2)

rfc = RandomForestClassifier(n_estimators=200, random_state=997)
tfc = DecisionTreeClassifier()
rfc = rfc.fit(Xtrain, Ytrain)
score_r1 = rfc.score(Xtest, Ytest)

tfc = tfc.fit(Xtrain, Ytrain)
score_r2 = tfc.score(Xtest, Ytest)
print("Random Forest:{}".format(score_r1))
print("Decision Tree:{}".format(score_r2))
