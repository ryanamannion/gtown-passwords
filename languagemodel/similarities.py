import random, math
import gensim.downloader as api
import numpy as np
import os
import argparse
import nltk

from evaluationlm import LanguageModel
from scipy.special import softmax
from tqdm import tqdm


class Similarity():
    def __init__(self,usereuters=False,wordcount=1000,useuniform=False):
        self.adjnoun = None
        self.nounnoun = None
        self.advadj = None

        self.adverbs = []
        self.nouns = []
        self.adjectives = []

        self.wordvectors = api.load("glove-wiki-gigaword-100")
        self.usereuters = usereuters
        self.separator = ['!', '@', '.', '-', '']

        self.wordcount = wordcount
        self.useuniform = useuniform

        self.evallm = LanguageModel()


    def initialize_models(self):
        """
        gets data and initializes the language model matrices
        """

        with open('data/adverbs.txt','r') as r:
            for adverb in r.readlines():
                self.adverbs.append(adverb.strip())
        self.adverbs.sort()

        with open('data/adjectives.txt','r') as r:
            for adj in r.readlines():
                self.adjectives.append(adj.strip())
        self.adjectives.sort()

        with open('data/nouns.txt','r') as r:
            for noun in r.readlines():
                self.nouns.append(noun.strip())

        self.nouns.sort()

        self.adjnoun = np.zeros((len(self.adjectives),len(self.nouns)),dtype=np.float16)
        self.advadj = np.zeros((len(self.adverbs),len(self.adjectives)),dtype=np.float16)
        self.nounnoun = np.zeros((len(self.nouns),len(self.nouns)),dtype=np.float16)

    def populate_models(self):

        if self.useuniform == False:

            """
            use cosine-distance based probabilities
            """

            print('Using cosine-distance probabilities')

            for i in tqdm(range(0,len(self.adverbs))):
                for j in range(0,len(self.adjectives)):
                    try:
                        self.advadj[i][j] = self.wordvectors.distance(self.adverbs[i],self.adjectives[j])
                    except Exception as e:
                        self.advadj[i][j] = 1

            for i in tqdm(range(0,len(self.adjectives))):
                for j in range(0,len(self.nouns)):
                    try:
                        self.adjnoun[i][j] = self.wordvectors.distance(self.adjectives[i],self.nouns[j])
                    except Exception as e:
                        self.adjnoun[i][j] = 1


            for i in tqdm(range(0,len(self.nouns))):
                for j in range(0,len(self.nouns)):
                    try:
                        self.nounnoun[i][j] = self.wordvectors.distance(self.nouns[i],self.nouns[j])
                    except Exception as e:
                        self.nounnoun[i][j] = 1

        else:

            print ('Using uniform probabilities')

            """
            uniform probabilities - baseline
            """

            uadj = 1 / len(self.adjectives)
            unoun = 1 / len(self.nouns)

            for i in tqdm(range(0,len(self.adverbs))):
                for j in range(0,len(self.adjectives)):
                    self.advadj[i][j] = uadj

            for i in tqdm(range(0,len(self.adjectives))):
                for j in range(0,len(self.nouns)):
                    self.adjnoun[i][j] = unoun

            for i in tqdm(range(0,len(self.nouns))):
                for j in range(0,len(self.nouns)):
                    self.nounnoun[i][j] = unoun

        self.adjnoun = softmax(self.adjnoun, axis=1)
        for row in self.adjnoun:
            assert round(float(np.sum(row)), 0) == float(1)

        self.nounnoun = softmax(self.nounnoun, axis=1)
        for row in self.nounnoun:
            assert round(float(np.sum(row)), 0) == float(1)

        self.advadj = softmax(self.advadj, axis=1)
        for row in self.advadj:
            assert round(float(np.sum(row)), 0) == float(1)

        if self.usereuters == True:
            np.save('models/reuters_nounnoun', self.nounnoun)
        else:
            np.save('models/poem_nounnoun', self.nounnoun)

        if self.usereuters == True:
            np.save('models/reuters_adjnoun', self.adjnoun)
        else:
            np.save('models/poem_adjnoun', self.adjnoun)

        if self.usereuters == True:
            np.save('models/reuters_advadj', self.advadj)
        else:
            np.save('models/poem_advadj', self.advadj)


    def generate(self):

        """
        Adv-Adj-Noun-Noun combo
        """
        if self.usereuters == True:
            if os.path.isfile('models/reuters_nounnoun.npy'):
                self.nounnoun = np.load('models/reuters_nounnoun.npy')
                self.adjnoun = np.load('models/reuters_adjnoun.npy')
                self.advadj = np.load('models/reuters_advadj.npy')
            else:
                self.populate_models()
        else:
            if os.path.isfile('models/poem_nounnoun.npy'):
                self.nounnoun = np.load('models/poem_nounnoun.npy')
                self.adjnoun = np.load('models/poem_adjnoun.npy')
                self.advadj = np.load('models/poem_advadj.npy')
            else:
                self.populate_models()


        with open('data/output/adv_adj_noun_noun.txt','w') as out:
            for x in range(0,self.wordcount):
                sep = self.separator[int(random.uniform(0,len(self.separator)))]
                advindex = math.floor(random.uniform(0, len(self.adverbs)))
                adjindex = np.random.choice(len(self.adjectives), 1, p=np.squeeze(self.advadj[advindex]))[0]
                nounindex = np.random.choice(len(self.nouns), 1, p=np.squeeze(self.adjnoun[adjindex]))[0]
                nounindex2 = np.random.choice(len(self.nouns), 1, p=np.squeeze(self.nounnoun[nounindex]))[0]

                st = []
                st.append([self.adverbs[advindex],self.adjectives[adjindex],self.nouns[nounindex],self.nouns[nounindex2]])

                test = [nltk.bigrams(t, pad_right=True, pad_left=True, left_pad_symbol="<s>",
                                     right_pad_symbol="</s>") for t in st]
                for _, t in enumerate(test):
                    entropy = math.log(self.evallm.model.perplexity(t), 2)

                out.write(self.adverbs[advindex] + sep + self.adjectives[adjindex] + sep + self.nouns[nounindex] + sep + self.nouns[nounindex2] + ',' + str(entropy) + '\n')


        """
        Adv-adj-noun
        """
        with open('data/output/adv_adj_noun.txt','w') as out:
            for x in range(0,self.wordcount):
                sep = self.separator[int(random.uniform(0, len(self.separator)))]
                advindex = math.floor(random.uniform(0, len(self.adverbs)))
                adjindex = np.random.choice(len(self.adjectives), 1, p=np.squeeze(self.advadj[advindex]))[0]
                nounindex = np.random.choice(len(self.nouns), 1, p=np.squeeze(self.adjnoun[adjindex]))[0]

                st = []
                st.append(
                    [self.adverbs[advindex], self.adjectives[adjindex], self.nouns[nounindex]])

                test = [nltk.bigrams(t, pad_right=True, pad_left=True, left_pad_symbol="<s>",
                                     right_pad_symbol="</s>") for t in st]
                for _, t in enumerate(test):
                    entropy = math.log(self.evallm.model.perplexity(t), 2)

                out.write(self.adverbs[advindex] + sep + self.adjectives[adjindex] + sep + self.nouns[nounindex] + ',' + str(entropy) +  '\n')

        """
        Adv-Adj
        """
        with open('data/output/adv_adj.txt', 'w') as out:
            for x in range(0, self.wordcount):
                sep = self.separator[int(random.uniform(0, len(self.separator)))]
                advindex = math.floor(random.uniform(0, len(self.adverbs)))
                adjindex = np.random.choice(len(self.adjectives), 1, p=np.squeeze(self.advadj[advindex]))[0]

                st = []
                st.append(
                    [self.adverbs[advindex], self.adjectives[adjindex]])

                test = [nltk.bigrams(t, pad_right=True, pad_left=True, left_pad_symbol="<s>",
                                     right_pad_symbol="</s>") for t in st]
                for _, t in enumerate(test):
                    entropy = math.log(self.evallm.model.perplexity(t), 2)

                out.write(self.adverbs[advindex] + sep + self.adjectives[adjindex] + ',' + str(entropy) +  '\n')

        """
        Adj-Noun
        """
        with open('data/output/adj_noun.txt', 'w') as out:
            for x in range(0, self.wordcount):
                sep = self.separator[int(random.uniform(0, len(self.separator)))]
                adjindex = math.floor(random.uniform(0, len(self.adjectives)))
                nounindex = np.random.choice(len(self.nouns), 1, p=np.squeeze(self.adjnoun[adjindex]))[0]

                st = []
                st.append(
                    [self.adjectives[adjindex], self.nouns[nounindex]])

                test = [nltk.bigrams(t, pad_right=True, pad_left=True, left_pad_symbol="<s>",
                                     right_pad_symbol="</s>") for t in st]
                for _, t in enumerate(test):
                    entropy = math.log(self.evallm.model.perplexity(t), 2)

                out.write(self.adjectives[adjindex] + sep + self.nouns[nounindex] + ',' + str(entropy) +  '\n')




def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--use-reuters', action='store_true',
                        help='use reuters dataset')
    parser.add_argument('--use-uniform', action='store_true',
                        help='use uniform distribution')
    parser.add_argument('--words', type=int, default='1000',
                        help='number of passwords to generate')

    args = parser.parse_args()

    sim = Similarity(usereuters=args.use_reuters,wordcount=args.words,useuniform=args.use_uniform)
    sim.initialize_models()
    sim.generate()



if __name__ == "__main__":
    main()



