import sys
import os
import requests
from bs4 import BeautifulSoup
from pytube import YouTube

def get_video_links(search_string, count):
    base_url = f"https://www.youtube.com/results?search_query={search_string}"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    video_links = []

    for link in soup.select(".yt-uix-tile-link"):
        video_links.append("https://www.youtube.com" + link["href"])

        if len(video_links) == count:
            break

    return video_links

def download_videos(video_links):
    if not os.path.exists("py-video-creator"):
        os.makedirs("py-video-creator")

    for link in video_links:
        try:
            yt = YouTube(link)
            video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
            if video:
                print(f"Downloading: {yt.title}")
                video.download(output_path="downloaded_vidoes")
            else:
                print(f"No high-resolution video available for: {yt.title}")
        except Exception as e:
            print(f"Error while downloading: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python video_downloader.py <search_string> <count>")
        sys.exit(1)

    search_string = sys.argv[1]
    count = int(sys.argv[2])

    video_links = get_video_links(search_string, count)
    download_videos(video_links)
