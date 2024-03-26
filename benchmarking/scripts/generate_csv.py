import random
import csv

def generate_random_numbers():
    return random.randint(1000, 10000), random.randint(1000, 10000)

num_iterations = 10000

random_numbers_list = [generate_random_numbers() for _ in range(num_iterations)]

with open('random_numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First Number', 'Second Number'])  # Writing header
    writer.writerows(random_numbers_list)