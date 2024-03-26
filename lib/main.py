import json
import mistake
import os
import random
from words import Words
import errors
import output_german

path = os.path.dirname(os.path.realpath(__file__))


class Hangman:
    def __init__(self):
        self.Add = Words(self)
        self.words = self.Add.words
        self.highscore = json.loads(open(f"{path}\\highscore.json").read())['highscore']
        #self.main_menu()
        self.waiting_for_command()


    def print_help(self):
        print(output_german.PRINT_HELP_helpForUser)

    def waiting_for_command(self):
        while True:
            print(output_german.WAITING_FOR_COMMAND_shortHelp)
            entry = input(output_german.WAITING_FOR_COMMAND_entry)

            if entry == "play":
                self.play()
            elif entry == "add":
                self.clear_terminal()
                self.Add.user_adds()
            elif entry == "help":
                self.print_help()
            elif entry == "exit":
                exit()
            elif entry == "\n" or entry == "":
                continue
            elif entry== "edit":
                self.Add.edit()
            elif entry == "overview":
                for i in range(len(self.words)):
                    print("{}. {}".format(i+1, self.words[i]))
            else:
                print(output_german.WAITING_FOR_COMMAND_error)

    def play(self):
        run= True
        score = 0
        while run:
            wordnumber = random.randint(0, len(self.words)-1)
            word = self.words[wordnumber]
            guessedCharsAndWords = []
            self.clear_terminal()
            Fehler = 0
            while True:

                unknown= 0
                for letter in word: # WATCHING HOW MANY LETTER ARE UNDEFINED
                    if letter in guessedCharsAndWords:
                        print(letter, end="")
                    else:
                        print("_ ", end="")
                        unknown+=1

                if unknown == 0:
                    print()
                    print()
                    print(output_german.PLAY_guessWordRight.format(word))
                    score +=1
                    if score >= self.highscore:
                        self.highscore = score
                        with open(f'{path}\\highscore.json') as f:
                            data = json.load(f)
                        data["highscore"] = self.highscore
                        with open(f'{path}\\highscore.json', 'w') as outfile:
                            json.dump(data, outfile)
                        print(output_german.PLAY_brokenHighscore.format(self.highscore))
                    break

                print()

                entry = input(output_german.PLAY_entry).upper().replace("AE","Ä").replace("OE","Ö").replace("UE","Ü")

                # IF ENTRY = COMMAND
                if entry.startswith("/EXIT"):
                    self.clear_terminal()
                    run = False
                    break

                elif entry.startswith("/HELP"):
                    self.print_help()
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

                if not word.find(entry) == -1:
                    already_exists = 0
                    for letter in entry:
                        if letter in guessedCharsAndWords:
                            already_exists += 1
                            continue
                        guessedCharsAndWords.append(letter)

                    if already_exists >= len(entry):
                        print(output_german.PLAY_entryAlwaysExists)
                    print(output_german.PLAY_guessLetterRight)
                else:
                    print(output_german.PLAY_guessLetterWrong)
                    Fehler+=1
                    self.print_mistake(Fehler)
                    if Fehler >= 11:
                        print(output_german.PLAY_lose.format(word))
                        break



    def print_mistake(self, misstake):
        if misstake == 1:
            print(mistake.eins)
        elif misstake ==2:
            print(mistake.zwei)
        elif misstake == 3:
            print(mistake.drei)
        elif misstake == 4:
            print(mistake.vier)
        elif misstake == 5:
            print(mistake.fünf)
        elif misstake == 6:
            print(mistake.sechs)
        elif misstake == 7:
            print(mistake.sieben)
        elif misstake == 8:
            print(mistake.acht)
        elif misstake == 9:
            print(mistake.neun)
        elif misstake == 10:
            print(mistake.zehn)
        elif misstake == 11:
            print(mistake.elf)
        else:
            raise errors.InvalidNumber()

    def clear_terminal(self):
        pass


if __name__ == "__main__":
    Hangman()
