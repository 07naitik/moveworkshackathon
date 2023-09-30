import os
os.environ["OPENAI_API_KEY"] = "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"

import requests
from xml.etree import ElementTree as ET

def get_sitemap_links(sitemap_url):
    try:
        # Fetch the sitemap.xml content
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            # Parse the XML content
            root = ET.fromstring(response.content)

            # Extract all URLs from the sitemap
            links = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

            return links
        else:
            print(f"Failed to fetch sitemap.xml. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:

site = 'https://www.moveworks.com'

sitemap_url = f'{site}/sitemap.xml'
urls = get_sitemap_links(sitemap_url)

# if result:
#     print(f"Webpage links from {sitemap_url}:")
#     for link in result:
#         print(link)
# else:
#     print("No webpage links found.")