import csv
import pandas as pd

data1 = 'data.csv'
data2 = 'dwarf_star_sorted.csv'

dataset1 = []
dataset2 = []
with open(data1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        dataset1.append(i)
        
with open(data2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        dataset2.append(i)

h1 = dataset1[0]
h2 = dataset2[0]

pad1 = dataset1[1:]
pad2 = dataset2[1:]

h = h1+h2

pad =[]

for i in pad1:
    pad.append(i)
for j in pad2:
    pad.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(pad)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)
