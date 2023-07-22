class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

    def __repr__(self):
        return f"Movie(title='{self.title}', year={self.year}, genres={self.genres})"


class MovieSorter:
    @staticmethod
    def sort_by_year(movies):
        movies.sort(key=lambda x: x.year, reverse=True)
        return movies

    
    def sort_by_title(self, movies):
        def remove_leading_articles(title):
            articles = ["A ", "An ", "The "]
            for article in articles:
                if title.startswith(article):
                    return title[len(article):]
            return title

        movies.sort(key=lambda x: remove_leading_articles(x.title.lower()))
        return movies



movies = [
    Movie('Interstellar', 2014, ['Action', 'Adventure', 'Drama']),
    Movie('The Matrix', 1999, ['Action', 'Sci-Fi']),
    Movie('Fight Club', 1999, ['Drama']),
    Movie('Goodfellas', 1990, ['Crime', 'Drama']),
    Movie('Blade Runner 2049', 2017, ['Sci-Fi', 'Thriller']),
]

movie_sorter = MovieSorter()
sorted_by_year = movie_sorter.sort_by_year(movies)
print("Sorted by Year:")
print(sorted_by_year)

sorted_by_title = movie_sorter.sort_by_title(movies)
print("Sorted by Title:")
print(sorted_by_title)
