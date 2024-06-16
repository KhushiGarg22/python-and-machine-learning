import csv

def read_csv_file(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

filename = input("Enter the CSV file name: ")
read_csv_file(filename)