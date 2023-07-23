def divisable_binary(binary_numbers):
    binary_numbers_list = binary_numbers.split(',')

    divisible_by_five = [binary for binary in binary_numbers_list if int(binary, 2) % 5 == 0]

    return ",".join(divisible_by_five)

def main():
    input_str = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

    print(divisable_binary(input_str))

if __name__ == "__main__":
    main()
