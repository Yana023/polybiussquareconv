#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: Yana

import re
import sys
import string


I_SYMBOL = '(IJ)'
POLYBIUS_SQUARE = [c if c != 'I' else I_SYMBOL for c in string.ascii_uppercase if c != 'J']


def ispolybius(code: str) -> bool:
    return bool(re.match(r'^([1-5\*]{2} *)+$', code))

def conv(char: str) -> str:
    try:
        if char in ['I', 'J']:
            val = POLYBIUS_SQUARE.index(I_SYMBOL)
        else:
            val = POLYBIUS_SQUARE.index(char)
    except ValueError:
        return "**"
    return "%d%d" % (val / 5 + 1, val % 5 + 1)

def decode(code: str) -> str:
    code_normalized = code.replace(' ', '')
    ret = ""
    for i in range(0, len(code_normalized), 2):
        if code_normalized[i] == "*":
            ret += "*"
        else:
            c_up = int(code_normalized[i]) - 1
            c_dn = int(code_normalized[i + 1]) - 1
            ret += POLYBIUS_SQUARE[c_up * 5 + c_dn]
    return ret

def encode(code: str) -> str:
    code_normalized = code.replace(' ', '').upper()
    return ' '.join([conv(c) for c in code_normalized])


if __name__ == '__main__':
    words = sys.argv[1]
    if ispolybius(words):
        print("Decode: %s => %s" % (words, decode(words)))
    else:
        print("Encode: %s => %s" % (words, encode(words)))
