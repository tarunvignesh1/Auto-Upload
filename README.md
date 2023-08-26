# Auto-Upload


### This is a Automation method for auto uploading videos for my faceless youtube channel 

The auto uploader for YouTube created using Python is a program that automates the process of uploading videos to YouTube. It utilizes the YouTube Data API, which allows developers to interact with YouTube's features and functionalities programmatically.

The program uses the Python programming language and the YouTube Data API to handle the authentication and communication with the YouTube platform. It enables users to upload videos to their YouTube channels directly from their local machine or a specified location.

The auto uploader program typically requires the user to provide the necessary credentials, such as the client secrets JSON file, which contains the OAuth 2.0 credentials for accessing the YouTube Data API. These credentials are used to authenticate the program and authorize it to upload videos on behalf of the user.

Once the program is authenticated, it can upload videos by specifying the video file's path, along with additional metadata such as the video title, description, and tags. The program then sends the video file to YouTube's servers for processing and makes it available on the user's YouTube channel.

The auto uploader program simplifies the process of uploading videos to YouTube, saving users time and effort. It can be customized and extended to include additional features such as video editing, thumbnail generation, and scheduling uploads.

Overall, the auto uploader for YouTube created using Python provides a convenient and efficient way to automate the process of uploading videos to YouTube, making it easier for content creators and businesses to share their content with a wider audience.

Citations:
[1] https://github.com/ClarityCoders/AutoTube

```PS: This is a public one so open to all improvements, correction and any kind of optimization on this repo is always welcomed.. :)```



### Sub Modules:

I have divided the Youtube Auto Upload project into multiple Sub modules to keep some track on it and be debug friendly.

-  [img-scraper](Py-Video-creator/img-scraper.py) -- this is used for scraping copyright free images from a specific site as explained in that note.

- [playlist-scraper](Py-Video-creator/playlist-scraper.py) -- Used to download a series of youtube playlist of lofi songs which are copyright free.

- [Video-renderer](Py-video-creator/video-renderer.py) -- Used moviepy python lib to edit the videos with the scraped images and audio and editing them to a specific themed one , here it is a Lofi video.

-  [video-uploader](video-uploader.py) -- Created to upload the video once the rendering has completed to a faceless Youtube channel.

---
	Note: These are linked with CLI arguments and timed in a specific manner such that it gives ample of time to scrape, render and upload, and can be sequenced using a shell script.

