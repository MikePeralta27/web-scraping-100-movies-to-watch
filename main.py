import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_website = response.text
soup = BeautifulSoup(movie_website, "html.parser")

movies_tags = soup.select("h3", {"class": "title"})
movies_title = [movies_tag.getText() for movies_tag in movies_tags]
movie_sorted_reverse = sorted(movies_title, reverse=False)

with open("100-movies.txt", "w") as movies_list:
    movies_list.write("\n".join(movie_sorted_reverse))





