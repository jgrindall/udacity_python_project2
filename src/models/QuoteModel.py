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
        """Check if model is valid.
        
        >>> q1.is_valid()
        True
        >>> q3.is_valid()
        False
        """
        return bool(self.body) and bool(self.author)

    def __repr__(self) -> str:
        """Model to string."""
        return f'A quote: {self.body} by {self.author}'

    def get_formatted(self) -> str:
        """Store body and author and format nicely to be written into an image
        """
        return f"\"{self.body}\"\n    - {self.author}"

    def __eq__(self, other):
        return self.author == other.author and self.body == other.body
    
    @staticmethod
    def from_text(text: str):

        """Parse a line using the regexps described above
        Returns a valid QuoteModel or throws a ValueError
        
        Test creating basic model
        >>> QuoteModel.from_text("Body1 - Author") == q1
        True
        
        Test whitespace
        >>> QuoteModel.from_text('   "Body2"          -     Author') == q2
        True
     
        Test error
        >>> q = QuoteModel.from_text("")
        Traceback (most recent call last):
        ...
        ValueError: Parsing text to model failed 
        
        Test error
        >>> q = QuoteModel.from_text("Body")
        Traceback (most recent call last):
        ...
        ValueError: Parsing text to model failed Body
        
        Test error - mismatched quotes
        >>> q = QuoteModel.from_text('"Body - Author')
        Traceback (most recent call last):
        ...
        ValueError: Parsing text to model failed "Body - Author
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
    print("tests...")
    q3 = QuoteModel('Body3', "Author")
    q3.author = ""
    eglobs = {
        'q1': QuoteModel('Body1', "Author"),
        'q2': QuoteModel('Body2', "Author"),
        'q3': q3
        }
    doctest.testmod(extraglobs=eglobs)



