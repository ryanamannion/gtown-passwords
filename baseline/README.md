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

## Dice Words List

This version of the Dice Words list was sourced from the Electronic Frontier Foundation, see
https://www.eff.org/dice for more information and additional wordlists.

This could be easily re-implemented to accomodate other langugaes or wordlists. The file containts a 5 integers from
1-6 (incl, like a dice roll), then a tab ('\t') and a word. Each entry is separated by a newline ('\n').

To use a new wordlist, simply specify its location in `config.yml`

## `config.yml`

`config.yml` handles the configuration of `baseline.py`. In it are defined:

Static Params: Georgetown's users cannot change these
* the path to the wordlist file
* the length range of the resulting password
* the number of words to generate

Dynamic Params: Georgetown's users can change these
* toggle to capitalize first letter of each word
* the separator to place between each word, from the set of `[".", "!", "-", "@", None]`

NOTE: the dynamic params can be overridden at runtime with the `-r` option, which uses python's `random` 
to choose the params each time a new password is generated. This is especially useful if you want to
generate a large number of passwords with the `-n` option
