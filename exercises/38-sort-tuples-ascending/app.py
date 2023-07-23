from operator import itemgetter

def sort_tuples_ascending(tuples_list):
    sorted_tuples = sorted(tuples_list, key=itemgetter(0, 1, 2))
    return sorted_tuples

def main():
    input_data = input("Enter tuples (name, age, height) separated by spaces: ")
    tuples_list = [tuple(item.split(',')) for item in input_data.split()]

    sorted_tuples = sort_tuples_ascending(tuples_list)

    print(sorted_tuples)

if __name__ == "__main__":
    main()
