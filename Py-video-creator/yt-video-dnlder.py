from pytube import Playlist, YouTube
from sys import argv
import re
from pytube import Playlist

def clean_filename(title):
    # Remove non-alphanumeric characters and spaces from the title
    cleaned_title = re.sub(r'[^\w\s]', '', title)
    # Replace spaces with underscores
    cleaned_title = cleaned_title.replace(' ', '_')
    return cleaned_title

def download_playlist(playlist_url, output_folder):
    try:
        # Create a Playlist object with the URL of the YouTube playlist
        playlist = Playlist(playlist_url)

        # Print the playlist title and number of videos in the playlist
        print(f"Downloading playlist: {playlist.title}")
        print(f"Number of videos in the playlist: {len(playlist.video_urls)}")

        # Loop through all video URLs in the playlist
        for video_url in playlist.video_urls:
            try:
                # Create a YouTube object with the video URL
                video = YouTube(video_url)
                # Print the video title
                print(f"Downloading video: {video.title}")

                # Choose the stream with the highest resolution (video only)
                video_stream = video.streams.filter(progressive=True, file_extension='mp4').\
                               order_by('resolution').desc().first()

                if video_stream is not None:
                    # Clean the video title to create a valid filename
                    cleaned_title = clean_filename(video.title)
                    # Set the output path for the downloaded video
                    output_path = f"{output_folder}/{cleaned_title}.mp4"
                    # Download the video in high resolution
                    video_stream.download(output_folder, filename=cleaned_title)
                    print(f"Downloaded video: {video.title}")
                else:
                    print(f"No suitable video stream found for {video.title}. Skipping.")

            except Exception as e:
                print(f"Error downloading video: {e}")
    except Exception as e:
        print(f"Error loading playlist: {e}")


if __name__ == "__main__":
    playlist_url = argv[1]
    output_folder = "downloaded_audios"

    download_playlist(playlist_url, output_folder)
