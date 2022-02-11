"""Model for a quote. Contains body and author."""
import doctest
import re


class QuoteModel():

    """Quotes in docs and other files are of the form:
            "body" - author
            or
            body - author (no quotes)
    Use these regexps to parse.
    """

    regexp_1 = r'\s*\"([^\"]*?)\"\s*-\s*([^\"]*)\s*'
    regexp_2 = r'\s*([^\"]*?)\s*-\s*([^\"]*)\s*'

    def __init__(self, body, author):
        """ Constructor """
        self.body = body
        self.author = author
        if not self.is_valid():
            raise ValueError("Badly formed quote model")

    def is_valid(self):
        """Check if model is valid."""
        return bool(self.body) and bool(self.author)

    def __repr__(self) -> str:
        """Model to string."""
        return f'A quote: {self.body} by {self.author}'

    def get_formatted(self) -> str:
        """Store body and author and format nicely to be written into an image
        """
        return f"\"{self.body}\"\n    - {self.author}"

    @staticmethod
    def from_text(text: str):

        """Parse a line using the regexps described above
        Returns a valid QuoteModel or throws a ValueError
        """

        groups = None
        if re.match(QuoteModel.regexp_1, text):
            groups = re.findall(QuoteModel.regexp_1, text)
        elif re.match(QuoteModel.regexp_2, text):
            groups = re.findall(QuoteModel.regexp_2, text)

        if not groups or len(groups) != 1:
            raise ValueError('Parsing text to model failed ' + text)
        matches = groups[0]
        return QuoteModel(matches[0], matches[1])


if __name__ == "__main__":
    # eg = {'kitty': Cat('Spot', 3)
    # doctest.testmod(extraglobs=eg)""" Comment """
    pass
