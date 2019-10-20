import csv
from Company import Company
from Year import Year
from Quarter import Quarter


def main():
    """Testing a case. May clean this up by adding methods in associated classes"""
    temp = Company("msci", "something")
    temp.years.append(Year(2014))
    print(temp.years[0].year)
    temp.years[0].quarters.append(Quarter("Q1"))
    print(temp.years[0].quarters[0].quarter)
    temp.years[0].quarters[0].assets.unit = "US Dollars"
    print(temp.years[0].quarters[0].assets.unit)
    temp.years[0].quarters[0].assets.amount = 24.50
    print(temp.years[0].quarters[0].assets.amount)


if __name__ == '__main__':
    main()