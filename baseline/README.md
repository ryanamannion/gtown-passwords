# Baseline System

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
	* To check, run `$ pwd`
* ensure your environment has any dependencies listed in `requirements.txt`:
	* Run `$ pip install -r requirements.txt`
* change any parameters you want in config.yml
	* To run `baseline.py` with a random config, run `python baseline.py -r`
* Options: `baseline.py [-h] [-c CONFIG] [-v VERBOSE] [-n NUMBER_OUT] [-r]`
* run `$ python baseline.py --help` for more info
