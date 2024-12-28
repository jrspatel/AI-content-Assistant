"""
    Get historical data from Google trends API, 
    Analytics tool,
    media information - [Reddit, X and medium]

    ************* google trends can give me top searches ---> [ Use that keyword to see wt the world is searching for [tweets], how was the user reaction]
                  wt is the search rate on this topic    ---> [ same with the youtube { how many videos were made on this topic}]

        Final Output :-- it should give me a compiled answer on how should i proceed in the future with all this analytics...;
""" 
import pytrends 
from dotenv import load_dotenv
import tweepy
import os

load_dotenv()
# x_key = os.getenv('X_BEARER_TOKEN')

from pytrends.request import TrendReq 
pytrends = TrendReq(hl='en-US', tz=360)

def search_google_trends(query):
    search_result = pytrends.trending_searches(pn='united_states')
    trending_topics = search_result[0].tolist()
    print(trending_topics)

def search_google_trends_time(query):
    query = ['AI']
    search_result = pytrends.trending_searches(pn='united_states')
    trending_topics = search_result[0].tolist()
    pytrends.build_payload(query, cat=0, timeframe='today 5-y', geo='US')
    trending_topics_overtime = pytrends.interest_over_time()
    print(trending_topics_overtime)
    print(trending_topics)

search_google_trends_time('AI')







