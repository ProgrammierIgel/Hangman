class InvalidNumber(Exception):
    "The mistakes were printed with entry {entry} but that's out of range"
    def __init__(self, entry):
        super().__init__(f"InvalidNumber: The mistakes were printed with entry {entry} but that's out of range")

class HighscoreInvalid (Exception):
    "HighscoreInvalid: The Highscore is equal or less than the highscore befor!"
    def __init__(self, highscore, oldHighscore):
        super().__init__(f"HighscoreInvalid: The Highscore is equal or less than the highscore befor! New Highscore {highscore} Old Highscore: {oldHighscore}")
