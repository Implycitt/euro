from bs4 import BeautifulSoup
from selenium import webdriver

raw_url = "https://www.google.com/search?q="

driver = webdriver.Chrome()

for word in open("../input/words.txt", 'r'):
    url = f"{raw_url}{word.rstrip()}+ap+euro+definition"
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    quotes = soup.findAll("span", attrs={"class": "hgKElc"})
    print(quotes)

driver.close()
