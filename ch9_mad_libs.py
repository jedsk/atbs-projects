### Project: Mad Libs

### Chapter 9: Mad Libs Project

import re

replaceReg = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

#open text file and read text
htextFile = open("txt2.txt")
textFile = htextFile.read()

#find matched regex
words = replaceReg.findall(textFile)
replacewd = []

#replace tuple with type, input
for key, word in enumerate(words):
    word = word.lower()
    new = input(f'Enter an {word}:')
    word = word.upper()
    newkw = [word, new]
    replacewd.append(newkw)

print(replacewd)

finalphrase = ''

for key, word in replacewd:
    newphrase = re.sub(key, word, textFile, 1)
    textFile = newphrase

finalphrase = textFile
print(finalphrase)

htextFile.close()
htextFile = open("txt2.txt", 'w')
htextFile.write(finalphrase)
htextFile.close()
