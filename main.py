import csv
from Company import Company
from Year import Year
from Quarter import Quarter
import csv


def main():
    """Testing a case. May clean this up by adding methods in associated classes"""
    """msci = Company("msci", "something")
    msci.years.append(Year(2014))
    print(msci.years[0].year)
    msci.years[0].quarters.append(Quarter("Q1"))
    print(msci.years[0].quarters[0].quarter)
    msci.years[0].quarters[0].assets.unit = "US Dollars"
    print(msci.years[0].quarters[0].assets.unit)
    msci.years[0].quarters[0].assets.amount = 24.50
    print(msci.years[0].quarters[0].assets.amount)"""
    test = []
    read("fundamentals_dataset.csv", test)
    for i in range(len(test)):
        print(test[i].name + ", " + test[i].ticker)


def read(file, test):
    companynames = []
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[1] not in companynames and row[1] != "company":
                companynames.append(row[1])
                company = Company(row[1], row[2])
                test.append(company)


if __name__ == '__main__':
    main()
