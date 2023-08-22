import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from sys import argv

def upload_video(video_path, title, description, tags):
    # Set up OAuth 2.0 credentials
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    credentials = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", scopes
    )
    credentials = credentials.run_local_server(port=8080)

    # Create the YouTube Data API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    # Create the video resource
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
        },
        "status": {
            "privacyStatus": "private",  # Set the privacy status of the video
        },
    }

    # Execute the API request to upload the video
    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=video_path,
    ).execute()

    print("Video uploaded successfully!")
    print(f"Video ID: {response['id']}")

# Example usage
video_path = "rendered_videos/output_video.mp4"
title = argv[1]
description = argv[2]
tags = ["test", "upload", "python"]
upload_video(video_path, title, description, tags)