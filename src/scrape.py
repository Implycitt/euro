from bs4 import BeautifulSoup
from selenium import webdriver

raw_url = "https://www.google.com/search?q="

def construct_url(word: str) -> str:
    words = word.split(" ")
    url = raw_url
    for part in words:
        if part == "&":
            part = "%26"
        url += f"{part}+"
    url += "ap+euro+definition"
    return url

def get_definition(word: str, driver) -> str:
    url = construct_url(word)
    print(url)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    definition = soup.findAll("span", attrs={"class": "hgKElc"})
    if definition == []:
        return ""
    ret = (definition[1].text).replace('.', '')
    if ("Advanced Placement" in definition[1].text):
        return definition[0].text.replace('.', '')
    return ret.lstrip()

def get_all(words_list: dict, driver) -> list:
    definitions = []
    for word in words_list.values():
        definitions.append(get_definition(word, driver))
    return definitions

def get_words() -> dict:
    file = open("../output/wordlist.txt", 'r')
    words = file.read().split('\n')
    words_dict = dict()
    for i in words[:-1]:
        num, word = i.split('.')
        words_dict[int(num)] = word

    words_dict = dict(sorted(words_dict.items()))
    words_dict = fix(words_dict)
    words_dict = dict(sorted(words_dict.items()))
    return words_dict

def fix(d: dict) -> dict:
    keys = list(d.keys())
    last = keys[-1]
    slargest = keys[-2]
    s1 = sum(keys[:-1])
    s2 = int(slargest*(slargest+1)/2)
    difference = abs(s2-s1)
    d[difference] = d[last]
    del d[last]
    return d

def scrape() -> None:
    driver = webdriver.Chrome()
    outfile = open("../output/final.txt", 'w', encoding="utf-8")
    words = get_words()
    definitions = get_all(words, driver)
    for pointer in range(1, len(words)+1):
        text = f"{pointer}. {words[pointer]}  -  {definitions[pointer-1]}\n" 
        outfile.write(text)

    driver.close()

