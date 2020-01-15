import dask.dataframe


def main():
    """dask.dataframe is a dataframe that stores files in a dataframe(a two-dimensional data structure), this reads a
    csv file and parses into data. From there we can use query like calls to search for specific data at O(N) time,
    I'm still new to dataframes, so doing these two search queries may somehow be done in line"""

    # reads from csv and stores into a dataframe
    data = dask.dataframe.read_csv("fundamentals_dataset.csv")
    # searches for all instances of specified company name, stores in temp dataframe
    temp = data[(data.company == '1347 Property Insurance Holdings, Inc.')]
    # searches for all instances of specified period within temp dataframe and prints results
    print(temp[(temp.period == '2014 Q1')].compute())


if __name__ == '__main__':
    main()
