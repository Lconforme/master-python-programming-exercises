def remove_duplicate_words(input_str):
    words_list = input_str.split()

    unique_words = list(set(words_list))

    return unique_words

def main():
    input_str = input("Enter a sequence of whitespace-separated words: ")

    unique_words = remove_duplicate_words(input_str)

    unique_words.sort()

    print(" ".join(unique_words))

if __name__ == "__main__":
    main()
