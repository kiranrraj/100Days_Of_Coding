import csv

out_file = open('out.csv', 'w', newline="")
out_write = csv.writer(out_file, delimiter="\t", lineterminator="\n\n");
out_write.writerow(['8/12/2020 23:27', 'Peach', '150']);
out_write.writerow(['8/12/2020 23:27', 'Grapes', '120']);
out_file.close();