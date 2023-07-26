# this is a sample uploader code , need to add the specific code to proceed with the actual uploading in YT channel

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import google.auth.transport.requests

def authenticate():
    # Set your credentials file path
    credentials_path = 'path/to/your/credentials.json'

    # Check if the credentials file exists
    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"Credentials file not found at {credentials_path}")

    # Create a flow instance to handle the OAuth 2.0 Authorization process
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        credentials_path, ['https://www.googleapis.com/auth/youtube.upload']
    )

    # Run the OAuth flow and get credentials
    credentials = flow.run_local_server()

    return credentials

def upload_video(video_path, title, description, category_id):
    # Authenticate
    credentials = authenticate()

    # Create an authorized API client
    youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

    # Prepare the video metadata
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'private'  # You can change this to 'public' if desired
        }
    }

    # Perform the video insert request
    try:
        response = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=video_path
        ).execute()

        video_id = response['id']
        print(f"Video uploaded successfully! Video ID: {video_id}")

    except googleapiclient.errors.HttpError as e:
        print(f"An error occurred: {e}")
        return None

    return video_id

if __name__ == '__main__':
    # Set your video file path
    video_file_path = 'path/to/your/video.mp4'
    video_title = 'Your Video Title'
    video_description = 'Your Video Description'
    video_category_id = 'Your Video Category ID'  # Category ID for 'Entertainment', 'Education', etc. You can find the IDs in YouTube API documentation.

    upload_video(video_file_path, video_title, video_description, video_category_id)
