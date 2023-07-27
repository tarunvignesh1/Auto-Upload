import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def download_images(url, output_folder):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (without a visible window)
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    page_source = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all image tags in the HTML
    image_tags = soup.find_all('img')

    # Download each image
    for img in image_tags:
        img_url = img.get('data-src')  # Extract image URL from 'data-src' attribute
        if img_url:
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

    driver.quit()

if __name__ == "__main__":
    website_url = "https://www.wallpaperflare.com/search?wallpaper=anime+sexy+girl"
    output_directory = "downloaded_images"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    download_images(website_url, output_directory)
