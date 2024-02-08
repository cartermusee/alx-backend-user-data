#!/usr/bin/env python3
"""modeule for filter_datum"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """the function filter_datum
    that returns the log message obfuscated:
    Keyword arguments:
    fields: represents all fields to obfuscate
    redaction:represents by what the field will be obfuscated
    message: a string representing the log line
    separator: separating all fields in the log line (message)
    Return: he log message obfuscated:
    """
    for key in fields:
        pattern = r'({0}=)[^{1}]*({1})'.format(key, separator)
        message = re.sub(pattern, r'\1{}\2'.format(redaction), message)
    return message
