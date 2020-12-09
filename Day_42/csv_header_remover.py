import csv, os

#crate a folder called csv_folder
os.makedirs("csv_folder", exist_ok=True)

for csv_file in os.listdir('.'):
    if not csv_file.endswith('.csv'):
        continue
    print(f'Removing header from {csv_file}')

    rows = []
    file_obj = open(csv_file)
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue
        rows.append(row)
    file_obj.close()

    file_obj = open(os.path.join("csv_folder", csv_file), 'w', newline="")
    csv_write = csv.writer(file_obj)
    for row in rows:
        csv_write.writerow(row)
    file_obj.close()