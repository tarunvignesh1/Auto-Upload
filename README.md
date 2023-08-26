# Auto-Upload


### This is a Automation method for auto uploading videos for my faceless youtube channel 


### Sub Modules:

I have divided the Youtube Auto Upload project into multiple Sub modules to keep some track on it and be debug friendly.

-  [img-scraper](Py-Video-creator/img-scraper.py) -- this is used for scraping copyright free images from a specific site as explained in that note.

- [playlist-scraper](Py-Video-creator/playlist-scraper.py) -- Used to download a series of youtube playlist of lofi songs which are copyright free.

- [Video-renderer](Py-video-creator/video-renderer.py) -- Used moviepy python lib to edit the videos with the scraped images and audio and editing them to a specific themed one , here it is a Lofi video.

-  [video-uploader](video-uploader.py) -- Created to upload the video once the rendering has completed to a faceless Youtube channel.

---
	Note: These are linked with CLI arguments and timed in a specific manner such that it gives ample of time to scrape, render and upload, and can be sequenced using a shell script.

Citations:
[1] https://github.com/ClarityCoders/AutoTube

```PS: This is a public one so open to all improvements, correction and any kind of optimization on this repo is always welcomed.. :)```