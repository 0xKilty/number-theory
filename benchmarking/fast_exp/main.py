import time
import csv
import math

def load_csv(file: str):
    data = []
    with open(file, 'r') as data_file:
        csvreader = csv.reader(data_file)
        for row in csvreader:
            data.append([int(row[0]), int(row[1])])
    return data


def python_exp(a: int, b: int):
    return a ** b


def measure_time(func, data):
    start_time = time.perf_counter()
    for item in data:
        print(item[0], item[1])
        func(item[0], item[1])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


data = load_csv('../data/random_numbers.csv')

test_time = measure_time(python_exp, data)
print(f'Time taken: {test_time} seconds')