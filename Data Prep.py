# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:13:49 2019

@author: Ranak Roy Chowdhury
"""

import operator


#sort the prior probabilities and print the 15 most frequent and 14 least frequent words.
def sort_and_print(prior):
    
    #sort the prior probability list
    sorted_prior = sorted(prior.items(), key=operator.itemgetter(1))
    
    print("Fifteen most frequent words\n")
    print(sorted_prior[-15:])
    print("Fourteen least frequent words\n")
    print(sorted_prior[0:14])
    

#computing the prior 
def computePrior(dictionary, prior):
    
    #total count of all the words that appear in the file
    total = sum(dictionary.values())
    
    #for each word, find Prior, prior_i = count_i/ total
    for key in dictionary:
        prior[key] = dictionary[key]/total


#scan the file and store the words, counts in dictionary
def readFile(dictionary):
    
    fname = "hw1_word_counts_05.txt"
 
    with open(fname, 'r') as f:
        for line in f:
            #spilt each line of file into strings
            words = line.split() 
            
            #first element of line is the key, second is the value(string converted to int)
            dictionary[words[0]] = int(words[1], 10)
    
    
def main():
    
    #create of dictionary of vocabulary words and their respective number of occurences
    dictionary = {} 
    
    #store the prior probability associated with each word
    prior = {} 
    
    #scan the file and store the words, counts in dictionary
    readFile(dictionary) 
    
    #computing the prior
    computePrior(dictionary, prior) 
    
    #sort the prior probabilities and print the 15 most frequent and 14 least frequent words.
    sort_and_print(prior) 
    
    
if __name__ == "__main__":
    main()