# -*- coding: utf-8 -*-

#import re

from pygments.lexer import RegexLexer, RegexLexerMeta, include, bygroups, using, this
from pygments.token import *

__all__ = ['OneSLexer']

class OneSLexer(RegexLexer):

    tokens = {
        'root': [
            (r'(?s)\{\+{2}.*?\+{2}\}', token.String)
        ]
    }
