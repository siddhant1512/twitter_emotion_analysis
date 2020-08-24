def query(a):
    import string
    from collections import Counter

    import matplotlib.pyplot as plt
    import nltk
    from nltk.tokenize import word_tokenize

    def get_tweets():
        import GetOldTweets3 as got
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(a) \
            .setSince("2020-01-01") \
            .setUntil("2020-04-01") \
            .setMaxTweets(100)
        # Creation of list that contains all tweets
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        # Creating list of chosen tweet data
        text_tweets = [[tweet.text] for tweet in tweets]
        return text_tweets

    tweet = get_tweets()
    text = ""
    for i in range(len(tweet)):
        text = tweet[i][0] + " " + text


    lower = text.lower()
    data = lower.translate(str.maketrans("","",string.punctuation))

    tokenize_word = data.split()

    from nltk.corpus import stopwords
    sw = set(stopwords.words('english'))



    cleantext = [word for word in tokenize_word if word not in sw]

    ##creating emotion list
    emotion_list=[]
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            if word in cleantext:
                emotion_list.append(emotion)




    w = Counter(emotion_list)




    ##plotting
    plt.style.use('seaborn')
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('QUERY.png')
    plt.xlabel('emotions')
    plt.title('twitter sentimental analyses ')

    plt.show()



