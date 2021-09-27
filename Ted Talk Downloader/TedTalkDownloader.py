import requests  # getting content of the TED's url
from bs4 import BeautifulSoup  # web scraping
import re  # regular expression pattern matching
import sys  # argument parsing

###### Exception handling ######

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# url = "https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection"  # Hardcoded url for example

r = requests.get(url)

print("Download about to start...")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.find_all("script"):
    if (re.search("talkPage.init", str(val))) is not None:
        result = str(val)
result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

print("Downloading video from ..." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/")) - 1].split('?')[0]

print("Sorting video in ..." + file_name)

r = requests.get(mp4_url)

with open(file_name,'wb') as f:
    f.write(r.content)


print("Download finished")