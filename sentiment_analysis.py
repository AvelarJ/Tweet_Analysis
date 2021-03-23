##
#Module used to compute tweet information
#

import string

pacificNum = 0
mountainNum = 0
centralNum = 0
easternNum = 0

totalEastScore = 0
totalCentralScore = 0
totalMountainScore = 0
totalPacificScore = 0

eastHappyCount = 0
centHappyCount = 0
mountHappyCount = 0
pacHappyCount = 0

def compute_tweets(tweetFile, keyFile):
    #Inefficient way of setting each  counter to zero when compute_tweets is used bellow
    global pacificNum, mountainNum, centralNum, easternNum, totalPacificScore, totalMountainScore
    global totalCentralScore, totalEastScore, eastHappyCount, centHappyCount, mountHappyCount, pacHappyCount

    pacificNum = 0
    mountainNum = 0
    centralNum = 0
    easternNum = 0

    totalEastScore = 0
    totalCentralScore = 0
    totalMountainScore = 0
    totalPacificScore = 0

    eastHappyCount = 0
    centHappyCount = 0
    mountHappyCount = 0
    pacHappyCount = 0

    try:    #Opening tweet and keyword files
        tweets = open(tweetFile, "r", encoding="utf-8")
        keyWords = open(keyFile, "r", encoding="utf-8")
    except IOError:
        return []

    keyDic = {}
    done = False

    line = keyWords.readline()  #Used to read the next line in specified file
    while not done:
        #Loop to place all keywords and values into dictionary
        line = line.strip("\n")
        key = line.split(",")
        keyDic[key[0]] = int(key[1])
        line = keyWords.readline()
        if line == "":
            done = True

    def analyze_tweet(tweet):
        #Global variables to be used outside of analyze_tweet function
        global pacificNum, mountainNum, centralNum, easternNum
        global totalEastScore, totalCentralScore, totalMountainScore, totalPacificScore
        global eastHappyCount, centHappyCount, mountHappyCount, pacHappyCount
        wordIndex = -1

        inEast = False
        inCent = False
        inMount = False
        inPac = False

        location = tweet[tweet.find("[")+1:tweet.find("]")]
        location = location.split(",")
        latitude = float(location[0])
        longitude = float(location[1])
        #If statements find what timezone each tweet is from
        #Looking between longitude and latitude intervals
        if 24.660845 <= latitude <= 49.189787 and -67.444574 >= longitude >= -87.518395:
            easternNum += 1
            inEast = True
        if 24.660845 <= latitude <= 49.189787 and -87.518395 >= longitude >= -101.998892:
            centralNum += 1
            inCent = True
        if 24.660845 <= latitude <= 49.189787 and -101.998892 >= longitude >= -115.236428:
            mountainNum += 1
            inMount = True
        if 24.660845 <= latitude <= 49.189787 and -115.236428 >= longitude >= -125.242264:
            pacificNum += 1
            inPac = True

        for char in tweet:  #Find index of first letter in tweet
            wordIndex += 1
            if char.isalpha():
                tweetString = line[wordIndex:].lower()  #Turn string into lowercase
                tweetWords = tweetString.split(" ")
                for word in tweetWords:
                    for c in string.punctuation:    #Checks each character and removes punctuation
                        word = word.replace(c, "")
                    for keyword in keyDic:
                        if word == keyword: #Compares each word in the tweet with the keywords
                            tempHappyScore = keyDic[keyword]
                            if inEast:  #If statements for which timezone the tweet was determined
                                        #to be in previously
                                totalEastScore += tempHappyScore
                                eastHappyCount += 1
                            if inCent:
                                totalCentralScore += tempHappyScore
                                centHappyCount += 1
                            if inMount:
                                totalMountainScore += tempHappyScore
                                mountHappyCount += 1
                            if inPac:
                                totalPacificScore += tempHappyScore
                                pacHappyCount += 1
                break #End loop after each word is compared

    done = False
    line = tweets.readline()

    while not done: #Main while loop for each line in tweets file
        analyze_tweet(line)
        line = tweets.readline()
        if line == "":
            done = True
    #Final average calculations to be returned
    #Checks if there are any timezones with 0 tweets, avoids division by 0
    if eastHappyCount != 0:
        eastAverage = totalEastScore / eastHappyCount
    elif eastHappyCount == 0:
        eastAverage = 0
    if centHappyCount != 0:
        centralAverage = totalCentralScore / centHappyCount
    elif centHappyCount == 0:
        centralAverage = 0
    if mountHappyCount != 0:
        mountainAverage = totalMountainScore / mountHappyCount
    elif mountHappyCount == 0:
        mountainAverage = 0
    if pacHappyCount != 0:
        pacificAverage = totalPacificScore / pacHappyCount
    elif pacHappyCount == 0:
        pacificAverage = 0

    Eastern = (eastAverage, eastHappyCount, easternNum)
    Central = (centralAverage, centHappyCount, centralNum)
    Mountain = (mountainAverage, mountHappyCount, mountainNum)
    Pacific = (pacificAverage, pacHappyCount, pacificNum)

    tweets.close()
    keyWords.close()

    return Eastern, Central, Mountain, Pacific
