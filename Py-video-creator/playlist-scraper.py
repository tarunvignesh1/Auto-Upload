import youtube_dl
from sys import argv
import os

def download_videos_from_playlist(playlist_url, output_path, vid_count):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'playlistend': vid_count,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = argv[1]
    vid_count = int(argv[2])
    output_path = "downloaded_videos"
    os.makedirs(output_path, exist_ok=True)
    download_videos_from_playlist(playlist_url, output_path, vid_count)