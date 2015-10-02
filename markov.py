import sys
from random import choice


class SimpleMarkovGenerator(object):

    def __init__(self, filepaths, ngram_size=2):
        self.input_filepaths = filepaths
        self.chains = {}
        self.ngram_size = ngram_size


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

        words = input_text_string.split()
        words.append(None)

        # initialize active ngram with first n words of input text
        ngram_list = []
        for i in range(self.ngram_size):
            ngram_list.append(words[i])
        active_ngram = tuple(ngram_list)

        # for each word *after* initial ngram, add it to the dictionary entry for the ngram preceeding it
        for i in range(self.ngram_size, len(words)):
            if active_ngram in self.chains:
                self.chains[active_ngram].append(words[i])
            else:
                self.chains[active_ngram] = [words[i]]

            # move to the next ngram
            active_ngram = active_ngram[1:] + (words[i],)




    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        # your code here


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    pass