"""
    1. Search how many articles are being published each day w.r.t { kEYWORD }
    2. Give me the most trending topic according to the blogs data
"""

# from newsapi import NewsApiClient

# # Init
# newsapi = NewsApiClient(api_key='143d133a85bb433e834e2edb6b9ff9bb')

# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='Artificial Intelligence',
                                          
#                                           language='en',
#                                           country='us')

# /v2/everything
# all_articles = newsapi.get_everything(q='AI',
#                                       from_param='2024-12-01',
#                                       to='2024-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/top-headlines/sources
# sources = newsapi.get_sources()
# print(sources) 
# print('--------------------')
# print(top_headlines)
# print(top_headlines['totalResults'])
# print(top_headlines['articles'][0]['content'])

# import feedparser
# import requests

# # arXiv search URL with query parameters
# search_url = "http://export.arxiv.org/api/query"
# params = {
#     "search_query": "cat:cs.AI",  # Search for AI papers in the AI category
#     "start": 0,  # Start at the beginning of the results
#     "max_results": 5,  # Limit to 5 results
#     "sortBy": "lastUpdatedDate",  # Sort by last updated date
# }

# # Make the request
# response = requests.get(search_url, params=params)

# # Parse the response as an XML feed
# feed = feedparser.parse(response.text)

# # Display paper details
# for entry in feed.entries:
#     print(f"Title: {entry.title}")
#     print(f"Link: {entry.link}")
#     print(f"Published: {entry.published}")
#     print(f"Summary: {entry.summary}")
#     print("-" * 50)

from serpapi import GoogleSearch
import os
import dotenv 
from dotenv import load_dotenv
import json 

load_dotenv()
api_key = os.getenv('SERPER_API_KEY')
print(api_key)
params = {
    "q": "Artificial Intelligence",  # Search query
    "tbm": "nws",  # Target Google News
    "location": "United States",  # Optional: Specify location
    "hl": "en",  # Language
    "api_key": api_key,  # SerpAPI Key
}

# Perform Search
search = GoogleSearch(params)
results = search.get_dict()
print(results)

# Display News Results
news_data = []
for article in results.get("news_results", []):
    news_data.append({
        "source": article.get("snippet")
    })

# Write News Results to a JSON File
with open("ai_news_results.json", "w", encoding="utf-8") as json_file:
    json.dump(news_data, json_file, ensure_ascii=False, indent=4)
