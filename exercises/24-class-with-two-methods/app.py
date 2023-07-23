class StringModifier:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

def test_string_modifier():
    string_modifier = StringModifier()

    string_modifier.getString()

    print("String in uppercase:")
    string_modifier.printString()

test_string_modifier()
