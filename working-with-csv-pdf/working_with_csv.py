import csv

data = open('example.csv', encoding='utf-8') # for accomodating @ symbols and so on..
csv_data = csv.reader(data)
data_lines = list(csv_data)

# print(data_lines) # this is a list of lists

#inspecting single element of data_lines
# print(data_lines[0]) # this is the title row

# print(len(data_lines)) # 1000 records with 1st row as title


#grab email of all records
# emails = []
# for line in data_lines[1:]: # excluding row 1 as it has title
#     emails.append(line[3])

# print(emails)

#grab full name of each record
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+ ' ' + line[2])

print(full_names)

