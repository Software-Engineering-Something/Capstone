import csv
from Company import Company
from Year import Year
from Quarter import Quarter
from Indicator import Indicator
import csv


def main():
    test = []
    read("fundamentals_dataset.csv", test)
    """Test method"""
    assets_per_quarter("EXA CORP", "2014", "Q1", "Assets", test)


def read(file, test):
    with open(file) as csvfile:
        quarter = None
        quarterob = None
        year = None
        yearob = None
        company = None
        companyob = None
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            if row[0] == "period":
                continue
            split = row[0].split(' ')
            temp = split[1]
            yeartemp = split[0]

            if quarter is None:
                quarter = temp
                quarterob = Quarter(quarter)

            if quarter != temp:
                if year is None:
                    year = yeartemp
                    yearob = Year(year)
                if year != yeartemp:
                    if company is None:
                        company = row[1]
                        companyob = Company(company, row[2])
                    if company != row[1]:
                        test.append(companyob)
                        company = row[1]
                        companyob = Company(company, row[2])
                    if company == row[1]:
                        companyob.years.append(yearob)
                        year = yeartemp
                        yearob = Year(year)
                if year == yeartemp:
                    yearob.quarters.append(quarterob)
                    quarter = temp
                    quarterob = Quarter(quarter)

            if quarter == temp:
                indicator = Indicator(row[3], row[4], row[5])
                quarterob.indicators.append(indicator)


def assets_per_quarter(company, year, quarter, assets, test):
    for i in range(len(test)):
        if test[i].name == company:
            for j in range(len(test[i].years)):
                if test[i].years[j].year == year:
                    for k in range(len(test[i].years[j].quarters)):
                        if test[i].years[j].quarters[k].quarter == quarter:
                            for q in range(len(test[i].years[j].quarters[k].indicators)):
                                if test[i].years[j].quarters[k].indicators[q].name == assets:
                                    print(test[i].years[j].quarters[k].indicators[q].unit + " " +
                                          test[i].years[j].quarters[k].indicators[q].amount)


if __name__ == '__main__':
    main()
