# gtown-passwords
This repo holds code for a final project in an ENLP class. The project is about creating a better passphrase generation system

# baseline
	```
	baseline/
	|
	|-- baseline.py
	|-- config.yml
	```
	
This directory contains files for running the clone of Georgetown's baseline password system. This is NOT the
exact system, but instead a recreation made to the best of our knowledge of how Georgetown's system works. 

### Usage:
* change any params you want in config.yml, they are set to Georgetown's params by default
* `baseline.py [-h] [-c CONFIG] [-v VERBOSE] [-n NUMBER_OUT]`
* run `python baseline.py --help` for more info

# data

source: https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt