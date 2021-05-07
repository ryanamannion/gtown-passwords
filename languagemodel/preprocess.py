import nltk
import string, re, shutil,os
import argparse

nltk.download('reuters')
nltk.download('words')

import stanza
from nltk.corpus import reuters
from tqdm import tqdm

class Preprocess():
    def __init__(self,usereuters=False):

        shutil.rmtree('models')
        os.mkdir('models')

        stanza.download('en')
        self.files = reuters.fileids()
        self.nlp = stanza.Pipeline(lang='en',processors='tokenize,mwt,pos')
        self.adverbs = set()
        self.adjectives = set()
        self.nouns = set()

        self.usereuters = usereuters

        self.wordlist = set(w.lower() for w in nltk.corpus.words.words())

        if self.usereuters == False:
            with open('data/train.txt','r') as f:
                for line in f.readlines():
                    if len(line.strip()) < 7: continue
                    line = self.clean(line)
                    line = line.split()
                    self.wordlist.update(line)

    def clean(self,sentence):
        sentence = sentence.strip().lower()
        sentence = sentence.strip(string.punctuation)
        sentence = sentence.replace('"',' ').replace("!",' ').replace('-',' ').replace('@',' ').replace('=',' ').replace('?',' ').replace(',',' ').replace('.',' ').replace('_',' ').replace(';',' ').replace(':',' ').replace(']',' ').replace('[',' ').replace('“',' ').replace("'",' ').replace('—',' ').replace('(',' ').replace(')',' ')
        sentence = re.sub(' +',' ',sentence)

        return sentence


    def create_wordlists(self,sentence):

        doc = self.nlp(sentence)

        for sent in doc.sentences:
            for i in range(0,len(sent.words)):
                if sent.words[i].upos == 'ADV':
                    if sent.words[i].text.lower().strip() in self.wordlist and len(sent.words[i].text.strip()) > 3:
                        self.adverbs.add(sent.words[i].text.lower())

                if sent.words[i].upos == 'ADJ':
                    if sent.words[i].text.lower().strip() in self.wordlist and len(sent.words[i].text.strip()) > 3:
                        self.adjectives.add(sent.words[i].text.lower())

                if sent.words[i].upos == 'NOUN':
                    if sent.words[i].text.lower().strip() in self.wordlist and len(sent.words[i].text.strip()) > 3:
                        self.nouns.add(sent.words[i].text.lower())

    def parse_files(self):

        if self.usereuters == True:
            for file in tqdm(self.files):
                cache = []
                for word in reuters.words(file):
                    if word != '.':
                        cache.append(word.lower())
                    else:
                        self.create_wordlists(' '.join(cache))
                        cache = []
            if len(cache) > 0:
                self.create_wordlists(' '.join(cache))
        else:
            with open('data/train.txt','r') as f:
                for line in tqdm(f.readlines()):
                    if len(line.strip()) < 7: continue
                    line = self.clean(line)
                    self.create_wordlists(line)

        with open('data/adverbs.txt','w') as out:
            for s in self.adverbs:
                out.write(s + '\n')

        with open('data/adjectives.txt','w') as out:
            for s in self.adjectives:
                out.write(s + '\n')

        with open('data/nouns.txt','w') as out:
            for s in self.nouns:
                out.write(s + '\n')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--use-reuters', action='store_true',
                        help='use reuters dataset')

    args = parser.parse_args()

    preprocess = Preprocess(usereuters=args.use_reuters)
    preprocess.parse_files()

if __name__ == "__main__":
    main()

