from pytube import Playlist, YouTube
from sys import argv
import os

def download_videos_from_playlist(playlist_url, output_path, vid_count):
    try:
        playlist = Playlist(playlist_url)
        count = 0
        for video_url in playlist.video_urls[:vid_count]:
            count += 1
            yt = YouTube(video_url)
            video_stream = yt.streams.get_highest_resolution()
            if video_stream is not None:
                video_filename = f"{count}.mp4"
                video_filepath = os.path.join(output_path, video_filename)
                print(f"Downloading: {yt.title}")
                video_stream.download(output_path, filename=video_filename)
                os.rename(os.path.join(output_path, video_filename), video_filepath)
            else:
                print(f"No suitable stream found for: {yt.title}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    playlist_url = argv[1]
    vid_count = int(argv[2])
    output_path = "downloaded_videos"
    os.makedirs(output_path, exist_ok=True)
    download_videos_from_playlist(playlist_url, output_path, vid_count)