import errors
import json
from mistake import mistakes
import os


class Files:
    def __init__(self, main):
        self.words = []
        self.main = main
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.highscore = 0
        self.highscore = self.getHighscoreFromFile()
        self.readWordFile()

    def addWordToFile(self, word):
        with open(f"{self.path}\\words.txt", "a") as file:
            file.write("{}\n".format(word.replace(" ","")))
            file.close()
        self.readWordFile()

    def readWordFile(self):
        self.words = []
        with open(f"{self.path}\\words.txt", "r") as file:

            for line in file.readlines():
                word = line.replace("\n", "").upper()
                self.words.append(word.replace("Ã¶", "Ü").replace("Ã„", "Ä").replace("ÃŒ", "Ü").replace("Ã–", "Ö"))
                file.close()

    def updateWordsFile(self):
        with open(f"{self.path}\\words.txt", "w") as file:
            for i in self.words:
                file.write("{}\n".format(i.replace(" ", "").repalce("Ï¿½", "Ö").replace("Ï¿Ï¿Ï¿½", "Ä").replace("Ï¿Ï¿½", "Ü")))

    def getWords(self):
        return self.words

    def getHighscoreFromFile (self):
        with open(f'{self.path}\\highscore.json') as f:
            data = json.load(f)
            f.close()
        data["highscore"] = self.highscore
        return self.highscore

    def writeHighscoreToFile(self, highscore=None):
        if highscore == None:
            print(highscore)
            highscore = self.main.highscore

        currentHighscore = self.getHighscoreFromFile()

        if currentHighscore >= highscore:
            raise errors.HighscoreInvalid(highscore=highscore, oldHighscore=currentHighscore)

        with open(f'{self.path}\\highscore.json') as f:
            data = json.load(f)
        data["highscore"] = highscore
        with open(f'{self.path}\\highscore.json', "w") as f:
            json.dump(data, f)

    def print_mistake(self, mistake):
        if mistake < 0 or mistake > 11:
            raise errors.InvalidNumber(mistake)
        print(mistakes[mistake])

    def deleteChois(self, chois):
        self.words.remove(self.words[chois])
        self.updateWordsFile()
        self.getWords()
