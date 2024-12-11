class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))


class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")

        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        return [article.title for article in self._articles] or None

    def contributing_authors(self):
        contributing_authors = [
            author
            for author in self.contributors()
            if len([article for article in self._articles if article.author == author]) > 2
        ]
        return contributing_authors if contributing_authors else None

    def add_article(self, article):
        self._articles.append(article)



class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        author.articles().append(self)
        magazine.articles().append(self)
        

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of the Author class.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        self._magazine = value
