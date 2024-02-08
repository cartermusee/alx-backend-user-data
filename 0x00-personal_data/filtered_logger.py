#!/usr/bin/env python3
"""modeule for filter_datum"""
from typing import List
import re
import logging
from logging import StreamHandler


PII_FIELDS = ("name", "email", "address", "phone", "ssn")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor
        Keyword arguments:
        fields:represents all fields to obfuscate
        Return: return_description
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method to filter values in incoming log records
        """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    logger for user data
    with RedactingFormatter
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter()
    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
