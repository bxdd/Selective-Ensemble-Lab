import numpy as np
import graphviz

from sklearn.datasets import load_digits, load_iris, make_multilabel_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree


from selab.ensemble.forest.tree import DecisionTreeClassifier
from selab.ensemble.forest import RandomForestClassifier


X, Y = make_multilabel_classification(n_samples=20480, n_features=64, n_classes=13, n_labels=1)
#dataset = load_iris()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.3)
rfc = RandomForestClassifier(n_estimators=200, criterion="entropy", bootstrap=False, max_features="auto")
rfc = rfc.fit(Xtrain, Ytrain)


print(233)
each_train_score = [accuracy_score(Ytrain, predict_Ytrain) for predict_Ytrain in rfc.predict_estimators(Xtrain)]
each_test_score = [accuracy_score(Ytest, predict_Ytest) for predict_Ytest in rfc.predict_estimators(Xtest)]

print("Decision Tree Train:{}, {}".format(np.mean(each_train_score), np.max(each_train_score)))
print("Decision Tree Test:{}, {}".format(np.mean(each_test_score), np.max(each_test_score)))
print("Random Forest Train:{}".format(rfc.score(Xtrain, Ytrain)))
print("Random Forest Test:{}".format(rfc.score(Xtest, Ytest)))
