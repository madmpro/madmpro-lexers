# -*- coding: utf-8 -*-
"""
    pygments.lexers.1S
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for language: 1S.

    :license: GNU LGPL, see LICENSE for more details.
"""

import re

from pygments.lexer import RegexLexer, RegexLexerMeta, include, bygroups, using, this
from pygments.token import \
     Text, Comment, Operator, Keyword, Name, String, Number, Literal


__all__ = ['OneSLexer']


class OneSLexer(RegexLexer):

    name = '1S'
    aliases = ['1s', '1c', 'bsl']
    filenames = ['*.1s', '*.prm', '*.1cpp', '*.bsl']
    mimetypes = ['text/x-1s']

    #: optional Comment or Whitespace
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'


    flags = re.IGNORECASE | re.MULTILINE | re.DOTALL | re.UNICODE
    tokens = {
        'whitespace': [
            (r'^\s*#', Comment.Preproc, 'macro'),
            (r'^\s*//#.*?\n', Comment.Preproc),
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text), # line continuation
            (r'//.*?\n', Comment),
        ],

    }
