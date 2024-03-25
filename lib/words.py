import os

path = os.path.dirname(os.path.realpath(__file__))

class Words:
    def __init__(self, main):
        self.words = []
        self.read()
        self.main = main

    def add(self, word):
        with open(f"{path}\\words.txt", "a") as file:

            file.write("{}\n".format(word.replace(" ","")))
            file.close()
        self.read()

    def read(self):
        self.words = []
        with open("words.txt", "r") as file:

            for line in file.readlines():
                word = line.replace("\n", "").upper()
                self.words.append(word.replace("Ã¶", "Ü").replace("Ã„", "Ä").replace("ÃŒ", "Ü").replace("Ã–", "Ö"))
                file.close()

    def user_adds(self):
        run = True
        while run:
            entry = input("Bitte gib ein neues Wort ein! ZU Abrechen gib bitte '/exit' ein! Für Hilfe: '/help' \n >>>")
            if entry == "/exit":
                run = False
            elif entry == "/help":
                self.main.print_help()
            elif entry in self.words:
                print("wort schon vorhanden!")
            else:
                self.add(str(entry))
                print(self.words)

    def edit(self):
        while True:
            for i in range(len(self.words)):
                print("{}: {}".format(i+1, self.words[i]))
            entry = input("Bitte gib die Nummer des Wortes ein, welches du bearbeiten möchtest! Um zu beenden :'/exit'\n")
            if entry.startswith("/exit"):
                break
            if entry.startswith("/help"):
                self.main.print_help()
                continue
            if entry == "\n":
                continue
            try:
                chois = int(entry)-1
            except:
                print("Ungültige Eingabe!")
                print()
                continue
            print()
            print("{}".format(self.words[chois]))

            new = input("Bitte gib das korigierte Wort jetzt ein or '/delete' zum löschen!\n>")
            if not new.startswith("/delete"):
                new = new.upper()
                print(new)
                yn = input("Bist du dir sicher? [y]/n :")
            else:
                yn = input("Bist du dir sicher. dass du {} löschen möchtest? [y]/n :".format(self.words[chois]))
            if yn == "":
                if new.startswith("/delete"):
                    self.words.pop(chois)
                    self.update()
                else:
                    self.words[chois] = new
                    self.update()
                print("Änderung wurde erfolgreich gespeichert")
            if yn.lower() == "y" or yn.lower() == "yes" or yn.lower() == "ja" :
                self.words[chois] = new
                self.update()
                print("Änderung wurde erfolgreich gespeichert")
                continue
            else:
                continue

    def update(self):
        with open(f"{path}\\words.txt", "w") as file:
            for i in self.words:
                file.write("{}\n".format(i.replace(" ", "")))
