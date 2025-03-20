# analysis of test

from collections import Counter


def get_num_words(string):
    count = len(string.split())
    return count


def get_char_count(string):
    content = string.lower()
    char_count_dict = dict(Counter(content))
    return char_count_dict


def sorted_dicts(dictionary):
    pass