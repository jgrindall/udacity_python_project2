import re
from ..errors import ParseError


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
            raise ParseError("Badly formed quote model")

    def is_valid(self):
        """Check if model is valid."""
        return bool(self.body) and bool(self.author)

    def __repr__(self) -> str:
        """Model to string."""
        return f'A quote: {self.body} by {self.author}'

    def get_formatted(self) -> str:
        """Store body and author and format nicely to be written into an image
        """
        return f'\"{self.body}\"\n    - {self.author}'

    def __eq__(self, other):
        return self.author == other.author and self.body == other.body

    @staticmethod
    def from_text(text: str):

        """Parse a line using the regexps described above
        Returns a valid QuoteModel or throws a ValueError

        Arguments:
            :text {str} - the line of test to use to construct the model
        """

        # first remove any non utf-8 weirdness
        # https://stackoverflow.com/questions/8898294/convert-utf-8-with-bom-to-utf-8-with-no-bom-in-python

        text = bytes(text.strip(), 'utf-8').decode('utf-8-sig', 'ignore')

        groups = None
        if re.match(QuoteModel.regexp_1, text):
            groups = re.findall(QuoteModel.regexp_1, text)
        elif re.match(QuoteModel.regexp_2, text):
            groups = re.findall(QuoteModel.regexp_2, text)

        if not groups or len(groups) != 1:
            raise ValueError('Parsing text to model failed:' + text)
        matches = groups[0]
        return QuoteModel(matches[0], matches[1])
