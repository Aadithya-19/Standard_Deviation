import math
import csv

with open("data_3_stnd.csv", newline='') as f:
    file_object = csv.reader(f)
    data_list = list(file_object)

data = data_list[0]

def mean(data):
    n = len(data)
    sum = 0
    for a in data:
        sum+=int(a)

    mean = sum/n
    return(mean)

sqrd_list = []

for x in data:
    dif = int(x) - mean(data)
    dif = dif**2
    sqrd_list.append(dif)
    print(dif)

tot = 0

for a in sqrd_list:
    tot+=int(a)

result = tot/(len(data)-1)

stnd_dev = math.sqrt(result)
print(str(stnd_dev) + " is the standard deviation.")