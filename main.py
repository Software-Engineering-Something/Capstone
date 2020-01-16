import dask.dataframe as dd
import pandas as pd


def main():
    """dask.dataframe is a dataframe that stores files in a dataframe(a two-dimensional data structure), this reads a
    csv file and parses into data. From there we can use query like calls to search for specific data at O(N) time,
    I'm still new to dataframes, so doing these two search queries may somehow be done in line"""

    df = pd.read_csv("fundamentals_dataset.csv")
    ddf = dd.from_pandas(df, npartitions=2)
    new = df[df.company == '1347 Property Insurance Holdings, Inc.'][df.period == '2014 Q1']
    new['amount'] = new['amount'].str.replace(',', '')
    print(new[new['amount'].astype(int) > 20000000])
    temp = new[new['amount'].astype(int) > 20000000]
    print("getting only the second rows amount: " + temp['amount'].iloc[1])


if __name__ == '__main__':
    main()
