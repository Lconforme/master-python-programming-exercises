import math

def calculate_Q(D, C=50, H=30):
    Q = math.sqrt((2 * C * D) / H)

    Q = round(Q)

    return Q

def print_formula(D_values):
    result = [calculate_Q(D) for D in D_values]
    return result

def main():
    input_str = input("Enter values of D (comma-separated sequence): ")

    D_values = list(map(int, input_str.split(',')))

    result = print_formula(D_values)

    print(",".join(str(val) for val in result))

if __name__ == "__main__":
    main()

