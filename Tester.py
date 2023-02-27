from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = "https://www.dictionary.com/list/s/68"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
next_page = soup.find_all("li",{"class":"vEZXlqxHKaa99UmuL3gA"})
next_page = next_page[2].find("a")
print(next_page)