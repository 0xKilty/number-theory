import csv
import time

def load_csv(file: str):
    data = []
    with open(file, 'r') as data_file:
        csvreader = csv.reader(data_file)
        for row in csvreader:
            data.append([int(row[0]), int(row[1]), int(row[2])])
    return data


def measure_time(func, data):
    start_time = time.perf_counter()
    for item in data:
        func(item[0], item[1], item[2])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time

data = load_csv('../data/random_numbers_10000_100000.csv')
time_taken = measure_time(pow, data)
print(time_taken)
