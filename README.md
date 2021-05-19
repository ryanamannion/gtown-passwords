# Different Approaches to Memorable Passphrase Generation
This repo holds code for a final project in an ENLP class. The project is about creating a more memorable passphrase generation system

# baseline

[This directory](https://github.com/ryanamannion/gtown-passwords/tree/main/baseline) contains files for the baseline Georgetown system.
This system is **NOT** the actual system run by Georgetown University, it is a close-as-possible recreation for benchmarking purposes.

Please see [the README](https://github.com/ryanamannion/gtown-passwords/blob/main/baseline/README.md) for more information. 

# languagemodel

[This directory](https://github.com/ryanamannion/gtown-passwords/tree/main/languagemodel) contains files for the **uniform model bi-gram language model generator** and the **cosine-distance based bi-gram language model generator**. Please see the README in this folder for more details.

The second language model generator type (LSTM-based language model) is too big to fit in this repo (as it is forked from pytorch/examples), and can be found [here](https://github.com/nitinvwaran/examples/tree/master/word_language_model)

# userinput

[This directory](https://github.com/ryanamannion/gtown-passwords/tree/main/userinput) contains files for a memorability-enhanced password generator that takes user inputs and generates passwords semantically related to the input.

# autoencoder

[This directory](https://github.com/ryanamannion/gtown-passwords/tree/main/autoencoder) contains files for a standard and a variational autoencoder. Please see the [README]((https://github.com/ryanamannion/gtown-passwords/tree/main/autoencoder/README.md) file for more details.

# evaluation

Two evaluation metrics are used: <br />
1. The **password entropy** is calculated using the formulae from [this link](https://generatepasswords.org/how-to-calculate-entropy/)

For the baseline and language models, static wordlists were used to calculate the password entropy in bits. <br />
For the auto-encoder model, static character-set lists derived from the training data passwords were used to calculate the password entropy in bits <br />
For the user input model, a combination of the static 1000 common nouns wordlist, and character-set lists were used, as the model uses non-static wordlists from WordNet, to incorporate non-English language words and hyponyms. The password entropies for this model may be sligtly inflated as a result of not having non-static wordlists <br />

2. **The Binary Entropy metric**, which calculates the Entropy of a binary string. Strings are converted to binary strings and the entropy is calculated as the weighted average of the Shannon entropy and the entropy of the (n-1) derivatives of the binary string. For more information, please see [this link](https://pypi.org/project/BiEntropy/) 

The Binary entropy may give a generalizeable measure as it uses binary strings for the Entropy measures, and facilitates comparisons with non-traditional passwords.

To run an evaluation on a txt or csv file with one column of passwords, run the following from the **evaluation** folder: <br />
`python entropy.py --password-file <location_of_txt_csv_file> --model-type <userinput,vae,baseline,lm>` <br />

The model type is one of the following. Supply this as an additional input to tell the script what type of model generated the file: <br />
`userinput`: The user-input model <br />
`vae`: Variational Auto-Encoder <br />
`baseline`: Baseline  <br />
`lm`: Language Model <br />


# Setup & Installation

To setup a conda environment to run the models, try the following: <br />
1. Install Anaconda. Python 3.8 distribution recommended. <br />
2. Run the following to create an environment and install all dependencies: <br />
   `conda env create -f gtown-passwords.yml` <br />
   `conda activate gtown-passwords` <br />
   
  Note, this installs the **CPU version of PyTorch** for the LSTM-language model.

# Disclaimers

**The owners, and original contributors of this repository will assume no liabilities nor damages** resulting from any use of this repository by any party, entity, person, groups of persons, groups of entities, or any other body or collective that is not the original owner or original contributor of this repository. By using this repository in any form, **you the user alone will be liable for any and all liabilities and damages incurred by yourself for any and all uses that you have actioned**. 
