#! /usr/bin/python3

import words
import argparse

parser = argparse.ArgumentParser(description='Process some chars.')
parser.add_argument('desired_chars', metavar='N', type=str, nargs='+',
                                        help='all chars you want in the word')


args = parser.parse_args()
desired_chars = set(args.desired_chars)

print("Showing results for desired alphabets:")
print(desired_chars)

for word in words.words:
    has_all = True
    for ch in desired_chars:
        if ch.upper() not in word:
            has_all = False
    if has_all:
        print(word)
