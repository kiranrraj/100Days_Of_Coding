import csv

file_read = open('sample.csv');
file_reader = csv.reader(file_read);

for row in file_reader:
    print(f"{str(file_reader.line_num)}) {str(row)}");