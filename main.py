import dask.dataframe as dd
import pandas
import math
import random


def main():
    """dask.dataframe is a dataframe that stores files in a dataframe(a two-dimensional data structure), this reads a
    csv file and parses into data. From there we can use query like calls to search for specific data at O(N) time,
    I'm still new to dataframes, so doing these two search queries may somehow be done in line"""

    df = pandas.read_csv("aadr.us.csv")
    df = df.drop(None,0,None,'Date',None, False, 'raise')
    df = df.drop(None,0,None,'Open',None, False, 'raise')
    df = df.drop(None, 0, None, 'High', None, False, 'raise')
    df = df.drop(None, 0, None, 'Low', None, False, 'raise')
    df = df.drop(None, 0, None, 'OpenInt', None, False, 'raise')
    print(df)
    """from numpy.random import permutation
    random_indices = permutation(new.index)
    test_cutoff = math.floor(len(new)/3)
    test = new.loc[random_indices[1:test_cutoff]]
    train = new.loc[random_indices[test_cutoff:]]
    x_columns = ['amount']
    y_column = ['amount']

    from sklearn.neighbors import KNeighborsRegressor
    knn = KNeighborsRegressor(n_neighbors=5)
    knn.fit(train[x_columns], train[y_column])
    predictions = knn.predict(test[x_columns])"""


if __name__ == '__main__':
    main()
