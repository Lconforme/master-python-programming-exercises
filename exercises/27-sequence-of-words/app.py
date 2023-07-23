def sort_words(input_str):
    words_list = input_str.split(',')

    sorted_words = sorted(words_list)

    return sorted_words

def main():
    input_str = input("Enter a comma-separated sequence of words: ")

    sorted_words = sort_words(input_str)

    print(",".join(sorted_words))

if __name__ == "__main__":
    main()
