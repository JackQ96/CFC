import json
import requests
from bs4 import BeautifulSoup
from collections import Counter

# Scrape the index webpage
response = requests.get("https://cfcunderwriting.com/")
soup = BeautifulSoup(response.text, 'html.parser')

# Write a list of all externally loaded resources to a JSON output file
external_resources = []
for link in soup.find_all('link'):
    if not link.get('href').startswith('https://cfcunderwriting.com/'):
        external_resources.append(link.get('href'))
for script in soup.find_all('script'):
    if script.get('src') and not script.get('src').startswith('https://cfcunderwriting.com/'):
        external_resources.append(script.get('src'))
with open('external_resources.json', 'w') as outfile:
    json.dump(external_resources, outfile)


# Enumerate the page's hyperlinks and identify the location of the "Privacy Policy" page
total_links = 0
privacy_policy_url = None
for a in soup.find_all('a', href=True):
    total_links += 1
    if a.text.lower() == 'privacy policy':
        privacy_policy_url = a['href']
        break
print("Total number of hyperlinks: ", total_links)

# Scrape the Privacy Policy page and produce a case-insensitive word count
if privacy_policy_url:
    if not privacy_policy_url.startswith("http"):
        privacy_policy_url = "https://cfcunderwriting.com" + privacy_policy_url
    response = requests.get(privacy_policy_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    text = text.lower() # ensure case is insensitive
    word_counts = Counter(text.split())
    with open('privacy_policy_word_counts.json', 'w') as outfile:
        json.dump(dict(word_counts), outfile)




# How would I improve the code if I had more time to make it more robust?

# 1) the Main thing would be error handling and test cases: Implementing Try-Except to catch errors, and even check to ensure I get a 200 response before going ahead with the parsed data

#2) Some websites load data dynamically and I believe this would cause issues with scraping. I would need to an external library to wait for the page to be fully loaded before scraping occurs.