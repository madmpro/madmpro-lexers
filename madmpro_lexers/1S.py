# -*- coding: utf-8 -*-
"""
    pygments.lexers.1S
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for language: 1S.

    :license: GNU LGPL, see LICENSE for more details.
"""

#import re

from pygments.lexer import RegexLexer, RegexLexerMeta, include, bygroups, using, this
from pygments.token import *

__all__ = ['OneSLexer']

class OneSLexer(RegexLexer):

    tokens = {
        'root': [
            (r'(?s)\{\+{2}.*?\+{2}\}', token.String),
            (r'(?s)\{\-{2}.*?\-{2}\}', token.String),
            (r'(?s)\{={2}.*?={2}\}', token.String),
            (r'(?s)\{>{2}.*?<{2}\}', token.String),
            (r'(?s)\{~{2}.*?~>.*?~{2}\}', token.String),
            (r' |\t', token.Whitespace),
            (r'.', token.Text)
        ]
    }
