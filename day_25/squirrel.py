import pandas

sq = pandas.read_csv("day_25/Central-Park-Squirrel-Census-Squirrel-Data.csv")
color = sq["Primary Fur Color"]
color.to_list
sq_color = {
"fur color" : ["Gray", "Black", "Cinnamon"],
"count" : [0, 0, 0]
}
number = sq_color["count"]
for rang in color:
    if rang == "Gray":
        number[0] += 1
    if rang == "Black":
        number[1] += 1
    if rang == "Cinnamon":
        number[2] += 1


data = pandas.DataFrame(sq_color)
data.to_csv("day_25/squirrel_count.csv ")
print(data)
    
#you can also use madam's code check day 25, 004

