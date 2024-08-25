import scrape, vision
import os

if __name__ == "__main__":
    image_path = "../input/terms.jpg"
    if (os.path.getsize("../output/wordlist.txt") == 0):
        vision.vision(image_path)
    scrape.scrape()
