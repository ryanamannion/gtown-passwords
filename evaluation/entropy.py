import math
import argparse
import os
import sys

from bientropy import bien
from bitstring import Bits

class PasswordEntropy():
    def __init__(self,passwordfile,type='char'):
        self.passwordfile = passwordfile
        self.symbolset = set()
        self.entropytype = type # type of entropy, word-based or character based

    def populate_symbolset(self):
        with open(self.passwordfile,'r') as f:
            for line in f.readlines():
                line = line.strip()
                #if ',' in line:
                #    line = line.split(',')[0]
                self.symbolset.update(line)

    def calculate_password_entropy(self):
        with open(self.passwordfile.replace('.csv','.evaluated.csv').replace('.txt','.evaluated.txt'),'w') as f:
            with open(self.passwordfile,'r') as r:
                for line in r.readlines():
                    line = line.strip()
                    if line != '':
                        if self.entropytype == 'char':
                            #if ',' in line:
                            #    l = line.split(',')[0]
                            #else:
                            #    l = line
                            entropy = math.log(math.pow(len(self.symbolset),len(line)),2)
                            bientropy = bien(Bits(bytearray(line,'utf-8')))


                            f.write(line + ',' + str(entropy) + ',' + str(bientropy) +  '\n')

        sys.stdout.write('Password Entropies calculated in a new file:' + self.passwordfile.replace('.csv','.evaluated.csv').replace('.txt','.evaluated.txt') + '\n')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--password-file', type=str, default='../baseline/examples/baseline_all.txt',
                        help='password file to calculate password entropy')

    args = parser.parse_args()

    if not os.path.isfile(args.password_file):
        sys.stdout.write('Invalid file supplied. System will now exit.' + '\n')
        return

    entropy = PasswordEntropy(passwordfile=args.password_file)
    entropy.populate_symbolset()
    entropy.calculate_password_entropy()




if __name__ == "__main__":
    main()