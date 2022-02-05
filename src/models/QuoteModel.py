""" Comment """
import doctest


class QuoteModel():

    quote_re_format = '\"(.*?)\"\s*-\s*(.*?)\s*'

    def __init__(self, body, author):
        """ Constructor """
        self.body = body
        self.author = author

    def is_valid(self):
        """ Constructor """
        return bool(self.body) and bool(self.author)

    def __repr__(self) -> str:
        """ Constructor """
        return f'A quote: {self.body} by {self.author}'

    def get_formatted(self) -> str:
        return f"\"{self.body}\" - {self.author}"


if __name__ == "__main__":
    # eg = {'kitty': Cat('Spot', 3)
    # doctest.testmod(extraglobs=eg)""" Comment """
    pass
