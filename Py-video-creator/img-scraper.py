import os
import requests
from bs4 import BeautifulSoup

def download_images(url, output_folder):
    # Send an HTTP GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags in the HTML
    image_tags = soup.find_all('img')

    # Download each image
    for img in image_tags:
        img_url = img['src']
        img_name = os.path.basename(img_url)

        try:
            # Send an HTTP GET request to download the image
            img_data = requests.get(img_url).content

            # Save the image in the output folder
            with open(os.path.join(output_folder, img_name), 'wb') as f:
                f.write(img_data)

            print(f"Image '{img_name}' downloaded successfully.")
        except Exception as e:
            print(f"Failed to download image '{img_name}': {e}")

if __name__ == "__main__":
    website_url = "https://www.wallpaperflare.com/search?wallpaper=anime+sexy+girl"  # Replace this with the website URL you want to scrape
    output_directory = "downloaded_images"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    download_images(website_url, output_directory)

