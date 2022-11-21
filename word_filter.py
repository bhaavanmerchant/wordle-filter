#! /usr/bin/python

import words

desired_chars = {'a', 'i', 'm'}
#desired_chars = {'s', 'n', 'e', 'a'}

for word in words.words:
    has_all = True
    for ch in desired_chars:
        if ch.upper() not in word:
            has_all = False
    if has_all:
        print(word)
