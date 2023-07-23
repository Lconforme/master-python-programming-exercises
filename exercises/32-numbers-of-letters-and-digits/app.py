def letters_and_digits(sentence):
    num_alphanumeric = sum(c.isalnum() for c in sentence)
    num_letters = sum(c.isalpha() for c in sentence)
    num_digits = num_alphanumeric - num_letters

    return num_letters, num_digits

def main():
    sentence = input("Enter a sentence: ")

    num_letters, num_digits = letters_and_digits(sentence)

    print(f"LETTERS {num_letters} DIGITS {num_digits}")

if __name__ == "__main__":
    main()
