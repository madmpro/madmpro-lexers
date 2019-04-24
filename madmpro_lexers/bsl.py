# -*- coding: utf-8 -*-
""" pygments.lexers.1C """

#import re
from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ("Lang1CLexer",)

class Lang1CLexer(RegexLexer):

    """Simple lexer for Language 1C."""

    name = 'Language 1C lexer'
    aliases = ['bsl']
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
            # Литералы Истина, Ложь
            (ur'(?i)(True|False|Null)\b|'
             ur'(?iu)(Истина|Ложь)\b'
             , Literal),
            # Описание чисел
            (r'\d*\.\d\b', Number),
            # Описание дат
            (r'\'\d*\'', Literal.Date),
            # Описание имён переменных и функций
            (ur'(?iu)\w*\b', Name),
        ]
    }
