import csv
from functools import reduce

def getPoliceReports():
    police_reports = []

    with open('data\policereports.csv') as file:
        reader = csv.reader(file)
        first_row = True

        # headers
        h = []

        # rows
        for r in reader:

            if first_row:
                h = r
                first_row = False

            else:
                d = {}
                for i in range(len(h)):
                    d[h[i]] = r[i]

                police_reports.append(d)

    return police_reports


def main():
    police_reports = getPoliceReports()

    police_reports = list(filter(lambda a: a["zip_code"] != "", police_reports))

    police_reports = list(filter(lambda a: a["neighborhood"] != "", police_reports))

    police_reports = list(filter(lambda a: a["totalresponsetime"] != "", police_reports))

    print(police_reports[0:2])

    average_response_time = sum(float(d['totalresponsetime']) for d in police_reports) / len(police_reports)

    print(average_response_time)

if __name__ == "__main__":
    main()