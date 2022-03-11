import string
import operator
from collections import OrderedDict

f = open("document.txt", encoding = "utf8")

wordFreqDT = dict()

for line in f:
    #removing punctuation
    line = line.translate(line.maketrans("", "", string.punctuation))
    #removing whitespace
    line = line.strip()
    #converting all the words to lowercase
    line = line.lower()
    #defining a new list containing all the words
    wordsList = line.split()

    #for loop which will iterate through the wordsList and will make a corresponding dictionary entry for each word
    for word in wordsList:
        #Case 1: Word is already in the dictionary and we want to increment the frequency
        if word in wordFreqDT:
            wordFreqDT[word] = wordFreqDT[word] + 1
        #Case 2: New Entry
        else:
            wordFreqDT[word] = 1

    sortedDict = dict(sorted(wordFreqDT.items(), key=operator.itemgetter(1),reverse=True))

    i = 0
    for key in sortedDict:
        if i < 5:
            print(key, ": ", sortedDict[key])
            i = i + 1

    
