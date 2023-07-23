def generate_list_and_tuple(numbers_str):
    numbers_list = numbers_str.split(',')

    numbers_tuple = tuple(numbers_list)

    return numbers_list, numbers_tuple

input_str = input("Enter a sequence of comma-separated numbers: ")

result_list, result_tuple = generate_list_and_tuple(input_str)

print(result_list)
print(result_tuple)
