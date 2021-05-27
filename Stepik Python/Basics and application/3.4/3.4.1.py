import csv
import re
list_primary_type = []
pattern = r"../../2015.*"
with open("Crimes.csv") as inf:
    reader = csv.reader(inf)
    for line in reader:
        if re.match(pattern,line[2]):
            list_primary_type.append(line[5])
print(max(set(list_primary_type), key=lambda x: list_primary_type.count(x)))
print(list_primary_type)