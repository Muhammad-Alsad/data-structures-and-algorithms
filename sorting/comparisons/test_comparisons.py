import pytest
from Comparisons import Movie, MovieSorter

@pytest.fixture
def sample_movies():
    return [
       Movie('Interstellar', 2014, ['Action', 'Adventure', 'Drama']),
       Movie('The Matrix', 1999, ['Action', 'Sci-Fi']),
       Movie('Fight Club', 1999, ['Drama']),
       Movie('Goodfellas', 1990, ['Crime', 'Drama']),
       Movie('Blade Runner 2049', 2017, ['Sci-Fi', 'Thriller']),
    ]

def test_sort_by_year(sample_movies):
    sorter = MovieSorter()
    sorted_movies = sorter.sort_by_year(sample_movies)
    years = [movie.year for movie in sorted_movies]
    assert years == [2017, 2014, 1999, 1999, 1990]

def test_sort_by_title(sample_movies):
    sorter = MovieSorter()
    sorted_movies = sorter.sort_by_title(sample_movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == ['Blade Runner 2049', 'Fight Club', 'Goodfellas', 'Interstellar','The Matrix']

def test_sort_by_title_with_leading_articles(sample_movies):
    # Add movies with leading articles to the fixture
    sample_movies.append(Movie('The Avengers', 2012, ['Action', 'Adventure', 'Sci-Fi']))
    sample_movies.append(Movie('A Beautiful Mind', 2001, ['Biography', 'Drama']))

    sorter = MovieSorter()
    sorted_movies = sorter.sort_by_title(sample_movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == ['A Beautiful Mind', 'Blade Runner 2049', 'Fight Club', 'Goodfellas', 'Interstellar', 'The Avengers', 'The Matrix']

