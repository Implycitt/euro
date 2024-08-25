from bs4 import BeautifulSoup
from selenium import webdriver

raw_url = "https://www.google.com/search?q="

def get_definition(word: str, driver) -> str:
    url = f"{raw_url}{word.rstrip()}+ap+euro+definition"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    definition = soup.findAll("span", attrs={"class": "hgKElc"})
    if definition == []:
        return ""
    return definition[0].text

def get_all(words_list: list, driver) -> list:
    definitions = []
    for word in words_list:
        definitions.append(get_definition(word, driver))
    return definitions

def get_words() -> list:
    file = open("../output/wordlist.txt", 'r')
    words = file.read().split('\n')
    return [i.split('.')[1] for i in words[:-2]] 

def scrape() -> None:
    driver = webdriver.Chrome()
    outfile = open("../output/final.txt", 'w', encoding="utf-8")
    pointer = 0
    words = get_words()
    definitions = get_all(words, driver)
    for i in range(len(words)):
        text = words[pointer] + ' - ' + definitions[pointer] + '\n'
        outfile.write(text)
        pointer += 1

    driver.close()

