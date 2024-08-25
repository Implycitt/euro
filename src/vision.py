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

def words_format(read_words: list) -> list:
    word_string = ""
    for i in read_words:
        i = i.replace(',', '.')
        i = i.replace(' ', '')
        if (len(i) <= 4  and i[-1] != '.'): 
            i += '.'
        if (i[-1].isalpha()):
            i += '|'
        word_string += i
    words = word_string.split('|')
    return words

read_words = read(image_path)[5:-30]
words = words_format(read_words)
for i in words:
    print(i)
