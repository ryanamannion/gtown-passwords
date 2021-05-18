# User Input Model

	userinput/
	|
	|-- commoun_nouns1000.txt
	|-- user_input.py
	|-- sample_generator.py

This directory contains files for running the User Input Model. `user_input.py` is the model for users to run, and `sample_generator.py` was used to generate 1,000 samples for evaluation, and not designed for users to run. `common_nouns1000.txt` was only used as an imitation of user input. Because manually defining a user input 1,000 times was not realistic, a random word was selected from this list as a user input.

### Usage:
* Options: `user_input.py [-w --word] [-l --lang] [-n --numwords] [-c --capital] [-u --upper] [-s --special]`
  * For example, the version based on Glory et al. (2019) implementation will have two words with random upper case and number/ special character replacements, which will be specified as `user_input.py -w [YOUR FAVORITE WORD] -l [YOUR L2] -n 2 --upper --special`
* run `$ python user_input.py --help` for more info
