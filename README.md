# API-Project-2
API project with Twitter API and Google NLP API
*******************************************
Written by:  Kellen Jay
EC 601 FALL 2020
*******************************************
Purpose:
This program users Google NLP API, the Twitter API and OpenSource Weather API to analyze a tweet from the current president and return their sentiment score along with the weather the day it was tweeted. It also prints a text sentence merging the two to see how the weather affected the presidents mood on twitter. The origianl goal of the project was to use the translate API too (some of the code is commented out) in order to translate the most recent tweet from a non-English twitter and then run it through the google NLP to see how it would work, but I ran into some issues getting non latin characters recognized so I stopped and worked from English only.  
********************************************
Further Implementation: 
This would be a fun machine learning project. Analyze the most recent 20 tweets from the POTUS twitter account using api.user_timline() and then run each one through sentiment. The difficult part would be accessing historical weather of Washington DC. It can be accessed with http://history.openweathermap.org/data/2.5/history/city?id={id}&type=hour&start={start}&cnt={cnt}&appid={API key} call but would have to run by the tweet date and it's limited to one call per week for free accounts. From that, the weather could be ranked similarly to the Google NLP sentiment, and then could be graphed to see how negative the president tweeeted in relation to the weather that day. Even further a OLS  regression could be used to determine an optimal function for how the president tweets depending on the weather. I would be interested in doing this in the future as a side project.
*********************************************
Unit Tests:
Testing was a challenge considering this project relied on a third API to get the weather of a person which I had set manually to the location of hte person. It was possible to test the sentiment analysis, tweets, and connection, but getting it to fail because it recognized that the person tweeting was in a different location from the returned temperature from Open weather was a challenging. The unit test will pass, but the user will have to ensure that the person they are returning tweets from is in the DC area, or else they would have to edit the source code. Further implementation would require learning more about how the Open Weather API works in order to possibly use GPS coordinates of twitter 'location' statistics to match, then return the weather for better accuracy on these unit tests.
