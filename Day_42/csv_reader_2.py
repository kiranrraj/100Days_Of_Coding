# Title  : Csv Module
# Author : Kiran Raj R.
# Date   : 25/11/2020

import csv

file_read = open('sample.csv');
file_reader = csv.reader(file_read);

for row in file_reader:
    print(f"{str(file_reader.line_num)}) {str(row)}");