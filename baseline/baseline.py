#!/usr/bin/env python3
"""
baseline.py

this file acts as the Georgetown baseline and is meant to be a clone of the new
passphrase system based on information given to us by the Chief engineer of UIS

BASIC USAGE (config.yml must be in same dir):
    $ python baseline.py -r

FOR MORE USAGE NOTES:
    $ python baseline.py --help
"""
import sys
import yaml
import random
import argparse


def load_words(filepath):
    """
    loads dice words from file and returns dict of number: word
    """

    with open(filepath, 'r') as f:
        dice_words = {}
        for line in f.readlines():
            line = line.rstrip("\n")
            num, word = line.split('\t')
            dice_words[num] = word

    return dice_words


def roll(n=5):
    """
    Returns string of random integers [1,6] of len n

    :param n: length of resulting string
    :return: string of integers of len()==n
    """
    this_roll = []
    for _ in range(n):
        this_roll.append(str(random.randint(1, 6)))
    return "".join(this_roll)


def generate(words, len_range_low, len_range_high, num_words, cap_words, sep,
             verbose=False):
    """
    Generates passphrase

    :param words: str, path to file containing dicewords list
    :param len_range_low: int, len of shortest possible passphrase
    :param len_range_high: int, len of longest possible passphrase
    :param num_words: int, number of words to generate
    :param sep: str, character to separate words
    :param verbose: bool, prints verbose output
    :return passphrase: str, resulting passphrase
    """
    if verbose:
        print("Loading words list...", end=" ", flush=True)
    words_dict = load_words(words)
    if verbose:
        print("Done")

    # separators contribute to the length of the phrase, adjust for that
    num_sep = num_words - 1
    if sep == 'None' or sep is None:
        sep = ''
    sep_chars = num_sep * len(sep)
    len_range = ((len_range_low - sep_chars), (len_range_high - sep_chars))

    def gen():
        rolled_words = []
        words_len = 0
        if verbose:
            print("Attempt:")
        for i in range(num_words):
            # roll dice and lookup word
            num = roll()
            word = words_dict[num]
            if verbose:
                print(f"\tRoll: {num} --> {word}")
            # lookup word and append to list
            rolled_words.append(word)
            # update overall len
            words_len += len(word)
        else:
            if not len_range[0] <= words_len <= len_range[1]:
                if verbose:
                    print(f"\tFailed attempt: len == {words_len + sep_chars}")
                # recursion, try again
                gen()
            if cap_words:
                rolled_words = [w.capitalize() for w in rolled_words]
            return sep.join(rolled_words)

    passphrase = gen()
    return passphrase


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, default='config.yml',
                        help='path to config file in yaml format')
    parser.add_argument('-v', '--verbose', type=bool, default=False,
                        help='verbose output')
    parser.add_argument('-n', '--number-phrases', type=int, default=1,
                        dest="number_out",
                        help="number of passphrases to return")
    parser.add_argument('-r', '--random', action="store_true",
                        help="selects random parameters for each passphrase")
    args = parser.parse_args()

    with open(args.config, 'r') as configfile:
        config = yaml.safe_load(configfile)

    for _ in range(args.number_out):
        if args.random:
            # change config['cap_words']    one of two options
            # change config['sep']          one of five options
            caps = [True, False]
            seps = [".", "!", "-", "@", None]
            rand_caps = caps[random.randint(0, 1)]
            rand_sep = seps[random.randint(0, 4)]
            config['cap_words'] = rand_caps
            config['sep'] = rand_sep
        phrase = generate(**config, verbose=args.verbose)
        print(phrase)
