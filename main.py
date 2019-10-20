import csv
from Company import Company
from Year import Year
from Quarter import Quarter


def main():
    """Testing a case. May clean this up by adding methods in associated classes"""
    msci = Company("msci", "something")
    msci.years.append(Year(2014))
    print(msci.years[0].year)
    msci.years[0].quarters.append(Quarter("Q1"))
    print(msci.years[0].quarters[0].quarter)
    msci.years[0].quarters[0].assets.unit = "US Dollars"
    print(msci.years[0].quarters[0].assets.unit)
    msci.years[0].quarters[0].assets.amount = 24.50
    print(msci.years[0].quarters[0].assets.amount)


if __name__ == '__main__':
    main()