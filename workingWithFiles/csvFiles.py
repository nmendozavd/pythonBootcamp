# CSV (comma separated variables): only contains raw data
# outside library: Pandas

import csv

# open the file (encoding necessary for special characters)
data = open('example.csv', encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

# read all data 
# print(data_lines)

# check column names (always the first line)
print(data_lines[0])

# check length of data/rows
print(len(data_lines))

# print lines until row 5
for line in data_lines[:5]:
    print(line)

# get data point 10
print(data_lines[10])

# get email with data point
print(data_lines[10][3])

# grab all columns (emails) up until row 15
all_emails = []

for line in data_lines[1:15]:
    all_emails.append(line[3])

#print(all_emails)

# Write to a CSV file mode is set to w for write, a for append, newline to empty string in this case
file_to_output = open('to_save_file.csv', mode='a', newline='')

csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['a','b','c'])

# close th file
file_to_output.close()
