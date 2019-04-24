# -*- coding: utf-8 -*-

import re

from pygments.lexer import RegexLexer, RegexLexerMeta, include, bygroups, using, this
from pygments.token import *

__all__ = ['OneSLexer']

class OneSLexer(RegexLexer):
    name = 'Language 1C lexer'
    aliases = ['1c']
    filenames = ['*.1s', '*.prm', '*.1cpp', '*.bsl', '*.os']
    mimetypes = ['text/x-1c']

    #: optional Comment or Whitespace
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'

    tokens = {
        'whitespace': [
            (r'^\s*#', Comment.Preproc, 'macro'),
            (r'^\s*//#.*?\n', Comment.Preproc),
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text), # line continuation
            (r'//.*?\n', Comment),
        ],
        'macro': [
            (r'[^/\n]+', Comment.Preproc),
            (r'/[*](.|\n)*?[*]/', Comment),
            (r'//.*?\n', Comment, '#pop'),
            (r'/', Comment.Preproc),
            (r'(?<=\\)\n', Comment.Preproc),
            (r'\n', Comment.Preproc, '#pop'),
        ],
    }
