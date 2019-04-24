""" pygments.lexers.1C """

#import re
from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ("Lang1CLexer",)

class Lang1CLexer(RegexLexer):

    """Simple lexer for Language 1C."""

    name = 'Language 1C lexer'
    aliases = ['1c', 'bsl']
    filenames = ['*.bsl', '*.os']
    mimetypes = ['text/x-1c']

    tokens = {
        'root': [
            (r'\s', Whitespace),

        ]
    }
