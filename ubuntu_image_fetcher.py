import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one if missing"""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def file_hash(filepath):
    """Compute SHA256 hash of a file to prevent duplicates"""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def fetch_image(url, folder="Fetched_Images"):
    """Fetch a single image from a URL"""
    try:
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()  # Check HTTP status codes

        # Check content-type to ensure it's an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: URL does not point to an image ({content_type})")
            return

        # Prepare folder and filename
        os.makedirs(folder, exist_ok=True)
        filename = get_filename_from_url(url)
        filepath = os.path.join(folder, filename)

        # Prevent duplicate downloads by comparing hashes
        if os.path.exists(filepath):
            existing_hash = file_hash(filepath)
            new_hash = hashlib.sha256(response.content).hexdigest()
            if existing_hash == new_hash:
                print(f"✓ Duplicate detected: {filename} already exists, skipping.")
                return

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter one or more image URLs (separated by commas): ").split(",")

    for url in urls:
        url = url.strip()
        if url:  # Ignore empty strings
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
