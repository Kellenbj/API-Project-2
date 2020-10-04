import tweepy
import math
import json
import urllib3
import requests
import re
#from nlkt.tokenize import WordPunctTokenizer

from google.oauth2 import service_account
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import translate_v2 as translate


#client = language.LanguageServiceClient.from_service_account_json("/home/kellen/Downloads/gootwi601/services.json")
CONSUMER_KEY = 'pMhMmluBwKSZMirVNTNJUdb6F'
CONSUMER_SECRET ='FSLkVlutzXbu6PQWq05ovWNlSJB73YwsBpz8vhLVWACA7eQyLb'
ACCESS_KEY = '1307713333475397638-KiXD5DQxbsTQpG17exsNnLOBbUZhNb'
ACCESS_SECRET ='jbTFUp5oNxUED3TrtulH2qkPRS9QX4hIUC7xXCrJgIUaV'

GOOGLE_APPLICATION_CREDENTIALS= '0671a27084b62c73cb123d26708d7a9b309eafcc'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def weathertweets():
    weatherrequest = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=38.8977&lon=77.0365&appid=8919a473d49b7ca8db97e901687f35f5')
    tweetdata = weatherrequest.json()
    return tweetdata
    

#def tweetcleaner():
    #based on code from Dzaky Widya Putra on freecodecamp
#    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
#   link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
#    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
#    lower_case_tweet= number_removed.lower()
#    tok = WordPunctTokenizer()
#    words = tok.tokenize(lower_case_tweet)
#    clean_tweet = (' '.join(words)).strip()
#    return tweetcleaner

#def translate_text(text,target='en'):
#    translate_client = translate.client()
#    result = translate_client.translate(
#        text,
#        target_language = target)
#    print(u'Translation: {}'.format(result['translatedText']))
#    return result""

def analyze(tweet):
    client = language.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT
    document = types.Document(
        content=tweet,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)
    overall = response.document_sentiment
    results = float(overall.score)
    return results

def main():
    j = weathertweets()
    potusrequest = api.get_status(1312449034154504192)
    prestweet = str(potusrequest.text)
    sentiment = analyze(prestweet)
    #translatedN = n.translate_text()
    #cleanENtweet = n.tweetcleaner()
    Ftemp = int(j['main']['temp'])*(9/5)-460
    Ftemp2 = math.trunc(Ftemp)
    Fstring = str(Ftemp2)
    weatherlist = 'The weather at the White House is: ', j['weather'][0]['description'] + ' Temperature: '+ Fstring
    print(weatherlist)
    print("Today the President tweeted: ")
    print(potusrequest.text)
    print("Which has a sentiment value of: ")
    print(sentiment)
    if sentiment > .24 and Ftemp2 > 70:
        print("The president tweeted positively on a warm day!")
    elif sentiment >-.26 and sentiment < .25 and Ftemp >70:
        print("The president is a bit neutral on a warm day.")
    elif sentiment < -.25 and Ftemp >70:
        print("The president is negative on a lovely day...")
    elif sentiment < -.25 and Ftemp <71:
        print("The president is negative on cool day")
    elif sentiment > -.26 and sentiment < .25 and Ftemp <71:
        print("The president is neutral on a cool day")
    elif sentiment > .25 and Ftemp <71:
        print("The president is positive on a poor weather day..")


    #api.update_status(send)

main()
