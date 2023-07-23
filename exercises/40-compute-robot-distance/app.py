def compute_robot_distance(movements):
    x, y = 0, 0
    for movement in movements:
        direction, steps = movement[0], int(movement[1])
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    distance = ((x ** 2) + (y ** 2)) ** 0.5

    return int(distance)

def main():
    input_data = input("Enter movements (e.g., UP 5 DOWN 3 LEFT 3 RIGHT 2): ")
    movements_list = [movement.split() for movement in input_data.split()]

    distance = compute_robot_distance(movements_list)

    print(distance)

if __name__ == "__main__":
    main()


