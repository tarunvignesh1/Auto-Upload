import os
import sys
import requests
from pytube import YouTube
import re

def search_youtube_videos(search_query, num_videos):
    search_url = f"https://www.youtube.com/results"
    response = requests.get(search_url, params={"search_query": search_query})
    video_ids = re.findall(r"watch\?v=(\S{11})", response.text)

    video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]

    filtered_video_urls = []
    for video_url in video_urls:
        response = requests.get(video_url)
        if "LIVE_STREAM_OFFLINE" not in response.text:
            filtered_video_urls.append(video_url)

    return filtered_video_urls[:num_videos]

def download_videos(video_urls):
    os.makedirs("downloaded_videos", exist_ok=True)

    for video_url in video_urls:
        try:
            video = YouTube(video_url)
            video_stream = video.streams.filter(file_extension='mp4').first()
            if video_stream is not None:
                print(f"Downloading video: {video.title}")
                file_path = video_stream.download("downloaded_videos")
                print(f"Downloaded: {video.title}")

        except Exception as e:
            print(f"Error downloading video: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python youtube_search_and_download.py <SEARCH_TERM> <NUM_VIDEOS>")
        sys.exit(1)

    search_query = sys.argv[1] + " japanese lofi"
    num_videos = int(sys.argv[2])

    video_urls = search_youtube_videos(search_query, num_videos)
    if not video_urls:
        print("No videos found for the given search term.")
    else:
        download_videos(video_urls)
