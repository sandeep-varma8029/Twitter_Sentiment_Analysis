from textblob import TextBlob 
import tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)

conKey="IeqYcpJsgOqT3C0nDr3ya64BY"
conSecret="YA5rJIl833oM9ZevI6kTK39Wjh97Svl6z6wmDAhouePlRjiEUZ"
accessToken="2824778653-TjduCGlYHplGvPPvirVokw3HaDvTaLtNdNOFX5l"
accessTokenSecret="ZWYHDlukqjJFAjJUllCaNkCvIP5FihxteIdYAQzDNpbVR"


auth = tweepy.OAuthHandler(consumer_key=conKey,consumer_secret=conSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)


searchTerm = input("enter keyword:")
numbertweets = int(input("How many tweets?"))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(numbertweets)

pos=0
neg=0
neu=0
polarity=0


for tweet in tweets:
     analysis = TextBlob(tweet.text)
     polarity +=analysis.sentiment.polarity
     if(analysis.sentiment.polarity == 0):
        neu  +=1
     elif(analysis.sentiment.polarity > 0.00):
        pos  +=1
     elif(analysis.sentiment.polarity < 0.00):
        neg  +=1
        
pos = percentage(pos,numbertweets)
neg = percentage(neg,numbertweets)
neu = percentage(neu,numbertweets)


print("people reaction on "+ searchTerm +" from " + str(numbertweets))


if(polarity == 0):
  print("neutral")
if(polarity < 0):
  print("negative")
if(polarity > 0):
  print("positive") 

labels = ['Positive['+str(pos)+ '%]', 'Neutral [' + str(neu) + '%]', 'Negative[' + str(neg) +'%]']
size = [pos,neu,neg]
color = ['red','yellow','green']
patches, texts = plt.pie(size, colors=color, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title("people reaction on "+ searchTerm +" from " + str(numbertweets))
plt.axis('equal')
plt.tight_layout()
plt.show()
     


  
  