from commands import commands
import os
import output_german
import random
import sys
from files import Files


class Hangman:
    def __init__(self):
        self.Files = Files(self)
        self.words = self.Files.getWords()
        self.main_menu()

    def main_menu(self):
        self.clear_terminal()
        while True:
            print(output_german.MAIN_MENU_shortHelp)
            entry = input(output_german.MAIN_MENU_entry)
            if "play" == entry:
                self.clear_terminal()
                self.play()
                continue
            elif "add" == entry:
                self.clear_terminal()
                self.addWordMenu()
                continue
            elif "help" == entry:
                self.printHelp()
                continue
            elif "exit" == entry:
                break
            elif "" == entry:
                continue
            elif "\n" == entry:
                continue
            elif "edit" == entry:
                self.clear_terminal()
                self.editWordMenu()
                continue
            elif "overview" == entry:
                self.print_overview()
                continue
            print(output_german.MAIN_MENU_error)
            continue
        print(output_german.MAIN_MENU_thanks)
        sys.exit()

    def play(self):
        run = True
        score = 0
        self.clear_terminal()
        while run:
            word = self.words[(random.randint(0, len(self.words)-1))]
            guessedCharsAndWords = []
            mistakes = 0

            while True:
                unknown = self.printWord(word, guessedCharsAndWords)

                if unknown == 0:
                    print(output_german.PLAY_guessWordRight.format(word))
                    score +=1
                    self.checkIfBrokenHighScore(score)
                    break

                entry = input("\n" + output_german.PLAY_entry).upper().replace("AE","Ä").replace("OE","Ö").replace("UE","Ü")

                # IF ENTRY = COMMAND
                if entry.startswith("/EXIT"):
                    self.clear_terminal()
                    run = False
                    break

                elif entry.startswith("/HELP"):
                    self.printHelp()
                    continue

                elif entry == "\n":
                    continue

                elif entry.startswith("/SCORE"):
                    print(output_german.PLAY_pointsNow.format(score))
                    continue

                elif entry.startswith("/HIGHSCORE"):
                    print(output_german.PLAY_highscoreNow.format(self.highscore))
                    continue

                # PLAY GUESS THE WHOLE WORD RIGHT
                elif entry == word:
                    # WILL BE CHECKED AHEAD
                    for letter in word:
                        if letter in guessedCharsAndWords:
                            continue
                        guessedCharsAndWords.append(letter)
                    continue

                # PLAY GUESS LETTER THE SAME LETTER OR WORD TWICE
                elif entry in guessedCharsAndWords:
                    print(output_german.PLAY_entryAlwaysExists)
                    continue

                # APPEND LETTER
                guessedCharsAndWords.append(entry)

                if word.find(entry) != -1:
                    already_exists = 0
                    for letter in entry:
                        if letter in guessedCharsAndWords:
                            already_exists += 1
                            continue
                        guessedCharsAndWords.append(letter)

                    if already_exists >= len(entry):
                        print(output_german.PLAY_entryAlwaysExists)
                    print(output_german.PLAY_guessLetterRight)
                    continue

                print(output_german.PLAY_guessLetterWrong)
                mistakes+=1
                self.Files.print_mistake(mistakes)
                if mistakes >= 11:
                    print(output_german.PLAY_lose.format(word))
                    break

    def print_overview(self):
        for key, word in enumerate(self.Files.words):
            print("{}.: {}".format(key+1, word))

    def clear_terminal(self):
        os.system("clear")


    def checkIfBrokenHighScore(self, score):
        if score > self.Files.highscore:
            self.Files.writeHighscoreToFile(score)
            self.Files.getHighscoreFromFile()

    def printWord(self, word, guessedCharsAndWords):
        unknown = 0
        word.replace("Ï¿Ï¿Ï¿½", "Ä")
        for letter in word: # WATCHING HOW MANY LETTER ARE UNDEFINED
            if letter in guessedCharsAndWords:
                print(letter, end="")
                continue
            print("_ ", end="")
            unknown += 1
        return unknown

    def printHelp(self):
        print(output_german.PRINT_HELP_helpForUser)

    def addWordMenu(self):
        while True:
            entry = input(output_german.ADDWORDMENU_entry_old_word)
            if entry == "/exit":
                break
            elif entry == "/help":
                self.printHelp()
            elif entry in self.words:
                print(output_german.ADDWORDMENU_word_always_exists)
            else:
                self.Files.addWordToFile(entry)

    def editWordMenu(self):
        while True:
            self.clear_terminal()
            self.print_overview()
            entry = input(output_german.ADDWORDMENU_entry_old_word)

            if entry.startswith("/exit"):
                break
            elif entry.startswith("/help"):
                self.main.print_help()
                continue
            elif entry == "\n":
                continue

            try:
                chois = int(entry) - 1
            except:
                print(output_german.EDITWORDMENU_error + "\n")
                continue

            print("\n{}".format(self.words[chois]))

            newWordEntry = input(output_german.EDITWORDMENU_entry_new_word)

            if newWordEntry.startswith("/delete"):
                yesNoPrompt = input(output_german.EDITWORDMENU_shure_to_delete_word.format(self.words[chois]))

                if yesNoPrompt in commands["editWordMenu"]["accept"]:
                    self.Files.deleteChois(chois)
                    print(output_german.EDITWORDMENU_save_sucessfully)
                continue
            newWordEntry = newWordEntry.upper()
            print(newWordEntry)
            yesNoPrompt = input(output_german.EDITWORDMENU_shre_to_apply)
            if yesNoPrompt in commands["editWordMenu"]["accept"]:
                self.words[chois] = newWordEntry
                self.Files.updateWordsFile()
                print(output_german.EDITWORDMENU_save_sucessfully)
                continue


if __name__ == "__main__":
    Hangman()
