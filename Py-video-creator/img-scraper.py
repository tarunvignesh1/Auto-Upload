import os
import requests
from bs4 import BeautifulSoup

def download_content_from_html(html, desired_file_location, filename=None):
    response = requests.get(html)
    if not filename:
        filename = html.split('/')[-1]
    if response.status_code == 200:
        full_file_path = os.path.join(desired_file_location, filename)
        with open(full_file_path, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully to {full_file_path}")
    else:
        print("Failed to download the file.")

def download_high_resolution_images(url, output_folder):
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags in the HTML
    a_tags = soup.find_all('a')
    count = 0
    for a_tag in a_tags:
        if 'href' in a_tag.attrs:
            href = a_tag['href']
            if href.startswith('http') and len(href) >= 52:
                count += 1
                response_new = requests.get(href)
                soup_new = BeautifulSoup(response_new.content,'html.parser')
                a_tags_new = soup_new.find_all('a', class_ ='btn btn-light download-item btn-lg btn-block')
                for a_tag2 in a_tags_new:
                    if 'href' in a_tag2.attrs:
                        href_new = a_tag2['href']
                        if count == 80:
                            exit(0)
                        download_content_from_html(href_new,output_folder)
                        


if __name__ == "__main__":
    website_url = "https://wallpapers.com/anime-girl"


    output_directory = "downloaded_images"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    download_high_resolution_images(website_url, output_directory)
    for pg in range(2,6):
            page = "?p="+str(pg)
            new_link = website_url+page
            download_high_resolution_images(new_link, output_directory)
