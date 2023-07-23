class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num

if __name__ == "__main__":
    n = int(input("Enter a number (n): "))
    generator = DivisibleBySevenGenerator(n)
    for num in generator.divisible_by_seven():
        print(num, end=" ")
