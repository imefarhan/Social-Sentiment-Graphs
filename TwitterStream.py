from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import MySQLdb
import time
import json
import sys
import Sentiment_mod as s


#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
#conn = MySQLdb.connect("mysql.server","beginneraccount","cookies","beginneraccount$tutorial")

#c = conn.cursor()


#consumer key, consumer secret, access token, access secret.
ckey="dtXcP1eEVxaIccRfJKlcySOkH"
csecret="3nG8jJLUXYdFNm2Fwq29xK94jsB1HffhkPbjS40FDcfJhsCef4"
atoken="155902992-FOF6RU3zUMq6fRewsVN7ELMtPadlIkI39FTY7PcF"
asecret="q8mf13xgbzTbPyVP8HfMdlTPbl2Kxtxye627qoqG9hpmf"

class listener(StreamListener):

    def on_data(self, data):
       try:
           
        all_data = json.loads(data)
        
        tweet = all_data["text"]

        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 70:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
	
######	if confidence*100 >= 70:
######      output = open("twitter-out.txt","a")
######	    output.write(sentiment_value)
######	    output.write('\n')
######      output.close()
        
        
        #username = all_data["user"]["screen_name"]
        
 #       c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
  #          (time.time(), username, tweet))

   #     conn.commit()

        #print((username,tweet))
        #print(tweet)
        
        return True
       except:
          return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"])
