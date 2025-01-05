#CSV stands for Comma Separated Values.
#it is best way to represent tabular form of data

# with open("day_25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#this above code will provide us a list which is very hard to read
#instead

import csv

with open("day_25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempretures = []
    for row in data:
        if row[1] != "temp":
            tempretures.append(int(row[1]))
    print(tempretures)


# using csv is very  lengthy so for data analysis we use pandas library

