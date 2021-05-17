import math
import argparse
import os
import sys

from bientropy import bien
from bitstring import Bits


class PasswordEntropy():

    def __init__(self,passwordfile,type):

        self.sep = ['!', '.', '@', '-']

        self.passwordfile = passwordfile
        self.symbolset = set()
        self.entropytype = type # type of entropy, word-based or character based

        self.efflist = []
        self.adverbs = []
        self.adjectives = []
        self.nouns = []

        self.commonnouns = set()

        self.punc = ['.', ',', '*', '+', '-', '~', '&', '_']

        if type == 'vae' or type == 'userinput':
            self.populate_symbolset()

        if type != 'vae':
            self.populate_wordlists()


    def populate_symbolset(self):
        with open(self.passwordfile,'r') as f:
            for line in f.readlines():
                line = line.strip()
                self.symbolset.update(line)

    def populate_wordlists(self):

        with open('../baseline/eff_large_wordlist.txt','r') as r:
            for line in r.readlines():
                if line.strip() != '':
                    self.efflist.append(line.strip().split('\t')[1])
        with open('../languagemodel/data/adjectives.txt','r') as r:
            for line in r.readlines():
                if line.strip() != '':
                    self.adjectives.append(line.strip())
        with open('../languagemodel/data/adverbs.txt','r') as r:
            for line in r.readlines():
                if line.strip() != '':
                    self.adverbs.append(line.strip())
        with open('../languagemodel/data/nouns.txt','r') as r:
            for line in r.readlines():
                if line.strip() != '':
                    self.nouns.append(line.strip())

        with open('../userinput/common_nouns1000.txt','r') as r:
            for line in r.readlines():
                if line.strip() != '':
                    self.commonnouns.add(line.strip())



    def calculate_password_entropy(self):
        with open(self.passwordfile.replace('.csv','.evaluated.csv').replace('.txt','.evaluated.txt'),'w') as f:
            with open(self.passwordfile,'r') as r:
                for line in r.readlines():
                    line = line.strip()
                    if line != '':

                        if  self.entropytype=='vae':

                            entropy = math.log(math.pow(len(self.symbolset),len(line)),2)
                            bientropy = bien(Bits(bytearray(line,'utf-8')))
                            f.write(line + ',' + str(entropy) + ',' + str(bientropy) +  '\n')

                        elif self.entropytype == 'userinput':
                            """
                            The basic approach is to find words from each password and calc the password entropy on the words, 
                            then a password entropy on the remaining characters
                            
                            There are too many hyponyms, spanish, japanese, french, chinese words. We'll assume a blanket character entropy setup. 
                            """

                            l = []
                            temp = line
                            entropy = 1

                            for sep in self.punc:
                                if sep in line:
                                    l = line.split(sep)
                                    break

                            if len(l) == 0:
                                for word in self.commonnouns:
                                    if word.lower() in temp.lower():
                                        entropy *= len(self.commonnouns)
                                        temp = temp.replace(word,'')
                                        if temp == '': break

                                if len(temp) > 0:
                                    entropy *= math.pow(len(self.symbolset),len(temp))

                            else:

                                for word in l:
                                    if word.lower() in [x.lower() for x in self.commonnouns]:
                                        entropy *= len(self.commonnouns)
                                    else:
                                        entropy *= math.pow(len(self.symbolset),len(word))

                            bientropy = bien(Bits(bytearray(line, 'utf-8')))
                            f.write(line + ',' + str(math.log(entropy,2)) + ',' + str(bientropy) + '\n')


                        elif self.entropytype == 'baseline':

                            # need to check how many words in the phrase.
                            l = []
                            for sep in self.sep:
                                if sep in line:
                                    l = line.split(sep)
                                    break

                            # Handles the None separator case. Assumes 5 words default.
                            if len(l) == 0:
                                entropy = math.log(math.pow(len(self.efflist), 5), 2)
                            else:
                                entropy = math.log(math.pow(len(self.efflist), len(l)), 2)

                            bientropy = bien(Bits(bytearray(line,'utf-8')))
                            f.write(line + ',' + str(entropy) + ',' + str(bientropy) + '\n')

                        else: # language model

                            if 'adv_adj_noun_noun' in self.passwordfile.lower():
                               entropy = math.log(
                                   len(self.adverbs) * len(self.adjectives) * len(self.nouns) * len(self.nouns), 2)
                            elif 'adv_adj_noun' in self.passwordfile.lower():
                               entropy = math.log(len(self.adverbs) * len(self.adjectives) * len(self.nouns), 2)
                            elif 'adv_adj' in self.passwordfile.lower():
                               entropy = math.log(len(self.adverbs) * len(self.adjectives), 2)
                            else:
                               entropy = math.log(len(self.adjectives) * len(self.nouns), 2)


                            bientropy = bien(Bits(bytearray(line, 'utf-8')))
                            f.write(line + ',' + str(entropy) + ',' + str(bientropy) + '\n')


        sys.stdout.write('Password Entropies calculated in a new file:' + self.passwordfile.replace('.csv','.evaluated.csv').replace('.txt','.evaluated.txt') + '\n')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--password-file', type=str, default='../baseline/examples/baseline_all.txt',
                        help='password file to calculate password entropy')
    parser.add_argument('--model-type', type=str,
                        help='model type. One of userinput,vae,baseline,lm')

    args = parser.parse_args()

    if not os.path.isfile(args.password_file):
        sys.stdout.write('Invalid file supplied. System will now exit.' + '\n')
        return

    if args.model_type is None:
        sys.stdout.write('Supply a model type. One of userinput,vae,baseline,lm' + '\n')
        return


    entropy = PasswordEntropy(passwordfile=args.password_file,type=args.model_type)
    entropy.populate_symbolset()
    entropy.calculate_password_entropy()




if __name__ == "__main__":
    main()