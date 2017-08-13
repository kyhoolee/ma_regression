

import numpy as np
from sklearn import datasets, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR
from read_ma_data import read_ma
import math


def mse_variance(model, ma_x, ma_target):
    # The mean squared error
    print("Logarithm mean squared error: %.2f"
          % math.log(np.mean((model.predict(ma_x) - ma_target) ** 2)))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % model.score(ma_x, ma_target))
    print()


def linear_regression(ma_x, ma_target):
    regr = linear_model.LinearRegression()
    regr.fit(ma_x, ma_target)

    print(regr)
    mse_variance(regr, ma_x, ma_target)


def kernel_ridge(ma_x, ma_target):
    clf = KernelRidge(alpha=1.0)
    #KernelRidge(kernel='rbf', gamma=0.1)
    clf.fit(ma_x, ma_target)

    print(clf)
    mse_variance(clf, ma_x, ma_target)


def svr(ma_x, ma_target):
    clf = SVR(C=1.0, epsilon=0.2)
    clf.fit(ma_x, ma_target)

    print(clf)
    mse_variance(clf, ma_x, ma_target)


def random_forest(ma_x, ma_target):
    clf = RandomForestRegressor(max_depth=8, random_state=0)
    clf.fit(ma_x, ma_target)

    print(clf)
    mse_variance(clf, ma_x, ma_target)


def decision_tree(ma_x, ma_target):
    clf = DecisionTreeRegressor(max_depth=8)
    clf.fit(ma_x, ma_target)

    print(clf)
    mse_variance(clf, ma_x, ma_target)


def ada_boost(ma_x, ma_target):
    clf = AdaBoostRegressor()
    clf.fit(ma_x, ma_target)

    print(clf)
    mse_variance(clf, ma_x, ma_target)


if __name__ == "__main__":
    ma_x, ma_target = read_ma()
    linear_regression(ma_x, ma_target)
    kernel_ridge(ma_x, ma_target)
    random_forest(ma_x, ma_target)
    decision_tree(ma_x, ma_target)
    ada_boost(ma_x, ma_target)