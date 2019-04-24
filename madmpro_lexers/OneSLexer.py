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
        'root': [
            include('whitespace'),
            # classes
            (r'(class|класс)(\s+)'                          # class keyword
             r'([a-zA-Zа-яА-Я_][a-zA-Zа-яА-Я0-9_.]*)(\s*)'   # class name
             r'(=)(\s*)'                                    # operator =
             r'([^:^{^/]*)(:{0,1})(.*?)({)',                  # class path
             bygroups(Keyword, Text, Name.Class, Text, Operator, Text, String, Operator, using(this), Keyword), 'classdef'),
            # functions
            #(r'(Процедура|Функция|procedure|function)(\s+)'
            #r'([a-zA-Zа-яА-Я_][a-zA-Zа-яА-Я0-9_]*)'
            #r'(\s*\([^;]*?\))',                           # signature
            #bygroups(Keyword, Text, Name.Function, using(this)), 'function'),
            ('', Text, 'statement'),
        ],
        'statement' : [
            include('whitespace'),
            include('statements'),
            (';', Text, '#pop'),
        ],
        'classdef': [
            include('whitespace'),
            (r'([a-zA-Zа-яА-Я_][a-zA-Zа-яА-Я0-9_.]*)(\s+)' # return arguments
             r'([a-zA-Zа-яА-Я_][a-zA-Zа-яА-Я0-9_]*)'      # method name
             r'(\s*\([^;]*?\))'                           # signature
             #r'(' + _ws + r')(;)',
             r'(;)',
             bygroups(using(this), Text, Name.Function, using(this), Text)),
            ('{', Keyword, '#push'),
            ('(}|}\s+;)', Keyword, '#pop'),
            include('statements'),
        ],
        'funcname': [
            (r'[a-zа-яA-ZА-Я_][a-zа-яA-ZА-Я0-9_]*', Name.Function, '#pop')
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            (r'[^\\"\n]+', String), # all other characters
            (r'\\\n', String), # line continuation
            (r'\\', String), # stray backslash
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
