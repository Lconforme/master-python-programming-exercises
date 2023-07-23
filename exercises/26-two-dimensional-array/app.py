def two_dimensional_array(X, Y):
    array_2d = []

    for i in range(X):
        row = [i * j for j in range(Y)]
        array_2d.append(row)

    return array_2d

def main():
    input_str = input("Enter two digits (X,Y) separated by a comma: ")

    X, Y = map(int, input_str.split(','))

    array_2d = two_dimensional_array(X, Y)

    for row in array_2d:
        print(row)

if __name__ == "__main__":
    main()
