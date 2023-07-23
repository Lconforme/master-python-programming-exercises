def square_odd_numbers(numbers):
    numbers = [int(num) for num in numbers.split(",")]

    squared_odd_numbers = [num**2 for num in numbers if num % 2 != 0]

    return squared_odd_numbers

def main():
    numbers_input = input("Enter a sequence of comma-separated numbers: ")

    squared_odd_numbers = square_odd_numbers(numbers_input)


    print(",".join(map(str, squared_odd_numbers)))

if __name__ == "__main__":
    main()
