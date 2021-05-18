# Uniform and Cosine-Distance based Bi-Gram Language Model Generators for Passphrases

## Uniform Model Password Generator

Run the following to generate passwords using the uniform model on the customized dataset: <br />
`python preprocess.py ` <br />
`python similarities.py --use-uniform` <br />


Run the following to generate passwords using the uniform model on the Reuters News Corpus _(takes a while on a CPU)_: <br />
`python preprocess.py --use-reuters ` <br />
`python similarities.py --use-reuters --use-uniform` <br />

The output passphrases are generated in `languagemodel/data/output`

## Cosine-Distance Password Generator
Run the following to generate passwords using the cosine-distance model on the customized dataset: <br />
`python preprocess.py ` <br />
`python similarities.py ` <br />


Run the following to generate passwords using the cosine-distance model on the Reuters News Corpus: <br />
`python preprocess.py --use-reuters ` <br />
`python similarities.py --use-reuters` <br />

The output passphrases are generated in `languagemodel/data/output`

## Details

This repo contains code for the final term project for the ENLP Spring 2021 course at Georgetown. 

This project aims to generate memorable passphrases that are difficult to crack. 

The basic idea behind doing this, is to use a series of Bi-gram Language Models to generate sequences of tokens that fit any of the following patterns: <br />
`Adverb-Adjective-Noun-Noun` <br />
`Adverb-Adjective-Noun` <br />
`Adverb-Adjective` <br />
`Adjective-Noun` <br />

Language Models are usually estimated using counts of co-located words. The problem with using counts is, that counts reflect statistics of everyday usage. This could make it easier to crack a password built using a Language Model that is based on everyday distributions of words. <br /> <br />
To make the password less hackable, the probability distributions of the bigram language model are estimated instead using a **cosine-distance based measure**. If you want to generate a passphrase that is an adjective followed by a noun, a noun that is more distanced from the adjective is given more weight in the language model. This skews the language model into generating somewhat ludicrous yet grammatically correct sequences (you can try this out for yourself!)

#### Some more details follow:<br /> 
-Cosine-distance between words is calculated using the **gensim** package, with glove vectors based on the gigaword corpus ('glove-wiki-gigaword-100') <br />
-The **dataset** used for this project is a **collection of fictional works written by Lewis Carroll and Edward Lear**. This is in **data/train.txt**. The choice of the dataset is deliberate: the passphrases generated are happily more ludicrous and possibly more memorable as a result! <br />
-There is also the option to use the **Reuters News Corpus** from nltk's in-built corpora, to generate passphrases for the patterns above. This takes somewhat longer. <br />
-Passphrases are generated in the **data/output** folder. Four files are created, corresponding to the four patterns above. To keep in-line with the GU baseline system, tokens are separated by [! . @ - None]
