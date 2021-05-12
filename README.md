# Different Approaches to Memorable Passphrase Generation
This repo holds code for a final project in an ENLP class. The project is about creating a more memorable passphrase generation system

# baseline
	baseline/
	|
	|-- requirements.txt
	|-- baseline.py
	|-- config.yml
	|-- eff_large_wordlist.txt
	|-- baseline-sample-pass.txt

	
This directory contains files for running the clone of Georgetown's baseline password system. This is NOT the
exact system, but instead a recreation made to the best of our knowledge of how Georgetown's system works. 

### Usage:
* ensure your working directory is `baseline/`
	* to check run `$ pwd`
* ensure your environment has any dependencies listed in `requirements.txt`:
	* Run `$ pip install -r requirements.txt`
* change any parameters you want in config.yml
* `baseline.py [-h] [-c CONFIG] [-v VERBOSE] [-n NUMBER_OUT]`
* run `$ python baseline.py --help` for more info

# languagemodel

[This directory](https://github.com/ryanamannion/gtown-passwords/tree/main/languagemodel) contains files for the first language model generator type, the **cosine-distance based bi-gram language model generator**. Please see the README in this folder for more details.

The second language model generator type (LSTM-based language model) is too big to fit in this repo (as it is forked from pytorch/examples), and can be found [here](https://github.com/nitinvwaran/examples/tree/master/word_language_model)
