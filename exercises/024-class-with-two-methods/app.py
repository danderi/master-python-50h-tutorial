# Your code here
class InputOutString:
    def __init__(self):
        self.txt = ""

    def get_string(self):
        self.txt = input("type your word: ")

    def print_string(self):
        print(self.txt.upper())
        return self.txt.upper()
    
word = InputOutString()
word.get_string()
word.print_string()