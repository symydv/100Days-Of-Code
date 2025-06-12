#Problem 1
# fruits = ["apple", "Banana", "Pear"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")

# make_pie(2)
# make_pie(3)


#Problem 2
# facebook_post =[
#     {"likes":21, "comments":2},
#     {"likes":13, "comments":2, "shares": 1},
#     {"likes":33, "comments":8, "shares": 3},
#     {"comments":4, "shares": 2},
#     {"shares":1, "comments":1},
#     {"likes":19, "comments":3},
# ]


# total_likes = 0

# for post in facebook_post:
#     try:
#         total_likes = total_likes + post["likes"]
#         #in above line error will occure because in some posts "like" keyword is not there
#     except KeyError:
#         pass

# print(f"Total likes are: {total_likes}")