# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:33:06 2019

@author: Ranak Roy Chowdhury
"""

fname = "hw1_word_counts_05.txt"
word_len = 5
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

correct_guess = ['U'] #letters guessed correctly
correct_pos = [1] #position of the correctly guessed letters in the word
incorrect_guess = ['A', 'E', 'I', 'O', 'S'] #letters guessed incorrectly

vocab = [] #list of all words
freq = [] #list of occurences of all words
prior = [] #list of prior probability of all words
    
#list of the letters guessed
all_guess = correct_guess + incorrect_guess

#list of letters that haven't been guessed yet
remaining_alphabet = list(set(alphabet) - set(all_guess))


#list of all positions in a word
all_pos = list(range(word_len))

#list of blank positions left
blank_pos = list(set(all_pos) - set(correct_pos))
    
#stores the probability distribution of the letters 
#that haven't been guessed yet
remaining_alphabet_prob = [] 


#compute the prior probabilities
def computePrior():
    
    #total count of all the words that appear in the file
    total = sum(freq)
    
    #for each word, find Prior, prior_i = count_i/ total
    for i in freq:
        prior.append(i/total)


#scan the file and store the words in vocab and the counts in freq
def readFile():
 
    with open(fname, 'r') as f:
        for line in f:
            #spilt each line of file into strings
            words = line.split()
            
            #first element of line is the word
            vocab.append(words[0])
            
            #second element of line is the count of occurence
            #(string converted to int)
            freq.append(int(words[1], 10))
    
    
#match a word with the list of correct and incorrect guesses
def match(word):
    
    #boolean variable, 0 if word doesn't match with pattern
    #1 otherwise
    found = 0 
    i = 0
    
    #for every correctly guessed position of the word
    for pos in correct_pos:
        
        #if the letter guessed is not the letter 
        #in that position of the word
        #match isn't found, return 0
        if(correct_guess[i] != word[pos]):
            return found
        
        i += 1
        
    #for every letter that has already been guessed, 
    #see if that appears in any of the blank position. 
    #If it does, match isn't found, return 0
    for letter in all_guess:
        for pos in blank_pos:
            if(letter == word[pos]):
                return found
    
    #otherwise, match is found, retuen 1
    found = 1
    return found
    

#computes for all words: [P(Evidence|word)*P(word)]
def normalizationFactor():
    
    sum = 0
    i = 0
    
    #for every word in vocabulary
    for word in vocab:
        #computes P(Evidence|word),
        #1 if evidence matches with word, 0 otherwise
        found = match(word) 
        
        #computes P(Evidence|word)*P(word) 
        #and adds it for every word
        sum += found * prior[i] 
        i += 1
    
    return sum


#computes whether the letter matches with any of the letters 
#in the blank positions of the word
def compare(letter, word):
    
    #boolean variable
    found = 1 

    #return 1 if the letter appears in any of the blank positions 
    #else return 0
    for pos in blank_pos:
        if(letter == word[pos]):
            return found
    
    found = 0
    return found


#compute probability distribution over letters 
#that haven't been guessed yet
def computeProbDis():
    
    #computes for all words: [P(Evidence|word)*P(word)]
    nf = normalizationFactor()
    
    for letter in remaining_alphabet:
        
        sum = 0;
        i = 0;
        
        for word in vocab:
            #computes whether the letter matches 
            #with any of the letters in the blank positions of the word
            #return 1 if the letter appears in any of the blank positions of the word
            #else return 0
            b = compare(letter, word) #P(letter|word)
            
            if(b == 1):
            
                #computes P(Evidence|word)
                #1 if evidence matches with word, 0 otherwise
                d = match(word) 
                
                #computes P(word|Evidence) = (P(Evidence|word)*P(word)) / (for all words: [P(Evidence|word)*P(word)])
                c = (d * prior[i]) / nf 
                
                #computes P(letter|Evidence) = P(letter|word)*P(word|Evidence)
                sum += b*c 
                
            i += 1
            
        remaining_alphabet_prob.append(sum)
        
        
def decideLetter():
    
    #find the maximum probability among the letters
    max_prob = max(remaining_alphabet_prob)
    
    #find the letter corresponding to the maximum probability
    index = remaining_alphabet_prob.index(max_prob)
    guess = remaining_alphabet[index]
    print("Next best guess is: " + guess + " with a probability of " + str(max_prob))
    
        
def main():
    
    #scan the file and store the words, counts in dictionary
    readFile()
    
    #computing the prior for all the words
    computePrior()
    
    #compute probability distribution over letters 
    #that haven't been guessed yet    
    computeProbDis()
    
    #decide the letter with highest probability that is to be guessed
    decideLetter()
    
    
if __name__ == "__main__":
    main()