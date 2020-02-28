#
# Assignment #3
# Calculates the average sentiment score, count of key word tweets and count of tweets in each time zone
#

# allows the use of string.punctuation
import string

# perimeters for the different geographic zones
LONG_2 = 49.189787
LONG_1 = 24.660845
LAT_1 = -67.444574
LAT_2 = -87.518395
LAT_3 = -101.998892
LAT_4 = -115.236428
LAT_5 = -125.242264


# changes the line into lower case
def format_input(text_line):
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = " ".join(word_list)
    return text_line


# finds the location from a given longitude and latitude
def position(long, lat):
    if LONG_1 <= long <= LONG_2:
        if LAT_1 >= lat > LAT_2:
            return "e"
        elif LAT_2 >= lat > LAT_3:
            return "c"
        elif LAT_3 >= lat > LAT_4:
            return "m"
        elif LAT_4 >= lat >= LAT_5:
            return "p"
        else:
            return


# method that computes scores
def compute_tweets(tweet, keyword):
    # initialize needed variables
    tweet_list = []
    keyword_list = []
    pacific = 0
    mountain = 0
    central = 0
    eastern = 0
    pacific_sentiment = 0
    mountain_sentiment = 0
    central_sentiment = 0
    eastern_sentiment = 0
    eastern_total = 0
    pacific_total = 0
    mountain_total = 0
    central_total = 0

    # checks any errors with opening the files
    try:
        open(tweet, "r", encoding="utf‐8")
    except IOError:
        print("Could not open input file: Error in Tweet input")
        return 0, 0, 0, 0
    try:
        open(keyword, "r", encoding="utf‐8")
    except IOError:
        print("Could not open input file: Error in Keyword input")
        return 0, 0, 0, 0

    # opens file and for each line in the tweet, adds it to the array list of tweets
    with open(tweet, encoding="utf‐8") as tweet_file:
        for line in tweet_file:
            tweet_list.append(line)
    # opens file and for each line in the keywords list, adds it to an array list of key words
    with open(keyword, encoding="utf‐8") as keyword_file:
        for line in keyword_file:
            keyword_list.append(line)
    # using each value in the array, will open the keyword and match every sentiment word with tweet word
    for x in range(len(tweet_list)):
        # initialize needed variables
        has_sentiment = False
        num_sentiments = 0
        sentiment = 0
        # formats the tweet in the method format input
        current_tweet = format_input(tweet_list[x])
        # find location of current tweet, a try statement to ensure that there is an actual location in the tweet
        try:
            long = float(current_tweet[1: current_tweet.find(",")])
        # if the given file does not have locations, then the wrong file was given and return an empty list
        except ValueError:
            print("Value Error. File is incorrect, there is no location in one or more tweets")
            return 0, 0, 0, 0
        lat = float(current_tweet[current_tweet.find(",")+1: current_tweet.find("]")])
        location = position(long, lat)
        # if the tweet contains a sentiment word, then add it to the total sentiments in the region
        for y in range(len(keyword_list)):
            # find the first part of the keyword before the comma
            current_keyword = keyword_list[y]
            current_keyword_word = current_keyword[:current_keyword.find(",")]
            # for each word in the current tweet
            for current_word in current_tweet.split():
                # takes away all the punctuation on both ends of the word as long as the word has more than one length
                while len(current_word) > 0 and (current_word[-1] in string.punctuation or current_word[0] in string.punctuation):
                    for punc in string.punctuation:
                        current_word = current_word.strip(punc)
                # if the keyword and the word from the tweet are the same adds one to the number of sentiment words in the current tweet
                if current_word == current_keyword_word:
                    num_sentiments += 1
                    # increases value of sentiment by the second part of the keyword after the comma (the score)
                    sentiment += int(current_keyword[current_keyword.find(",")+1:])
                    # declares that this tweet does have a sentiment word
                    has_sentiment = True

        # add tweet to the total amount of tweets in the region and if there is sentiment words in the tweet, adds the happiness score to the locations sentiment score and one to total sentiment tweets in that location
        if location == "e":
            eastern_total += 1
            if has_sentiment:
                eastern += 1
                eastern_sentiment += sentiment/num_sentiments
        elif location == "c":
            central_total += 1
            if has_sentiment:
                central += 1
                central_sentiment += sentiment/num_sentiments
        elif location == "m":
            mountain_total += 1
            if has_sentiment:
                mountain += 1
                mountain_sentiment += sentiment/num_sentiments
        elif location == "p":
            pacific_total += 1
            if has_sentiment:
                pacific += 1
                pacific_sentiment += sentiment/num_sentiments

    # adds the value of happiness score, total tweets with sentiment in region and total tweets in region to a list (if total tweets with sentiment is zero, then the happiness score is zero)
    if eastern == 0:
        happiness_eastern = 0
    else:
        happiness_eastern = eastern_sentiment/eastern
    final_eastern = (happiness_eastern, eastern, eastern_total)
    if central == 0:
        happiness_central = 0
    else:
        happiness_central = central_sentiment/central
    final_central = (happiness_central, central, central_total)
    if mountain == 0:
        happiness_mountain = 0
    else:
        happiness_mountain = mountain_sentiment/mountain
    final_mountain = (happiness_mountain, mountain, mountain_total)
    if pacific == 0:
        happiness_pacific = 0
    else:
        happiness_pacific = pacific_sentiment/pacific
    final_pacific = (happiness_pacific, pacific, pacific_total)
    return [final_eastern, final_central, final_mountain, final_pacific]




