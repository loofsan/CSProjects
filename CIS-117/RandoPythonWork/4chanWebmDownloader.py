import os
import requests
from bs4 import BeautifulSoup

# Set the download path
download_path = r"C:\\Users\\Lynn Thike Aung\\Downloads\\4chanwebms\\ERP"

# Function to download webms from a given 4chan thread URL
def download_webms(url):
    if not url.startswith("https://boards.4chan.org/"):
        print("Please provide a valid 4chan thread URL.")
        return
    
    # Ensure the download directory exists
    os.makedirs(download_path, exist_ok=True)
    
    try:
        # Fetch the thread's HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error on bad status
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all .webm links in the thread
    webms = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.webm')]

    if not webms:
        print("No .webm files found in the thread.")
        return

    # Download each .webm file found
    for webm_url in webms:
        webm_filename = webm_url.split('/')[-1]
        file_path = os.path.join(download_path, webm_filename)

        # Avoid overwriting existing files
        if os.path.exists(file_path):
            print(f"File {webm_filename} already exists, skipping.")
            continue
        
        try:
            with requests.get(f'https:{webm_url}', stream=True) as webm_response:
                webm_response.raise_for_status()

                # Write the .webm content to the specified path
                with open(file_path, 'wb') as f:
                    for chunk in webm_response.iter_content(chunk_size=8192):
                        f.write(chunk)

                print(f"Downloaded {webm_filename} successfully.")
        except requests.RequestException as e:
            print(f"Failed to download {webm_url}: {e}")

if __name__ == '__main__':
    thread_url = input("Enter a 4chan thread URL: ")
    download_webms(thread_url)
