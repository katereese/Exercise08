#!/usr/bin/env python
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    word_list = corpus.split()
    markov_dict = {}
    for idx in range(len(word_list)-2):
        if (word_list[idx],word_list[idx+1]) in markov_dict:
            markov_dict[(word_list[idx],word_list[idx+1])] += [word_list[idx+2]]
        else:
            markov_dict[(word_list[idx],word_list[idx+1])] = [word_list[idx+2]]
    return markov_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    tuple_start = ("could", "you")
    final_string = ""
    while chains.get(tuple_start):# != ("the", "end"):
        markov_value = chains.get(tuple_start)#, ("the", "end"))
        index = random.randint(0,len(markov_value)-1)
        tuple_start = (tuple_start[1], markov_value[index])
        final_string = final_string + " " + tuple_start[1]
        #print tuple_start
        # print final_string
    return final_string


def main():
    #args = sys.argv

    file = open("drsuess.txt")
    input_text = file.read()
    #print input_text

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":

    main()
