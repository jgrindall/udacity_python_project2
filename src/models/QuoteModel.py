""" Comment """
import doctest


class QuoteModel():
    def __init__(self, body, author):
        """ Constructor """
        self.body = body
        self.author = author

    def is_valid(self):
        """ Constructor """
        return bool(self.body) and bool(self.author)

    def __repr__(self) -> str:
        """ Constructor """
        return f'A quote <{self.body} by {self.author}'


if __name__ == "__main__":
    #eg = {'kitty': Cat('Spot', 3)
    #doctest.testmod(extraglobs=eg)""" Comment """
    pass