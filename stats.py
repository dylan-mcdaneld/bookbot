# analysis of test

from collections import Counter


def get_num_words(string):
    count = len(string.split())
    return count


def get_char_count(string):
    content = string.lower()
    char_count_dict = dict(Counter(content))
    return char_count_dict


def sorted_dicts(character_counts):
    # sub function to get the count values
    def sort_on(dict):
        return dict["count"]

    sorted = []
    for char, count in character_counts.items():
        sorted.append({"character":char, "count":count})

    # sort list of dicts hight to low, by count
    sorted.sort(reverse=True, key=sort_on)
    # print(sorted)
    return sorted