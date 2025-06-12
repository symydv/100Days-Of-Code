'''Beautyfull soup is a python library for pulling data out of HTML and  XML files'''

from bs4 import BeautifulSoup

# with open("day_45/website.html", encoding="utf8") as file: #sometime python cant uderstand encoding thats why we included it here otherwise no need.
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser") #html.parser helps python understaand html.


# print(soup) #It will print entire html code.

#print(soup.prettify()) #this code will print entire html code but with proper indentations

# print(soup.title) # It will print the title tag of website.

# print(soup.title.name) # It will print the name of title tag which is title.

# print(soup.title.string) #It will print the string that is contained by title tag.

#print(soup.a) #it will print first anchor tag in our html code , similarlly can be done with other tags.

# all_anchor_tags = soup.find_all(name="a")  #It will find all anchor tags not just one. we can change it to p to get paragraph tags
# # print(all_anchor_tags)

# for tags in all_anchor_tags:
#     print(tags.getText()) #Print text of anchhor tags.
#     print(tags.get("href")) #to print out the links in anchor tags.


# heading = soup.find(name="h1", id = "name") #to get h1 with a specific id.we can do same for class just replace id with class_  ..
# print(heading)


# company_url = soup.select_one(selector="p a") #this selector works as css selector where p a shows that we need to select anchor tag which is inside a paragraph tag.
# print(company_url)
# #same we can do for class and id.
# name = soup.select_one("#name") # selects tag with id ="name"
# print(name)


#__________________________________________________________________________________________________________________________________________________
#Web Scrapping a website (Hacker news website)
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text #This will get us the code of the website

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = soup.find_all(class_ = "titleline") #wwe are getting all the titles of headlines.
titleList = []
for title in titles:

    titleList.append(title.getText())


upvotes = soup.find_all(class_ = "score")
likes = []
for upvote in upvotes:
    likes.append(int(upvote.getText().split()[0]))
    #upvote.getText() will get you text like 40 points etc .split will plit it into 40, point thenn we select 40 and convert it into int.



# print(titleList)
# print(likes)

max = 0
max_index = 0
for index,like in enumerate(likes):
    if like > max:
        max = like
        max_index = index

final = [titleList[max_index], likes[max_index]]
print(final)


#----------------#IMPORTANT#------------------------

#Add "/robots.txt" at the end of website url to check what data you are legaly(lawfully) allowed to scrap or automate from that website. 
