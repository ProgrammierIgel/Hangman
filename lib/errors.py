class InvalidNumber(Exception):
    "TEST"
    def __init__(self, entry):
        super().__init__(f"The mistakes was printed with entry {entry} but thats out of range")