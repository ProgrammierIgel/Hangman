import random
import Fehler
import json
import keyboard
import os
import sys
import time
from Words import Words


async def keys(cancel):
    while not cancel:
        if keyboard.wait("<Right>"):
            print("runter")
        time.sleep(0.1)


class Hangman:
    def __init__(self):
        self.Add = Words(self)
        self.words = self.Add.words
        self.highscore = json.loads(open("highscore.json").read())['highscore']
        self.main_menu()
        self.waiting_for_command()

    def main_menu(self):
        cancel = True
        keys(True)
        time.sleep(10)
        cancel= False
        sys.stdout.write("\r{0}>".format("="))
        sys.stdout.flush()

    def print_help(self):
        print("""HILFE FÜR USER:
         - um zu beenden: 'exit'
         - für die Hilfe: 'help'
         - um Wörter hinzuzufügen: 'add'
         - um zu spielen: 'play'
         - Wörter bearbeiten: 'edit'
         
         PLAY: Man hat 11 Versuche. Bitte gib das Wort oder einzelne oder Wortgruppen Buchstaben ein.
         Eingaben werden in Großbuch umgewandelt!
         um den Spielmodus zu beenden :'/exit'
         
         ADD: Modus um Wörter hinzuzufügen.
         Wörter werden automatisch in Wörter, verwandelt bei denen alle Buchstaben groß geschrieben sind!
         Hinzufügenmodus beenden mit: '/exit'.
         
         EDIT: Gib die Nummer des Wortes ein welches du bearbeiten möchtest.
         Die Wörter, welche zur Auwahl stehen werden dir angezeigt.
         Gib nun das korigierte Wort ein. Bestätige nun deine Eingabe mit einem Ja!
         Um den Bearbeitungsmodus zu verlassen gib bitte '/exit' ein!. 
         
         OVERVIEW: Zeigt alle vorhnadenen Wörter. 
         
         EXIT: Beendet das Programm.  
         
         HELP: Zeigt die Hilfe an.
              
         """)

    def waiting_for_command(self):
        while True:
            print("Für die Hilfe: 'help'")
            print("Zum beenden: 'exit'")
            entry = input("Bitte gib einen Befehl ein! \n >>> ")

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
                print("FEHLER: Eingabe ungültig!\n Für die Hilfe gib bitte 'help' ein !")

    def play(self):
        run= True
        score = 0
        while run:
            wordnumber = random.randint(0, len(self.words)-1)
            word = self.words[wordnumber]
            geraten = []
            Fehler = 0
            self.clear_terminal()
            while True:

                unknown= 0
                for letter in word:
                    if letter in geraten:
                        print(letter, end="")
                    else:
                        print("_ ", end="")
                        unknown+=1
                if unknown ==0:
                    print()
                    print()
                    print("GEWONNEN")
                    score +=1
                    if score >= self.highscore:
                        self.highscore = score
                        with open('highscore.json') as f:
                            data = json.load(f)
                        data["highscore"] = self.highscore
                        with open('highscore.json', 'w') as outfile:
                            json.dump(data, outfile)
                        print("SUPER! Du hast deinen Highscore geknackt! Highscore: {}".format(self.highscore))
                    break

                print()
                entry = input("Bitte gib einen Buchstaben oder das Wort ein. Zu Abbrechen '/exit'! Hilfe: '/help'  Score: '/score' Highscore: '/highscore' \n").upper().replace("AE","Ä").replace("OE","Ö").replace("UE","Ü")
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
                    print("DU hast gerade {} Punkte.".format(score))
                    continue

                elif entry.startswith("/HIGHSCORE"):
                    print("Dein Highscore beträgt gerade {} Punkte!".format(self.highscore))
                    continue

                elif entry == word:
                    print("Prima! Du hast gewonnen!")
                    print("Das Wort war: {}".format(word))
                    score =score+1
                    if score >= self.highscore:
                        self.highscore = score
                        with open('highscore.json') as f:
                            data = json.load(f)
                        data["highscore"] = self.highscore
                        with open('highscore.json', 'w') as outfile:
                            json.dump(data, outfile)

                        print("SUPER! Du hast deinen Highscore geknackt! Highscore: {}".format(self.highscore))

                    break
                elif entry in geraten:
                    print("Eingabe schon vorhanden!")
                    continue
                geraten.append(entry)
                if not word.find(entry) == -1:
                    always_exists = 0
                    for letter in entry:
                        if letter in geraten:
                            always_exists += 1
                            continue
                        else:
                            geraten.append(letter)

                    if always_exists >= len(entry):
                        print("Eingabe schon vorhanden")
                    else:
                        print("Super")
                else:
                    print("Leider Falsch!")
                    Fehler+=1
                    self.print_misstake(Fehler)
                    if Fehler >= 11:
                        print("GAME OVER")
                        print("Du wurdest gehängt")
                        print("Das Wort war: {}".format(word))
                        break



    def print_misstake(self, misstake):
        if misstake == 1:
            print(Fehler.eins)
        elif misstake ==2:
            print(Fehler.zwei)
        elif misstake == 3:
            print(Fehler.drei)
        elif misstake == 4:
            print(Fehler.vier)
        elif misstake == 5:
            print(Fehler.fünf)
        elif misstake == 6:
            print(Fehler.sechs)
        elif misstake == 7:
            print(Fehler.sieben)
        elif misstake == 8:
            print(Fehler.acht)
        elif misstake == 9:
            print(Fehler.neun)
        elif misstake == 10:
            print(Fehler.zehn)
        elif misstake == 11:
            print(Fehler.elf)
        elif misstake == 0:
            print("""
            
            
            
            
            """)

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    Hangman()

