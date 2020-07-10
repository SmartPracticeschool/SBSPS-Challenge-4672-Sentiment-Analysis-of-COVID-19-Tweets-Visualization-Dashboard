import tweepy
import TwitterKey#Confidential files
import datetime
import mysql.connector
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, SentimentOptions

# connection of IBM Watson Studio
authenticator = IAMAuthenticator('3YVTTrpXHhpeouEsvNLJoQhRJm20aHGzCiS5oMnl0Ijr')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/93a3cf90-92c7-4d86-99aa-762e9b1dffb5')

# Credentials of twitter
consumerKey = TwitterKey.twitter_key["consumerKey"]
consumerSecret = TwitterKey.twitter_key["consumerSecret"]
accessKey = TwitterKey.twitter_key["accessKey"]
accessSecret = TwitterKey.twitter_key["accessSecret"]

# Authenticate Object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
authenticate.set_access_token(accessKey, accessSecret)
api = tweepy.API(authenticate, wait_on_rate_limit=True)

# dictionary of longitude,latitude,radius of cities
cities = {
    "Delhi": "28.7041,77.1025,21.73km",
    "Chennai": "13.0827,80.2707,11.65km",
    "Mumbai": "19.0760,72.8777,13.86km",
    "Kolkata": "12.9716,77.5946,15.02km"
}


# function of sentiment analysis of major cities

def overall_sentiment():
    t=0
    positive_sentiment = 0
    negative_sentiment = 0
    neutral_sentiment = 0
    sad_score = 0
    joy_score = 0
    anger_score = 0
    search_words = "#covid19" + " -filter:retweets"
    x = datetime.datetime.today()
    i= x - datetime.timedelta(days=1)
    while (t<1):
        tweets = tweepy.Cursor(api.search,
                              q=search_words,
                              lang="en", geocode="20.5937,78.9629,1023.140km", until=x.date()).items(500)

        for tweet in tweets:

            response = natural_language_understanding.analyze(
                text=tweet.text,
                language="en",
                features=Features(sentiment=SentimentOptions(document=True),
                         emotion= EmotionOptions(document=True))).get_result()

            score = response["sentiment"]["document"]["score"]

            sad_emotion = response["emotion"]["document"]["emotion"]["sadness"]
            anger_emotion = response["emotion"]["document"]["emotion"]["anger"]
            joy_emotion = response["emotion"]["document"]["emotion"]["joy"]

            if score > 0:
                positive_sentiment += 1
            elif score < 0:
                negative_sentiment += 1
            else:
                neutral_sentiment += 1

            if sad_emotion > anger_emotion and sad_emotion > joy_emotion:
                sad_score +=1
            if anger_emotion > sad_emotion and anger_emotion > joy_emotion:
                anger_score+=1
            if joy_emotion > anger_emotion and joy_emotion > sad_emotion:
                joy_score +=1

        mydb = mysql.connector.connect(
                     host="covidsentimentanalysis.mysql.pythonanywhere-services.com",
                     user="covidsentimentan",
                     password="administrator",
                     database = "covidsentimentan$tweets"
                    )
        mycursor = mydb.cursor()


        sql = "INSERT INTO overall_sentiment  VALUES ( %s,%s, %s,%s,%s,%s,%s)"
        val = (str(i.date()),positive_sentiment,negative_sentiment,neutral_sentiment,sad_score,anger_score,joy_score)
        mycursor.execute(sql, val)
        mydb.commit()


        # sql = "DELETE FROM overall_sentiment order by date LIMIT 1"
        # mycursor.execute(sql)
        # mydb.commit()

        t=+1
    print("done")


def sentiment_major_cities():
    city=0
    t=0
    positive_sentiment = 0
    negative_sentiment = 0
    neutral_sentiment = 0
    sad_score = 0
    joy_score = 0
    anger_score = 0
    x = datetime.datetime.today()
    i= x - datetime.timedelta(days=1)
    while (t<1):
        for a, y in cities.items():
            city+=1
            positive_sentiment = 0
            negative_sentiment = 0
            neutral_sentiment = 0
            sad_score = 0
            joy_score = 0
            anger_score = 0
            search_words = "#covid19" + " -filter:retweets"
            tweets = tweepy.Cursor(api.search,
                                  q=search_words,
                                  lang="en", geocode=y, until=x.date()).items(500)

            for tweet in tweets:

                response = natural_language_understanding.analyze(
                    text=tweet.text,
                    language="en",
                    features=Features(sentiment=SentimentOptions(document=True),
                             emotion= EmotionOptions(document=True))).get_result()

                score = response["sentiment"]["document"]["score"]

                sad_emotion = response["emotion"]["document"]["emotion"]["sadness"]
                anger_emotion = response["emotion"]["document"]["emotion"]["anger"]
                joy_emotion = response["emotion"]["document"]["emotion"]["joy"]

                if score > 0:
                    positive_sentiment += 1
                elif score < 0:
                    negative_sentiment += 1
                else:
                    neutral_sentiment += 1

                if sad_emotion > anger_emotion and sad_emotion > joy_emotion:
                    sad_score +=1
                if anger_emotion > sad_emotion and anger_emotion > joy_emotion:
                    anger_score+=1
                if joy_emotion > anger_emotion and joy_emotion > sad_emotion:
                    joy_score +=1

            mydb = mysql.connector.connect(
                         host="covidsentimentanalysis.mysql.pythonanywhere-services.com",
                         user="covidsentimentan",
                         password="administrator",
                         database = "covidsentimentan$tweets"
                        )
            mycursor = mydb.cursor()

            if city == 1:
                sql = "INSERT INTO delhi_sentiment  VALUES ( %s,%s, %s,%s,%s,%s,%s)"
                val = (str(i.date()),positive_sentiment,negative_sentiment,neutral_sentiment,sad_score,anger_score,joy_score)
                mycursor.execute(sql, val)
                mydb.commit()

            if city == 2:
                sql = "INSERT INTO chennai_sentiment  VALUES ( %s,%s, %s,%s,%s,%s,%s)"
                val = (str(i.date()),positive_sentiment,negative_sentiment,neutral_sentiment,sad_score,anger_score,joy_score)
                mycursor.execute(sql, val)
                mydb.commit()

            if city == 3:
                sql = "INSERT INTO mumbai_sentiment  VALUES ( %s,%s, %s,%s,%s,%s,%s)"
                val = (str(i.date()),positive_sentiment,negative_sentiment,neutral_sentiment,sad_score,anger_score,joy_score)
                mycursor.execute(sql, val)
                mydb.commit()

            if city == 4:
                sql = "INSERT INTO kolkata_sentiment  VALUES ( %s,%s, %s,%s,%s,%s,%s)"
                val = (str(i.date()),positive_sentiment,negative_sentiment,neutral_sentiment,sad_score,anger_score,joy_score)
                mycursor.execute(sql, val)
                mydb.commit()

        # sql = "DELETE FROM delhi_sentiment order by date LIMIT 1"
        # mycursor.execute(sql)
        # mydb.commit()

        # sql = "DELETE FROM mumbai_sentiment order by date LIMIT 1"
        # mycursor.execute(sql)
        # mydb.commit()

        # sql = "DELETE FROM chennai_sentiment order by date LIMIT 1"
        # mycursor.execute(sql)
        # mydb.commit()

        # sql = "DELETE FROM kolkata_sentiment order by date LIMIT 1"
        # mycursor.execute(sql)
        # mydb.commit()

        t=+1
    print("done")

sentiment_major_cities()
overall_sentiment()
