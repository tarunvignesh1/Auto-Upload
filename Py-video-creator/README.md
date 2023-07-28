# Py-Video-Creator


## Module 1: High-Resolution Image Scraper

This Python script allows you to download high-resolution images from a specific website. It uses the `requests` and `BeautifulSoup` libraries for web scraping.
--- It was structured for site like wallpapers.com

### Features:
- Downloads high-resolution images from a specified website.
- Supports multiple pages for gallery navigation.

### How to Run the Program:

1. Ensure you have Python and the necessary libraries installed (requests, BeautifulSoup).
2. Save the provided script in a Python file (e.g., `image_downloader.py`).

3. Open a terminal or command prompt and run the script with the website URL as a command line argument:

```bash
python image_downloader.py <website_url>
```

Replace `<website_url>` with the URL of the website from which you want to download the high-resolution images.

### Notes:
- The script is tailored to work with a specific website's HTML structure for image retrieval.
- Images are saved in the "downloaded_images" folder in the same directory as the script.
- The script fetches images from multiple pages (up to 5) by appending the query parameter `?p=` to the URL.
- The script will stop after downloading 80 images to prevent potential redirection loops.

Please ensure you have permission to access and download content from the website you are scraping, and be aware of any legal implications. Modify the script to suit other websites with different HTML structures or requirements.
