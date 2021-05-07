# Different Approaches to Memorable Passphrase Generation
This repo holds code for a final project in an ENLP class. The project is about creating a more memorable passphrase generation system

# baseline
	baseline/
	|
	|-- baseline.py
	|-- config.yml
	|-- baseline-sample-pass.txt

	
[This directory](https://github.com/ryanamannion/gtown-passwords/tree/main/languagemodel) contains files for running the clone of Georgetown's baseline password system. This is NOT the
exact system, but instead a recreation made to the best of our knowledge of how Georgetown's system works. 

### Usage:
* change any params you want in config.yml
* `baseline.py [-h] [-c CONFIG] [-v VERBOSE] [-n NUMBER_OUT]`
* run `python baseline.py --help` for more info

# data (for baseline)
	data/
	|
	|-- eff_large_wordlist.txt

### EFF Wordlist
source: https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

# languagemodel

This directory contains files for the first language model generator type, the **cosine-distance based bi-gram language model generator**. Please see the README in this folder for more details.

The second language model generator type (LSTM-based language model) is too big to fit in this repo (as it is forked from pytorch/examples), and can be found [here](https://github.com/nitinvwaran/examples/tree/master/word_language_model)
