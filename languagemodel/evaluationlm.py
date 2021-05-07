import string, re
import nltk
from nltk.lm import KneserNeyInterpolated
from nltk.lm import Vocabulary

class LanguageModel():
    def __init__(self):
        self.sentences = []
        self.model = None

        self.train_lm()

    def clean(self, sentence):
        sentence = sentence.strip().lower()
        sentence = sentence.strip(string.punctuation)
        sentence = sentence.replace('"', ' ').replace("!", ' ').replace('-', ' ').replace('@', ' ').replace('=',' ').replace(
            '?', ' ').replace(',', ' ').replace('.', ' ').replace('_', ' ').replace(';', ' ').replace(':', ' ').replace(
            ']', ' ').replace('[', ' ').replace('“', ' ').replace("'", ' ').replace('—', ' ').replace('(', ' ').replace(
            ')', ' ')
        sentence = re.sub(' +', ' ', sentence)

        return sentence

    def train_lm(self):

        with open('data/train.txt','r') as f:
            for line in f.readlines():
                if len(line.strip()) < 7: continue
                line = self.clean(line)
                line = line.split()
                self.sentences.append(line)

        n = 2
        train_data = [nltk.bigrams(t, pad_right=True, pad_left=True, left_pad_symbol="<s>", right_pad_symbol="</s>") for
                      t in self.sentences]
        words = [word for sent in self.sentences for word in sent]
        words.extend(["<s>", "</s>"])
        padded_vocab = Vocabulary(words)
        self.model = KneserNeyInterpolated(n)
        self.model.fit(train_data, padded_vocab)



def main():
    lm = LanguageModel()


if __name__ == "__main__":
    main()



