def is_all_digits_even(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

def find_even_digit_numbers(start, end):
    even_digit_numbers = [num for num in range(start, end+1) if is_all_digits_even(num)]

    return even_digit_numbers

def main():
    start = 1000
    end = 3000

    even_digit_numbers = find_even_digit_numbers(start, end)
    print(",".join(map(str, even_digit_numbers)))

if __name__ == "__main__":
    main()
