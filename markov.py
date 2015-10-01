import sys
from random import choice


class SimpleMarkovGenerator(object):

    def __init__(self, filepaths):
        self.input_filepaths = filepaths
        self.chains = {}


    def read_files(self):
        """Given a list of files, make chains from them."""


        for filepath in self.input_filepaths:
            text_file = open(filepath)
            full_text_string = text_file.read()
            text_file.close()

            # add chains from the current file to the overall chains dictionary
            self.make_chains(full_text_string)

        print self.chains


    def make_chains(self, input_text_string):
        """Takes input text as string; stores chains."""

        # your code here which works on self.chains

        #don't return chains

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        # your code here


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    pass