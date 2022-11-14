
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find_all(name="h3", class_="title")
print(title)
title_list = []


for title_name in list(reversed(title)):
    title_list.append((title_name.getText()))

print(title_list)

with open("movie_list.txt", "w") as file:
    for i in range(0,len(title_list)):
        file.write(f"{title_list[i]}\n")

