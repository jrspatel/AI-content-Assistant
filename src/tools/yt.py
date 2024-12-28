# -*- coding: utf-8 -*-

import os
import numpy as np
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from datetime import datetime, timedelta
import json 

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_video_statistics(youtube, video_ids):
    """
    Fetch statistics for a list of video IDs.
    """
    stats = []
    for i in range(0, len(video_ids), 50):  # Fetch in batches of 50 (API limit)
        request = youtube.videos().list(
            part="statistics",
            id=",".join(video_ids[i:i+50])
        )
        response = request.execute()
        for item in response.get("items", []):
            stats.append({
                "views": int(item["statistics"].get("viewCount", 0)),
                "likes": int(item["statistics"].get("likeCount", 0)),
                "comments": int(item["statistics"].get("commentCount", 0))
            })
    return stats

def fetch_videos_by_date(youtube, keyword, date):
    """
    Fetch videos for a specific keyword and date.
    """
    request = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=50,
        order="date",
        publishedAfter='2024-12-10T00:00:00Z',
        publishedBefore='2024-12-11T00:00:00Z'
    )
    response = request.execute()
    return response.get("items", [])

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "D:/Personalized-AI-Content-Assistant/credentials.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Analyze data for the past 7 days
    keyword = "AI"
    today = datetime.utcnow()
    daily_video_counts = []
    video_stats = []

    for i in range(7):
        date = today - timedelta(days=i)
        videos = fetch_videos_by_date(youtube, keyword, date)
        video_ids = [item["id"]["videoId"] for item in videos]
        daily_video_counts.append(len(video_ids))
        if video_ids:
            stats = get_video_statistics(youtube, video_ids)
            video_stats.extend(stats)

    # Calculate statistics
    total_videos = len(video_stats)
    avg_views = np.mean([stat["views"] for stat in video_stats]) if total_videos > 0 else 0
    avg_likes = np.mean([stat["likes"] for stat in video_stats]) if total_videos > 0 else 0
    avg_comments = np.mean([stat["comments"] for stat in video_stats]) if total_videos > 0 else 0

    youtube_statistics = {
    "keyword": keyword,
    "total_videos_analyzed": sum(daily_video_counts),
    "average_daily_video_count": round(np.mean(daily_video_counts), 2),
    "average_views": round(avg_views, 2),
    "average_likes": round(avg_likes, 2),
    "average_comments": round(avg_comments, 2)
    }

# Dump to a JSON file
    with open("youtube_statistics.json", "w") as json_file:
        json.dump(youtube_statistics, json_file, indent=4)

    print("YouTube statistics have been saved to 'youtube_statistics.json'.")

if __name__ == "__main__":
    main()
