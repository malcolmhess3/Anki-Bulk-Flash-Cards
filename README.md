# Anki Bulk Flash Card Generator

Quickly create Japanese flash cards for Anki using words from a word list.

## How to use:
1. Open wordlist.txt with your favorite text editor 
2. Open your command line interface or type Run CMD
3. navigate to the file  location and run the command
```
python main.py wordList.txt
```

## How it works
The python script reads the given word list and makes an API request to jisho.org to find basic information about the word. It then uses HTML scrapping to find relevant vocabulary and example sentences. Finally the script compiles the information into a single Anki card using the Anki card generator python package. The script exports a file that can be executed to add the cards to Anki.
