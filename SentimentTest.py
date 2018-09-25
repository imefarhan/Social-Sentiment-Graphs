import Sentiment_mod as s

myText = "i am happy"

sentiment_value, confidence = s.sentiment(myText)
print(myText,sentiment_value, confidence)
