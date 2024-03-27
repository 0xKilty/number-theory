import random
import csv

def generate_random_numbers():
    return random.randint(100, 100), random.randint(100, 100)

num_iterations = 10000

random_numbers_list = [generate_random_numbers() for _ in range(num_iterations)]

with open('../data/random_numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(random_numbers_list)