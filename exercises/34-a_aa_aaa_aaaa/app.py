def computed_value(a):
    a = int(a)

    result = a + (a * 11) + (a * 111) + (a * 1111)

    return result

def main():
    a = input("Enter a digit: ")

    value = computed_value(a)

    print(value)

if __name__ == "__main__":
    main()

