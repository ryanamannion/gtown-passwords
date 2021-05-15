import re
import numpy as np
from nltk.corpus import wordnet as wn
from unidecode import unidecode
import random
import pykakasi

numwords = 5
special = False
capital = False

def convert_to_romaji(text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "a")        # Hiragana to ascii
    kakasi.setMode("K", "a")        # Katakana to ascii
    kakasi.setMode("J", "a")        # Japanese to ascii
    kakasi.setMode("r", "Hepburn")  # use Hepburn Roman table
    kakasi.setMode("s", True)       # add space
    kakasi.setMode("C", False)      # no capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)
    return result

code_list = sorted(wn.langs())
lang_list = ['albanian', 'arabic', 'bulgarian', 'catalan', ['chinese', 'mandarin'], 'danish', 'greek', 'english', 'basque', ['persian', 'farsi'], 'finnish', 'french', 'galician','hebrew', 'croatian', 'indonesian', 'italian', 'japanese', ['dutch', 'flemish'], 'bokmal', 'nynorsk', 'polish', 'portuguese', '???', 'slovenian', 'spanish', 'swedish', 'thai', 'malay']
lang_code = {}
for i in range(len(code_list)):
    if type(lang_list[i]) == list:
        for j in range(len(lang_list[i])):
            lang_code[lang_list[i][j]] = code_list[i]
    else:
        lang_code[lang_list[i]] = code_list[i]

def get_hypo(word):
    hypo_senses = []
    for sense in wn.synsets(word):
        hypo_senses.extend([i for i in sense.closure(lambda x:x.hyponyms())])
    hypo_senses = list(set(hypo_senses))
#    hypo_words = hypo_senses[np.random.randint(0, len(hypo_senses))].lemma_names()
    hypo_words = []
    for hypo_sense in hypo_senses:
        hypo_words.extend([i for i in hypo_sense.lemma_names()])
    hypo_words = list(set(hypo_words))
#    word = hypo_words[np.random.randint(0, len(hypo_words))]
    clean = []
    for word in hypo_words:
        clean.append(re.sub(r'[^a-zA-Z]', r'', word).lower())
    return clean

def get_l2(word, lang):
    senses = wn.synsets(word)
    hypo_senses = []
    for sense in wn.synsets(word):
        hypo_senses.extend([i for i in sense.closure(lambda x:x.hyponyms())])
    senses.extend(hypo_senses)
    l2_words = []
    for sense in senses:
        l2_words.extend(sense.lemma_names(lang_code[lang]))
#    while len(l2_words) == 0:
#        syn_index = np.random.randint(0, len(wn.synsets(word)))
#        l2_words = wn.synsets(word)[syn_index].lemma_names(lang_code[lang])
#    word_index = np.random.randint(0, len(l2_words))
    l2_words = list(set(l2_words))
    clean = []
    for word in l2_words:
        if lang == 'japanese':
            new_word = re.sub(r'[^a-zA-Z]', '', convert_to_romaji(word)).lower()
        else:
            new_word = re.sub(r'[^a-zA-Z]', '', unidecode(word)).lower()
        clean.append(new_word)
    return(clean)

"""
Password Generation
"""

def random_capital(word):
    new_word = ''
    index = np.random.randint(0, len(word))
    for i, char in enumerate(word):
        new_word += char.upper() if i == index else char
    return new_word

def special_char(word):
    new_word = ''
    convert = {'a':'@', 's':'$', 'i':'!', 'o':'0', 'e':'3', 'l':'|', 'c':'<', 'r':'&', 'x':'#'}
    for char in word:
        if char in convert.keys():
            new_char = convert[char] if random.random() >= 0.5 else char
        else:
            new_char = char
        new_word += new_char
    return new_word

def pass_gen(words, capital=False, special=False, numwords=0):
    if numwords==0:
        numwords=len(words)
    random.shuffle(words)
    new_words = []
    punc = ['.', ',', '*', '+', '-', '~', '&', '_']
    for word in words[:numwords]:
        new_word = word
        if capital:
            new_word = random_capital(new_word)
        if special:
            new_word = special_char(new_word)
        new_word = word[0].upper()
        new_word += word[1:]
        new_words.append(new_word)
    rand_punc = random.sample(punc, 1)[0]
    return rand_punc.join(new_words)

"""
def get_words():
    word = common_nouns[np.random.randint(0,len(common_nouns))]
    lang = ['spanish', 'french', 'chinese', 'japanese'][np.random.randint(0,4)]
    try:
        words = [word, get_hypo(word), get_l2(word, lang)]
        while words is None:
            words = get_words()
        return words
    except:
        words = get_words()
"""

def get_words(numwords, word=None, balance=False):
    if word == None:
        word = common_nouns[np.random.randint(0,len(common_nouns))]
    lang = ['spanish', 'french', 'chinese', 'japanese'][np.random.randint(0,4)]
    words = []
    l2 = get_l2(word, lang)
    hypo = get_hypo(word)
    if balance:
        for item in random.sample(l2, numwords//2):
            words.append(item)
        for item in random.sample(hypo, numwords//2):
            words.append(item)
    else:
        l2.extend(hypo)
        random.shuffle(l2)
        for item in random.sample(l2, numwords):
            words.append(item)
    return words

def main():
    words = get_words(numwords)
    return pass_gen(words, capital=capital, special=special, numwords=numwords)

def get_common_nouns():
    common_nouns_file = "common_nouns1000.txt"
    common_nouns = []
    with open(common_nouns_file, encoding='utf8') as f:
        raw = f.read()
        for line in raw.split('\n'):
            common_nouns.append(line)
    return common_nouns

if __name__ == '__main__':
    common_nouns = get_common_nouns()
    pass_list = []
    i = 0
    while i < 1000:
        i += 1
        try:
            pass_list.append(main())
        except:
            i -= 1
        print(i)

with open("Password_MinPairUpper.txt", 'w') as w:
    for item in pass_list:
        w.write(item)
        w.write('\n')