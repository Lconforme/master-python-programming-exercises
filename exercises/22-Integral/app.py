def generate_square_dict(n):
    square_dict = dict()

    for i in range(1, n + 1):
        square_dict[i] = i * i

    return square_dict

n = int(input("Enter an integral number (n): "))

result_dict = generate_square_dict(n)
print(result_dict)
