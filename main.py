# (c) en2si
# ударения v.1.0.
#
#
#
#
#
#
#
#
#
#
#
#
#
import urllib.request
from urllib.parse import unquote
from random import *
# GLOBALS!
words = []


def get():
    file_url = "https://raw.githubusercontent.com/humanly/stresses/main/base.txt"
    file = urllib.request.urlopen(file_url)

    for line in file:
        current = unquote(line)
        words.append(current[0:-1])
    # print(words)


def gen():
    while True:
        current = words[randint(0, len(words) - 1)]
        print(">", current.lower())
        answer = str(input("< "))
        if answer == current:
            print("> ok!")
        else:
            print("> no!", current)


if __name__ == '__main__':
    get()
    gen()
