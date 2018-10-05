"""Some useful pre-processing functions"""
import os
import re

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"

USER_PATH = os.path.expanduser('~')
CORPUS_PATH = os.path.join(USER_PATH, "cltk_data", "old_norse", "text", "old_norse_texts_heimskringla")


def remove_punctuations(text):
    res = text
    if re.match(r"[0-9]+\.", text) is None:
        res = re.sub("[\-:?;.,]", "", res)
    res = re.sub("z", "s", res)
    res = re.sub("x", "ks", res)
    res = re.sub(r" +", " ", res)
    return res
