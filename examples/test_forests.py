import numpy as np

from sklearn.datasets import load_wine

from selab.forest.tree import DecisionTreeClassifier
from selab.forest import RandomForestClassifier
from selab.forest.binner import Binner

wine = load_wine()
from sklearn.model_selection import train_test_split


binner_ = Binner(
    n_bins=255,
    bin_subsample=200000,
    bin_type="percentile",
)

# Bin the training data

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
Xtrain = binner_.bin_data(Xtrain, is_training_data=True)
Xtest = binner_.bin_data(Xtest, is_training_data=False)
rfc = RandomForestClassifier(n_estimators=200, random_state=0)
# tfc = DecisionTreeClassifier()
rfc = rfc.fit(Xtrain, Ytrain)
score_r = rfc.score(Xtest, Ytest)
print("Random Forest:{}".format(score_r))
