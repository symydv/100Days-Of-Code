# <span class="content_content__i0P3p" data-test="content">
# <h2><strong>100) Reservoir Dogs (1992)</strong></h2>
# </span>

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")

titles = soup.select(selector="h2 strong")

MovieList1 = []
for title in titles :
    MovieList1.append(title.getText())



file = open("./day_45/MovieList.txt", "w")
for movie in MovieList1[::-1]:  #MoviesList1[::-1] reverses the list
    file.writelines(f"\n{movie}")  

file.close()


