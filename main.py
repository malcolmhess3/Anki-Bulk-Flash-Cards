import sys
import genanki
import apiCallHandler
import datetime

# https://jisho.org/api/v1/search/words?keyword=

my_model = genanki.Model(
  1410157755,
  'FirstJapaneseCard',
  fields=[
    {'name': 'sort_field'},
    {'name': 'Word'},
    {'name': 'Parts_of_Speech'},
    {'name': 'enDefinition'},
    {'name': 'jpReading'},
    {'name': 'jpSentence'},
    {'name': 'enSentence'}
  ],
  templates=[
    {
      'name': 'JpRecognition',
      'qfmt': "<div style='font-size: 12px; text-align: center; color: #6699CC'>{{Parts_of_Speech}}</div><div style='font-size: 60px; text-align: center; color: #003366'>{{Word}}</div>",
      'afmt': "{{FrontSide}}<hr id=answer><div style='font-size: 18px; text-align: center; color: #003366'>{{jpReading}}</div><br><div style='font-size: 24px; text-align: center; color: #003366'>{{enDefinition}}</div><br><br><div style='font-size: 28px; text-align: center; color: #003366'>{{furigana:jpSentence}}</div><br><div style='font-size: 14px; text-align: center; color: #000044'>{{enSentence}}</div>",
    },
  ])

my_deck = genanki.Deck(
  2154433122,
  'jpCards')

# create the note card using information from jisho
def makeNote(word):
  print(word)
  time = datetime.datetime
  sortNum =  time.today().strftime(f"%y%m%d_%H%M%S%f")

  enDefinition, jpReading, pos = apiCallHandler.getDefinition(word)
  exampleJp, exampleEn = apiCallHandler.getExampleSentences(word)
  note = genanki.Note(model=my_model, fields=[sortNum, word, pos, enDefinition, jpReading, exampleJp, exampleEn])
  
  return note

# Add a single word to the deck
def addSingle(word):
  outputFileName = "single.apkg"
  my_note = makeNote(word)
  my_deck.add_note(my_note)
  genanki.Package(my_deck).write_to_file(outputFileName)
  print(outputFileName)


# Add multiple words from a text file to the deck
def addFromlist(wordFile):

  file = open(wordFile, "r", encoding="UTF-8")

  outputFileName = "multi.apkg"

  for line in file:
    word = line.strip()
    my_note = makeNote(word)
    my_deck.add_note(my_note)

  genanki.Package(my_deck).write_to_file(outputFileName)
  print(outputFileName)
    
# If main run with text file or with single word
if __name__ == "__main__":
  if sys.argv[1][-4:] == ".txt":
    print ("Reading from Txt document")
    addFromlist(sys.argv[1])
  else:
    addSingle(sys.argv[1])