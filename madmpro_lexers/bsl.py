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
            # Описание ключевых слов
            (ur'(?i)(Var|Val|New|Return|Goto|Continue|Break|Execute)\b|'
             ur'(?iu)(Перем|Знач|Новый|Возврат|Перейти|Продолжить|Прервать|Выполнить)\b|'
             # Условие Если
             ur'(?i)(EndIf|If|Then|ElsIf|Else)\b|'
             ur'(?iu)(КонецЕсли|Если|Тогда|ИначеЕсли|Иначе)\b|'
             # Циклы
             ur'(?i)(EndDo|Do|For|Each|In|While|To)\b|'
             ur'(?iu)(КонецЦикла|Цикл|Для|Каждого|Из|Пока|По)\b|'
             # Процедура и Функция
             ur'(?i)(EndProcedure|Procedure|EndFunction|Function)\b|'
             ur'(?iu)(КонецПроцедуры|Процедура|КонецФункции|Функция)\b|'
             # Попытка
             ur'(?i)(EndTry|Try|Raise|Except)\b|'
             ur'(?iu)(КонецПопытки|Попытка|ВызватьИсключение|Исключение)\b|'
             # Условия: И, Или, Не
             ur'(?i)(And|Or|Not)\b|'
             ur'(?iu)(И|Или|Не)\b'
             , Keyword.Reserved),

        ]
    }
