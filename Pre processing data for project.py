import csv

data = []

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
star_data = data[1:]

for data_point in star_data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
star_data.sort(key=lambda star_data: star_data[2])


with open("dwarf_star_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
