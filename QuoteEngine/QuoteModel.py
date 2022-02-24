"""Class to encapsulate one quote with its author."""


class QuoteModel():
    """Class to estructure the body and author

Attributes:
    body - A string to store the body of the quote.
    author - A string to store the author of the quote.

"""

    def __init__(self, body, author):
        """Initiate QuoteModel with quote body and author."""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """return string of the data (body and author)"""
        return f"{self.body} {self.author}"
