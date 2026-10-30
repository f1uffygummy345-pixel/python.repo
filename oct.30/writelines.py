movies = ["Shrek", "Star Wars", "Star Trek", "X-Men"]

with open("movies.txt", "w", encoding='utf-8') as file:
    file.writelines(f"{movie}\n" for movie in movies)