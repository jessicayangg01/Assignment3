"""
Name: Jessica Yang
Program: Assignment 3, Sentiment Analysis
Program Description: analyzes twitter data and sentiment values
"""

import sentiment_analysis as s

# prompts user for tweet and key word list
tweet = input("Which tweet? ")
keyword = input("Which keyword list? ")


# calculates the scores from the given tweet and keywords
master_list = s.compute_tweets(tweet, keyword)

# print statements for empty master list
if master_list == (0, 0, 0, 0):
    for x in range(4):
        if x == 0:
            print("Eastern")
        if x == 1:
            print("Central")
        if x == 2:
            print("Mountain")
        if x == 3:
            print("Pacific")
        for y in range(3):
            if y == 0:
                print("Happiness Score: ", "0")
            if y == 1:
                print("Total sentiment tweets: ", "0")
            if y == 2:
                print("Total tweets: ", "0")
            y += 1
        x += 1
# print statement for if master list has values
else:
    # prints the list of all the different regions scores in a formatted matter
    for x in range(4):
        if x == 0:
            print("Eastern")
        if x == 1:
            print("Central")
        if x == 2:
            print("Mountain")
        if x == 3:
            print("Pacific")
        for y in range(3):
            if y == 0:
                print("Happiness Score: ", master_list[x][y])
            if y == 1:
                print("Total sentiment tweets: ", master_list[x][y])
            if y == 2:
                print("Total tweets: ", master_list[x][y])
            y += 1
        x += 1

