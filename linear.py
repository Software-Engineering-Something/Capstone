import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import glob, os

while True:
    option = input("Option: ")
    # Option 1: Linear Regression
    if option == '1':
        # Read multiple file
        data = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "*.txt"))))
        # Read one file
        # data = pd.read_csv('jpm_a.us.txt')

        X = data.iloc[:, 1].values.reshape(-1, 1)
        Y = data.iloc[:, 4].values.reshape(-1, 1)

        # Remove Outliners
        meanY = np.mean(Y, axis=0)
        sdY = np.std(Y, axis=0)
        outlinerY = meanY - 2 * sdY
        meanX = np.mean(X, axis=0)
        sdX = np.std(X, axis=0)
        outlinerX = meanX - 2 * sdX
        i = 0
        while i < len(Y):
            if Y[i] > outlinerY or Y[i] < outlinerY or X[i] > outlinerX or X[i] < outlinerX:
                Y = np.delete(Y, i).reshape(-1, 1)
                X = np.delete(X, i).reshape(-1, 1)
            i = i+1

        # Train and Predict
        lr = LinearRegression()
        lr.fit(X, Y)
        Y_pred = lr.predict(X)
        MSE = mean_squared_error(Y, Y_pred)
        SCORE = lr.score(Y, Y_pred)
        # Calculations
        print("MSE", MSE)
        print("R^2 Score", SCORE)
        # Graph
        # plt.scatter(X, Y)
        # plt.plot(X, Y_pred, color='red')
        # plt.show()


