#CSV stands for Comma Separated Values.
#it is best way to represent tabular form of data

# with open("day_25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#this above code will provide us a list which is very hard to read
#instead

# import csv

# with open("day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempretures = []
#     for row in data:
#         if row[1] != "temp":
#             tempretures.append(int(row[1]))
#     print(tempretures)


# using csv is very  lengthy so for data analysis we use pandas library

import pandas

data = pandas.read_csv("day_25/weather_data.csv")
print(data)

#here we can easiely print a column using column heading
print(data["temp"])
#or
print(data.condition)

#dataframe are two dimention obj in pandas.
#eg: a table with rows and columns.

#series is a one dimention obj.
#eg: a signle column or a list.


#we can convert a dataframe into a dicrionary using pandas
data_dictionary = data.to_dict()
print(data_dictionary)

#we can convert a series into a list.
temp_list = data["temp"].to_list()
print(temp_list)


#to get the avg
avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)

#OR
print(data["temp"].mean())

#simillarly
print(data["temp"].max())


#Get data of a row.
print(data[data.day == "monday"])
print(data[data.temp == data.temp.max()])


#to get one element from a row.
monday = data[data.day == "monday"]
print(monday.condition)


mon_temp = monday.temp
ferh_temp = (mon_temp*9/5) + 32
print(ferh_temp)


#create a dataframe from scratch.
data_dict = {
    "student": ["Amy", "james", "angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
#we can also save it as a csv.
data.to_csv("new_data.csv")
