import csv
from Company import Company
from Year import Year
from Quarter import Quarter
from Indicator import Indicator
import csv


def main():
    test = []
    temread("fundamentals_dataset.csv", test)
    """Test method"""
    #assets_per_quarter("ALCO, INC.", "2015", "Q2", "Assets", test)
    for i in range(len(test)):
        print(test[i].indicators[0].amount)

def temread(file, test):
    with open(file) as csvfile:
        quarter = None
        quarterob = None
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            if row[0] == "period":
                continue

            split = row[0].split(' ')
            temp = split[1]
            if quarter is None:
                quarter = temp
                quarterob = Quarter(quarter)

            if quarter != temp:
                test.append(quarterob)
                quarter = temp
                quarterob = Quarter(quarter)

            if quarter == temp:
                indicator = Indicator(row[3], row[4], row[5])
                quarterob.indicators.append(indicator)




"""        
def read(file, test):
    #Fix time complexity
    companynames = []
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == "period":
                  continue
            elif row[1] not in companynames:
                companynames.append(row[1])
                company = Company(row[1], row[2])
                test.append(company)
            for i in range(len(test)):
                if test[i].name == row[1]:
                    split = row[0].split(' ')
                    yearcount = 0
                    for j in range(len(test[i].years)):
                        if test[i].years[j].year != split[0]:
                            yearcount += 1
                    if yearcount == len(test[i].years):
                        test[i].years.append(Year(split[0]))
                    for k in range(len(test[i].years)):
                        quartercount = 0
                        for m in range(len(test[i].years[k].quarters)):
                            if test[i].years[k].quarters[m].quarter != split[1]:
                                quartercount += 1
                        if quartercount == len(test[i].years[k].quarters):
                            test[i].years[k].quarters.append(Quarter(split[1]))
                        for q in range(len(test[i].years[k].quarters)):
                            if test[i].years[k].year == split[0]:
                                if test[i].years[k].quarters[q].quarter == split[1]:
                                    test[i].years[k].quarters[q].indicators.append(Indicator(row[3], row[4], row[5]))
"""

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
