# -*- coding: utf-8 -*-

#import re

from pygments.lexer import RegexLexer, RegexLexerMeta, include, bygroups, using, this
from pygments.token import *

__all__ = ['OneSLexer']

class OneSLexer(RegexLexer):
    name = 'Language 1C lexer'
    aliases = ['1c']
    filenames = ['*.bsl', '*.os']
    mimetypes = ['text/x-1c']

    tokens = {
        'root': [
            (r'\s', Whitespace),
            # Описание строки.
            (r'(\".*?\"|\|.*?\"|\".*|\|.*)', String),
            # Описание коментария.
            (r'//.*?\n', Comment),
            # Описание знаков пунктуации
            (r'[,.!:;()\[\]]', Punctuation),
            # Описание операторов.
            (r'[%^&*+=|<>/?-]', Operator),

        ]
    }

    }