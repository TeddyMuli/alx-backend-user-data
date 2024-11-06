#!/usr/bin/env python3
""" Module to filter logs
"""
import re


def filter_datum (fields, redaction, message, separator):
    """ Function to return the log message obfuscated
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
