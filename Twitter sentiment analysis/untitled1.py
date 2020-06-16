from textblob import TextBlob 
import sys,tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)

conKey="kbgWkH6gJ5GzExCIYbmptrOAm"
conSecret="c7xSEGsUAUPELpE6owvZYNwpYLXK2WLOFwiADj97Nsm5VmvuBJ"
accessToken="2824778653-2iK3MZyltx9WEqMq3MwSRTbxhnDVK9ONlPPBRqI"
accessTokenSecret="tRqRDmcnG7DMrmzZ31z9KFuV9swBURluQZHOY1meWkifs"


auth = tweepy.OAuthHandler(consumer_key=conKey,consumer_secret=conSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)


searchTerm = input("enter keyword:")
numbertweets = int(input("How many tweets?"))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(numbertweets)

p=0;
ne=0;
n=0;
polarity=0
for tweet in tweets:
     print(tweet.text)
     analyse = TextBlob(tweet.text)
      
     if(analyse.sentiment.polarity == 0):
        n  +=1
     elif(analyse.sentiment.polarity == 1):
        p  +=1
     elif(analyse.sentiment.polarity == -1):
        n  +=1
p = percentage(p,numbertweets)
ne = percentage(ne,numbertweets)
n = percentage(n,numbertweets)


print("people reaction on "+ searchTerm +" from " + str(numbertweets))


if(polarity == 0):
  print("neutral")
if(polarity < 0):
  print("negative")
if(polarity > 0):
  print("positive") 

labels = ['Positive['+str(p)+ '%]', 'Neutral [' + str(n) + '%]', 'Negative[' + str(ne) +'%]']
size = [p,n,ne]
color = ['red','yellow','green']
patches, texts = plt.pie(size, colors=color, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title("people reaction on"+ searchTerm +"from" + str(numbertweets))
plt.axis('equal')
plt.tight_layout()
plt.show()


  
  