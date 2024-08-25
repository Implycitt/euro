import cv2
import easyocr

words = []
image_path = "../input/terms.jpg"

def read(image_path: str) -> list:
    read_words = []
    image = cv2.imread(image_path)
    reader = easyocr.Reader(['en'])
    text = reader.readtext(image)
    read_words = [i[1] for i in text]
    return read_words

def get_words(garbage: list) -> list:
    copy = False 
    out = []
    for i in garbage:
        if "Comprehension Questions".lower() in i.lower():
            return out
        if copy:
            out.append(i)
        if "(1 point each)" in i.lower():
            copy = True
    return out 

def words_format(read_words: list) -> list:
    word_string = ""
    for i in read_words:
        i = i.replace(',', '.')
        if (len(i) <= 4  and i[-1] != '.'): 
            i += '.'
        if (i[-1].isalpha()):
            i += '|'
        word_string += i
    words = word_string.split('|')
    return words

def output_words(words: list) -> None:
    with open("../output/wordlist.txt", 'w') as outfile:
        for word in words:
            outfile.write(word+'\n')

def vision(image_path: str) -> None:
    read_words = read(image_path)
    readable = get_words(read_words)
    words = words_format(readable)
    output_words(words)

