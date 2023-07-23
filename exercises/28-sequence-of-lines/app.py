def capitalize_lines(input_lines):
    capitalized_lines = [line.upper() for line in input_lines]

    return capitalized_lines

def lines():
    input_lines = []
    while True:
        line = input("Enter a line (press Enter to stop): ")
        if line:
            input_lines.append(line)
        else:
            break

    capitalized_lines = capitalize_lines(input_lines)
    return capitalized_lines

def main():
    capitalized_lines = lines()
    for line in capitalized_lines:
        print(line)

if __name__ == "__main__":
    main()

