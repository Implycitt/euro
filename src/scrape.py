import requests
from bs4 import BeautifulSoup
from selenium import webdriver

raw_url = "https://www.google.com/search?q="

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

for word in open("../input/words.txt", 'r'):
    url = f"{raw_url}{word}+ap+euro+definition"
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')
    print(soup)
    result = soup.find('div', class_='hgKElc')
    print(result)
    #result = soup.find('div', class_='hgKElc')
    #open("output.txt", 'w').write(result.text)
