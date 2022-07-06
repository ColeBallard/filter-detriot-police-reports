import csv
import json
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

def part1(police_reports):

    average_response_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["totalresponsetime"]), police_reports, 0) / len(police_reports)
    
    average_dispatch_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["dispatchtime"]), police_reports, 0) / len(police_reports)

    average_total_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["totaltime"]), police_reports, 0) / len(police_reports)

    # average_response_time = sum(float(d['totalresponsetime']) for d in police_reports) / len(police_reports)

    print("Part 1")
    print("Average Response Time: " + str(average_response_time))
    print("Average Dispatch Time: " + str(average_dispatch_time))
    print("Average Total Time: " + str(average_total_time))
    print("")

    return {"Average Response Time":average_response_time, "Average Dispatch Time":average_dispatch_time, "Average Total Time":average_total_time}

def part2(police_reports):
    print("Part 2")
    print("")

    neighborhoods = set()

    for dictionary in police_reports:
        neighborhoods.add(dictionary['neighborhood'])

    police_reports_by_neighborhood = []

    for neighborhood in neighborhoods:
        police_reports_by_neighborhood.append(list(filter(lambda a: a["neighborhood"] == neighborhood, police_reports)))

    neighborhood_times = []

    for neighborhood in police_reports_by_neighborhood:
        average_response_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["totalresponsetime"]), neighborhood, 0) / len(neighborhood)

        average_dispatch_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["dispatchtime"]), neighborhood, 0) / len(neighborhood)

        average_total_time = reduce(lambda aggregate_value, next_row: aggregate_value + float(next_row["totaltime"]), neighborhood, 0) / len(neighborhood)

        print(neighborhood[0]["neighborhood"])
        print("Average Response Time: " + str(average_response_time))
        print("Average Dispatch Time: " + str(average_dispatch_time))
        print("Average Total Time: " + str(average_total_time))
        print("")

        neighborhood_times.append({"Name":neighborhood[0]["neighborhood"], "Average Response Time":average_response_time, "Average Dispatch Time":average_dispatch_time, "Average Total Time":average_total_time})

    return neighborhood_times

def part3(main_dict):
    with open('data/detroitpolicedata.json', 'w') as file:
        json.dump(main_dict, file)

def main():
    police_reports = getPoliceReports()

    police_reports = list(filter(lambda a: a["zip_code"] != "", police_reports))

    police_reports = list(filter(lambda a: a["neighborhood"] != "", police_reports))

    police_reports = list(filter(lambda a: a["totalresponsetime"] != "", police_reports))

    police_reports = list(filter(lambda a: a["dispatchtime"] != "", police_reports))

    police_reports = list(filter(lambda a: a["totaltime"] != "", police_reports))

    main_dict = part1(police_reports)

    main_dict["Neighborhood Times"] = part2(police_reports)

    part3(main_dict)

if __name__ == "__main__":
    main()