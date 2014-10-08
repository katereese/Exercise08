#!/usr/bin/env python
import random, string

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
    while True:
        random_idx = random.randint(0,len(chains)-1)
        tuple_start = chains.keys()[random_idx]
        if tuple_start[1][0] in string.ascii_uppercase:
            break
    final_string = ""
    
    while len(final_string) <= 140:
        markov_value = chains.get(tuple_start)
        index = random.randint(0,len(markov_value)-1)
        final_string = final_string + tuple_start[1] + " "
        tuple_start = (tuple_start[1], markov_value[index])
        if final_string[-2] in [".", "?", "!"] and len(final_string > 70:
            break
    return final_string


def main():

    file = open("frozen.txt")
    input_text = file.read()
    file2 =open("fscott.txt")
    input_text2 = file2.read()
    input_text += input_text2
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":

    main()
