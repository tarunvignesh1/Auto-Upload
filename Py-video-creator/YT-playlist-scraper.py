from pytube import Playlist, YouTube
from sys import argv

def download_videos_from_playlist(playlist_url, output_path):
    try:
        playlist = Playlist(playlist_url)
        
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            video_stream = yt.streams.filter(file_extension='mp4', res="720p").first()
            if video_stream is not None:
                print(f"Downloading: {yt.title}")
                video_stream.download(output_path)
            else:
                print(f"No suitable stream found for: {yt.title}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    playlist_url = argv[1]
    output_path = "downloaded_videos"
    download_videos_from_playlist(playlist_url, output_path)
