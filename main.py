##
#Made by Jordan Avelar
#To calculate the happiness score and location of tweets
#

import sentiment_analysis
#Get file names containing tweets and words with correlating happiness scores
tweetFile = input("Enter tweet file name: ")
keyWordsFile = input("Enter key words file name: ")

output = sentiment_analysis.compute_tweets(tweetFile, keyWordsFile)

if output == []:
    print("Error: At least one file not found.")
#Print out results from all 4 time zones used
else:
    print("\nEASTERN:\nAverage happiness score: %4.2f\nNumber of tweets with happy words: %d"
        "\nTotal number of tweets: %d\n" %(output[0][0], output[0][1], output[0][2]))

    print("CENTRAL:\nAverage happiness score: %4.2f\nNumber of tweets with happy words: %d"
        "\nTotal number of tweets: %d\n" %(output[1][0], output[1][1], output[1][2]))

    print("MOUNTAIN:\nAverage happiness score: %4.2f\nNumber of tweets with happy words: %d"
        "\nTotal number of tweets: %d\n" %(output[2][0], output[2][1], output[2][2]))

    print("PACIFIC:\nAverage happiness score: %4.2f\nNumber of tweets with happy words: %d"
        "\nTotal number of tweets: %d" %(output[3][0], output[3][1], output[3][2]))
