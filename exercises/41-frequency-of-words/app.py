def word_frequency(input_string):
    words = input_string.split()
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    sorted_keys = sorted(frequency_dict.keys())

    output = []
    for key in sorted_keys:
        output.append(f"{key}:{frequency_dict[key]}")

    return " ".join(output)

def main():
    input_string = input("Enter a sentence: ")
    result = word_frequency(input_string)
    print(result)

if __name__ == "__main__":
    main()
