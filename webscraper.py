from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re
import pandas as pd

# Load URLs from a CSV file
csv_file = 'websites.csv'  # Make sure to update this with the path to your CSV file
df = pd.read_csv(csv_file)
urls_list = df['website'].tolist()  # Assuming the CSV file has a column named 'url'

# Initialize the URL deque with the URLs from the CSV file
urls = deque(urls_list)

scraped_urls = set()
emails = set()

count = 0
try:
    while len(urls):
        count += 1
        if count == 36674:  # Set a limit to avoid infinite loops or excessive requests
            break
        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)

        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue
        except requests.exceptions.InvalidURL:
            print("Invalid URL:", url)
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

for mail in emails:
    print(mail)

# Instead of the last loop that prints emails, we add code to write them to a file.
with open('emails.txt', 'w') as f:
    for mail in emails:
        f.write(mail + '\n')

print("Emails extracted successfully and saved to 'emails.txt' file.")
