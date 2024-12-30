# Content Assistant for Creators: AI-Powered Insights



## Background
With the rapid growth of content creators across various platforms like YouTube, blogs, and news websites, staying updated with the latest trends, performance metrics, and content ideas has become a challenge. The increasing number of creators and the evolving content landscape demand a tool that can assist in analyzing real-time data and offer actionable insights. 

This project is specifically developed to help content creators whether new or already have channels or blogs and help to stay ahead of the curve by:
- Tracking trending topics and the latest updates in their niche
- Analyzing YouTube video statistics for specific keywords to understand audience engagement
- Summarizing news and other relevant data to help creators focus on actionable insights
- Providing recommendations based on video performance metrics for better content creation strategies

With new creators emerging every day, the need for tools like this has never been greater. By using AI-powered insights, this project helps creators to make data-driven decisions and optimize their content creation journey.

## Project Purpose
This tool serves as a comprehensive assistant for content creators, offering:
- **Trending Topic Analysis**: Helps identify and track popular topics in real-time.
- **YouTube Video Analytics**: Gathers insights from YouTube statistics based on specific keywords.
- **Real time information**:  Top and trending information fetched/scrapped directly from the web.
- **Content Summarization**: Uses advanced models to generate summaries from news articles, so creators can focus on the important details.
- **Actionable Insights**: Provides actionable recommendations and strategies for audience engagement, makes schedule to plan the next moves and channel analysis.

By automating the process of tracking trends, summarizing information, and analyzing video performance, this tool helps content creators focus more on their creative work, while staying informed about their audience and the content they are creating.

## Features
### 1. **YouTube Video Analytics**
- Collects statistics on videos related to a specified keyword (e.g., views, likes, comments).
- Analyzes video performance over time, providing average engagement metrics.
- Helps creators understand which topics perform well.

### 2. **News Text Analysis**
- Retrieves the latest news articles related to a given keyword.
- Uses text processing and summarization techniques to provide short, meaningful summaries of the articles.
  
### 3. **Embedding-Based Search**
- Converts raw text data from YouTube statistics and news articles into high-quality embeddings.
- Uses **FAISS (Facebook AI Similarity Search)** to perform fast similarity searches and retrieve the most relevant content based on queries.

### 4. **Summarization**
- Uses GPT-based models to generate summaries of the retrieved content, allowing creators to focus on key insights.

### 5. **Query-Based Insights**
- Perform queries to retrieve relevant information (e.g., "What’s trending in AI?").
- Display the most relevant results based on user queries and summarize them using GPT models.




Example Workflow
Input Data: News articles and YouTube statistics related to trending keywords (e.g., “AI”).
Generate Embeddings: The raw text data from YouTube videos and news articles are converted into embeddings using the Sentence-BERT model.
Search with Query: Perform a query like "What’s trending in AI?" to retrieve relevant news articles and YouTube video data.
Summarization: The retrieved results are summarized using GPT-based models, providing you with concise insights.
Technology Stack
Language: Python
Libraries:
faiss for fast similarity search
sentence-transformers for generating embeddings
tensorflow for AI-based summarization models
numpy, json, os for data processing
Models:
all-MiniLM-L6-v2 for embedding generation
GPT-based models for summarization
Contributing
We welcome contributions to make this project even better! Whether you're improving the summarization algorithms, adding new features, or fixing bugs, we appreciate your help.



Creators: Stay Ahead of the Curve!
With more creators joining the space every day, it’s crucial to have a tool that helps you stay informed and ahead of the competition. By using this tool, you can access the latest data, track trends, and generate actionable insights that will improve your content creation process.
