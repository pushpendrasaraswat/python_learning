from bs4 import BeautifulSoup
import requests

URL="https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

website_soup= BeautifulSoup(response.text,"html.parser")

all_movies = [movie.getText() for movie in website_soup.find_all(name="h2") if movie.find("strong")]


movies = all_movies[::-1] # Print the list in reverse order

for i in range (len(all_movies)-1,0,-1):
    print(all_movies[i])


with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")