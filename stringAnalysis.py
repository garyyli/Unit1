#Gary Li
#9/7/17
#stringAnalysis.py

sentence = input('Enter a sentence: ')
sentence = sentence.lower()

totalCharacters = int(len(sentence))
spaces = int(sentence.count(' '))
totalLetters = totalCharacters - spaces
totalWords = spaces + 1

print('Your sentence has', totalWords, 'words and', totalCharacters, 'characters and', totalLetters, 'letters')

character = input('Enter a character to search for: ')
print('Your sentence has', sentence.count(character), 'of the character', character)

word = input('Enter a word to search for: ')
print('Your sentence has', sentence.count(word), 'of the word', word)