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
            # Описание чисел
            (r'\d*\.\d\b', Number),
            # Описание дат
            (r'\'\d*\'', Literal.Date),
            # Описание имён переменных и функций
            (r'(?iu)\w*\b', Name),
            # Описание ключевых слов
            (r'(?i)(Var|Val|New|Return|Goto|Continue|Break|Execute)\b|'
             r'(?iu)(Перем|Знач|Новый|Возврат|Перейти|Продолжить|Прервать|Выполнить)\b|'
             # Условие Если
             r'(?i)(EndIf|If|Then|ElsIf|Else)\b|'
             r'(?iu)(КонецЕсли|Если|Тогда|ИначеЕсли|Иначе)\b|'
             # Циклы
             r'(?i)(EndDo|Do|For|Each|In|While|To)\b|'
             r'(?iu)(КонецЦикла|Цикл|Для|Каждого|Из|Пока|По)\b|'
             # Процедура и Функция
             r'(?i)(EndProcedure|Procedure|EndFunction|Function)\b|'
             r'(?iu)(КонецПроцедуры|Процедура|КонецФункции|Функция)\b|'
             # Попытка
             r'(?i)(EndTry|Try|Raise|Except)\b|'
             r'(?iu)(КонецПопытки|Попытка|ВызватьИсключение|Исключение)\b|'
             # Условия: И, Или, Не
             r'(?i)(And|Or|Not)\b|'
             r'(?iu)(И|Или|Не)\b'
             , Keyword.Reserved),
             # Литералы Истина, Ложь
             (r'(?i)(True|False|Null)\b|'
              r'(?iu)(Истина|Ложь)\b'
              , Literal),
        ]
    }
