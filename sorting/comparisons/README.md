# Sorting Comparisons

## Author : Muhammad Al-Sa'd 

### How to initialize/run your application:
    - cd to the file.py


### Testing 
    - pytest --> file.py 


#### Algorithm:
    - class MovieSorter:
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


#### Efficency :
     - sortbytitle: 
        - Time: O(n log (n))
        - Space : O(n)

     -  sortbyyear:
        - Time : O(n^2)
        - Space : O(n)
