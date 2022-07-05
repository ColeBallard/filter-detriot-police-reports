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

    police_reports = list(filter(lambda a: a["dispatchtime"] != "", police_reports))

    police_reports = list(filter(lambda a: a["totaltime"] != "", police_reports))

    average_response_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["totalresponsetime"]), police_reports, 0) / len(police_reports)
    
    average_dispatch_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["dispatchtime"]), police_reports, 0) / len(police_reports)

    average_total_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["totaltime"]), police_reports, 0) / len(police_reports)

    # average_response_time = sum(float(d['totalresponsetime']) for d in police_reports) / len(police_reports)

    print("Part 1")
    print("Average Response Time: " + str(average_response_time))
    print("Average Dispatch Time: " + str(average_dispatch_time))
    print("Average Total Time: " + str(average_total_time))



if __name__ == "__main__":
    main()