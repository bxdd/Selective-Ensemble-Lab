import numpy as np

from sklearn.datasets import load_wine

from selab.seforest.tree.tree import DecisionTreeClassifier
from selab.seforest.forest import RandomForestClassifier
from selab.seforest._binner import Binner

wine = load_wine()
from sklearn.model_selection import train_test_split


binner_ = Binner(
    n_bins=255,
    bin_subsample=200000,
    bin_type="percentile",
)


def _bin_data(binner, X, is_training_data=True):
    """
    Bin data X. If X is training data, the bin mapper is fitted first."""
    if is_training_data:
        X_binned = binner.fit_transform(X)
    else:
        X_binned = binner.transform(X)
        X_binned = np.ascontiguousarray(X_binned)
    return X_binned


# Bin the training data

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
Xtrain = _bin_data(binner_, Xtrain, is_training_data=True)
Xtest = _bin_data(binner_, Xtest, is_training_data=False)
rfc = RandomForestClassifier(n_estimators=200, random_state=0)
tfc = DecisionTreeClassifier()
rfc = rfc.fit(Xtrain, Ytrain)
score_r = rfc.score(Xtest, Ytest)
print("Random Forest:{}".format(score_r))
