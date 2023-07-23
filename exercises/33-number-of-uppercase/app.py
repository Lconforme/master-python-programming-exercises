def count_upper_and_lower(sentence):
    num_upper = sum(c.isupper() for c in sentence)
    num_lower = sum(c.islower() for c in sentence)

    return num_upper, num_lower

def main():
    sentence = input("Enter a sentence: ")

    num_upper, num_lower = count_upper_and_lower(sentence)

    print(f"UPPER CASE {num_upper} LOWER CASE {num_lower}")

if __name__ == "__main__":
    main()
