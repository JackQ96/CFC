import json
import requests
from bs4 import BeautifulSoup
from collections import Counter

# Scrape the index webpage
response = requests.get("https://cfcunderwriting.com/")
#Parse the response in HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Write a list of all externally loaded resources to a JSON output file
external_resources = []
for link in soup.find_all('link'):
    # To find external, we want to find all links that do not start with cfc...
    if not link.get('href').startswith('https://cfcunderwriting.com/'):
        # Append results that fit this filter to external resources list
        external_resources.append(link.get('href'))
# Same as above but now for the script tags
for script in soup.find_all('script'):
    if script.get('src') and not script.get('src').startswith('https://cfcunderwriting.com/'):
        external_resources.append(script.get('src'))
# Finally send the results to a json file
with open('external_resources.json', 'w') as outfile:
    json.dump(external_resources, outfile)


# Enumerate the page's hyperlinks and identify the location of the "Privacy Policy" page
# Initialising needed variables
total_links = 0
privacy_policy_url = None
# Find all 'a' tags that have a href attribute inside the HTML
for a in soup.find_all('a', href=True):
    # Increase the variable by 1 each iteration
    total_links += 1
    # Checks each text to see if it matches privacy policy
    if a.text.lower() == 'privacy policy':
        # If so assign href attribute and store in variable
        privacy_policy_url = a['href']
        break
print("Total number of hyperlinks: ", total_links)

# Scrape the Privacy Policy page and produce a case-insensitive word count
if privacy_policy_url:
    if not privacy_policy_url.startswith("http"):
        # If relative to the main page we append the CFC url to the start to make it a full URL and to ensure the get requests work correctly
        privacy_policy_url = "https://cfcunderwriting.com" + privacy_policy_url
    response = requests.get(privacy_policy_url)
    # Parses the output to HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    # ensure all text is lower case
    text = text.lower()
    # Count how many times each word occurs
    word_counts = Counter(text.split())
    # Send the results to the JSON file
    with open('privacy_policy_word_counts.json', 'w') as outfile:
        json.dump(dict(word_counts), outfile)