import csv
from Company import Company
from Year import Year
from Quarter import Quarter
import csv


def main():
    """Testing a case."""
    test = []
    read("fundamentals_dataset.csv", test)
    for i in range(len(test)):
        print(test[i].name + ", " + test[i].ticker + " " + test[i].years[0].quarters[0].assets.unit + " " +
              test[i].years[0].quarters[0].assets.amount)


def read(file, test):
    """Fix time complexity"""
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
                    quartercount = 0
                    for j in range(len(test[i].years)):
                        if test[i].years[j].year != split[0]:
                            yearcount += 1
                        for k in range(len(test[i].years[j].quarters)):
                            if test[i].years[j].quarters[k].quarter != split[1]:
                                quartercount += 1
                    if yearcount == len(test[i].years):
                        test[i].years.append(Year(split[0]))
                    for k in range(len(test[i].years)):
                        if quartercount == len(test[i].years[k].quarters):
                            test[i].years[k].quarters.append(Quarter(split[1]))
                        for l in range(len(test[i].years[k].quarters)):
                            if test[i].years[k].quarters[l].quarter == split[1]:
                                test[i].years[k].quarters[l].assets.unit = row[4]
                                test[i].years[k].quarters[l].assets.amount = row[5]


if __name__ == '__main__':
    main()
