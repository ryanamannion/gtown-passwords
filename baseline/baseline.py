#!/usr/bin/env python3
"""
baseline.py

this file acts as the Georgetown baseline and is meant to be a clone of the new
passphrase system based on information given to us by the Chief engineer of UIS

USAGE:
    $ python baseline.py path_to_config.yml
"""
import sys
import yaml
import random


def load_words(filepath):
    """
    loads dice words and returns list of tuples (dice_num, word)
    """

    with open(filepath, 'r') as f:
        words_raw = f.readlines()
        dice_words = [tuple(line.strip('\n').split('\t')) for line in words_raw]

    return dice_words


def roll(n=5):
    """
    Returns string of random integers [1,6] of len n
    :param n: length of resulting string
    :return: string of integers of len()==n
    """
    this_roll = []
    for _ in range(n):
        this_roll.append(random.randint(1, 6))
    return "".join(this_roll)


def generate(len_range_low, len_range_high, num_words, sep):
    """

    :param len_range_low: int, shortest possible passphrase
    :param len_range_high: int, longest possible passphrase
    :param num_words: int, number of words to generate in passphrase
    :param sep: str, character to separate words
    :return passphrase: str, resulting passphrase
    """
    ...


if __name__ == "__main__":
    config_path = sys.argv[1]
    with open(config_path, 'r') as configfile:
        config = yaml.safe_load(configfile)

    load_words(config['words'])

    print(generate(**config['output']))
