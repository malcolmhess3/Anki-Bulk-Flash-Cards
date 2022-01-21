import requests
from bs4 import BeautifulSoup

def getDefinition(word):
    res = requests.get("https://jisho.org/api/v1/search/words?keyword="+word)
    if(res.ok):
        try:
            definedList = res.json()["data"][0]["senses"][0]
            jpReadingList = res.json()["data"][0]["japanese"][0]

            englishReading = definedList["english_definitions"][0]
            if(len(definedList["english_definitions"]) > 2):
                englishReading += ", " + definedList["english_definitions"][1]
            
            jpReading = jpReadingList["reading"]
            partSpeech = definedList["parts_of_speech"][0]
        except:
            print("Something is wrong with ", word)
            return("None", "None", "None")

        return (englishReading, jpReading, partSpeech)

def getExampleSentences(word):
    res = requests.get("https://jisho.org/search/" + word + "%23sentences")
    if(res.ok):
        soup = BeautifulSoup(res.content, "html.parser")
        try:
            firstSentence = soup.find("li", "entry sentence clearfix")
            jpSentence = firstSentence.find("ul", "japanese_sentence japanese japanese_gothic clearfix")
            jpSentencelines = jpSentence.find_all("li")
        except AttributeError:
            return ("None", "None")

        comp = ""
        for line in jpSentencelines:
            furi = line.find(class_="furigana")
            if (furi):
                comp+= " " + line.find(class_="unlinked").get_text()
                comp+= "[" + furi.get_text() + "]"
            else:
                comp += line.get_text()

        return (comp, firstSentence.find(class_='english').get_text())