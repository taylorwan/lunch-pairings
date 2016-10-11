import datetime
import argparse
import csv
import random
import copy

array = []

def populate_database():
    print 'Starting'
    with open('new_names.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            if row[0] != '' and row[0] != 'Last Name' and row[3] == 'DC' and row[5] == 'YES':
                first_name = row[1]
                last_name  = row[0]
                array.append(first_name + " " + last_name)
    print_pairings(array)

def print_pairings(array):
    while len(array) > 1:
        a = random.choice(array)
        array.remove(a)
        b = random.choice(array)
        array.remove(b)
        print a + " and " + b

    print array

if __name__ == "__main__":
    populate_database()
