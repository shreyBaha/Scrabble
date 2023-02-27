from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def no_special_chars(s):
  if any(ord(x) > 127 or x.isupper() for x in s) or not s.isalpha() or len(s) < 2: #filtering out things I dont want as dictionary.com includes acronyms names phrases and other such undesirable material that dictionary.com has
    return False
  return True

for i in range(97,123): #print(chr(97)) number to ascii 97 = a
  page_letter = chr(i)
  start_url = f"https://www.dictionary.com/list/{page_letter}" #dictionary.com base everything after is what is appended. cant start at base however must start at /letter
  base_url = "https://www.dictionary.com"
  prev_word = "a"
  while True:
    response = requests.get(start_url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(start_url)
    next_page = soup.find_all("li",{"class":"vEZXlqxHKaa99UmuL3gA"})
    next_page = next_page[2].find("a")
    words = soup.find_all("ul")
    words = words[7].find_all("li")
    for word in words:
      dictionary_file = open("Dic.txt", "a")
      if no_special_chars(word.find("a").string):
        if(page_letter == word.find("a").string[0] and word.find("a").string >= prev_word): #for some reason at the end of a letter's entries the dictionary will include words that aren't from that letter so this breaks out into the next letter if it detects this happening (binary search wouldn't work otherwise)
          dictionary_file.write(word.find("a").string+"\n")
          prev_word = word.find("a").string
        else:
          break;
      dictionary_file.close
    if next_page:
      next_url = next_page.get("href")
      start_url = urljoin(base_url, next_url)
    else:
      break;



#result  = requests.get(url)
#doc = BeautifulSoup(result.text, "html.parser") #print doc.prettify first to see the html
#prices = doc.find_all(text = "$")
#parent = prices[0].parent # there was only one instance of the dollar sign so we go into the first instance of prices
#strong = parent.find("strong") #strong is the html tage that contains the price
#print(strong.string) #.string removes the strong tag
