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

# Setup & Installation

To setup a conda environment to run the models, try the following: <br />
1. Install Anaconda. Python 3.8 distribution recommended. <br />
2. Run the following to create an environment and install all dependencies: <br />
   `conda env create -f gtown-passwords.yml` <br />
   `conda activate gtown-passwords` <br />
   
  Note, this installs the **CPU version of PyTorch** for the LSTM-language model.

# Disclaimers

**The owners, and original co-contributors of this repository will assume no liabilities** resulting from any use of this repository by any party, entity, person, groups of persons, groups of entities, or any other body or collective that is not the original owner or original co-contributor of this repository. By using this repository in any form, **you the user alone will be liable for any and all liabilities incurred by yourself for any and all uses that you have actioned**. 
