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
    counter = 0
    final_string = ""
    while tuple_start != ("the", "end") or counter == 20:
        markov_value = chains.get(tuple_start, ("the", "end"))
        #print markov_value
        index = random.randint(0,len(markov_value)-1)
        #print index
        tuple_start = (tuple_start[1], markov_value[index])
        #print tuple_start
        #print markov_value[index]
        counter += 1
        final_string = final_string + tuple_start[1]
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
