# Program will let user play hangman
import random

class Hangman:

    def __init__(self, wordList):
        self.usedLetters = []
        self.wordList = wordList
        self.strikes = 0
        self.word = ''
        self.currentWord = ''

    def randomWord(self):
        return self.wordList[random.randrange(len(self.wordList))]

    def resetGame(self):
        self.usedLetters = []
        self.strikes = 0
        self.word = self.randomWord()
        self.currentWord = ''
        for i in range(len(self.word)):
            if self.word[i:i+1] == " ":
                self.currentWord += " "
            else:
                self.currentWord += '_'

    def guessLetter(self, userInput):
        userInput = userInput.casefold()
        if self.strikes == 6:
            self.currentWord = self.getWord()
            return "You already lost!"
        elif self.currentWord == self.getWord():
            return "You already won!"
        elif len(userInput) == 1:
            for x in self.usedLetters:
                if x == userInput:
                    return "Repeat"
            count = 0
            for i in range(len(self.word)):
                if userInput == self.word[i: i + 1].casefold():
                    self.currentWord = self.currentWord[:i] + self.getWord()[i:i+1] + self.currentWord[i+1:]
                    count += 1
            if self.word == self.currentWord:
                        return "You won!"
            if count == 0:
                self.strikes += 1
            elif count > 0:
                self.usedLetters.append(userInput)
                return "Correct"
            if self.strikes == 6:
                self.usedLetters.append(userInput)
                self.currentWord = self.getWord()
                return "You lose!"
            self.usedLetters.append(userInput)
            return "Incorrect"
        elif len(userInput) > 1:
            if userInput == self.word.casefold():
                self.currentWord = self.word
                return "You won!"
            else:
                self.strikes += 1
                if self.strikes == 6:
                    self.currentWord = self.getWord()
                    return "You lose!"
                return "Incorrect"

    def getUsedLetters(self):
        return self.usedLetters

    def getStrikes(self):
        return self.strikes

    def getWord(self):
        return self.word

    def getCurrentWord(self):
        formattedCurrentWord = ''
        for i in range (len(self.currentWord)):
            formattedCurrentWord += self.currentWord[i:i+1] + ' '
        return formattedCurrentWord

    def getWordList(self):
        return self.wordList
