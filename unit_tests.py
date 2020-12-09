from 601APIPUBLIC import *
t = TwitterAPI()


def test_601APIPUBLIC_connection():
    test_connect = t.twitter_auth_and_connect("https://api.twitter.com/2/tweets/search/stream/rules")
    assert 'meta' in test_connect


def test_601APIPUBLIC_analysis():
    sampletweet = "NASDAQ and S&P close at all-time highs. Congratulations!" #POTUS most recent tweet copied to test sentiment, seems very positive, tested .3
    sentiment = t.analyze_sentiment(sampletweet = sampletweet)
    assert score > 0.25, "Sentiment should be positive" # this should be positive, tested on website was 0.3 which is green

def test_API_function(request):
    text = str(request.text)
    sen = analyze(text)
    w = weathertweets():
    Ftemp = int(j['main']['temp']*(9/5)-460
    Ftemp2 = math.trunc(Ftemp)
    assert 'sentiment' in sen
    assert Ftemp2 > 70 && sen > .25
    assert Ftemp2 <70 && sen <-.25 
    assert 

def test_case1():
    #returns positive depending on most recent potus tweet
    request = t.get_status(1312449034154504192)
    test_API_function(request)


def test_case2():
    request = t.get_status(1323457369670512641) # president elects most recent should work same
    test_API_function(request)


def test_case3();
    request = t.get_status(806191194736889856) #UK PM not in DC so weather should be wrong but function will run correctly
    test_API_function(request)

