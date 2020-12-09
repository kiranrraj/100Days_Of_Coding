# To read you need to import csv module
import csv

# To read a file first open it.
file_read = open('sample.csv');

#creater a reader objects
file_reader = csv.reader(file_read);

#Convert the reader object into list
file_data = list(file_reader);
print(file_data);