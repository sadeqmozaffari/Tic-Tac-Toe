def show_board(array):
    print("_____________\n")
    for i in range(0, len(array)):
        for item in array[i]:
            print(f"| {item}", end=" ")
        print(f'|', end="")

        print(f"\n", end="")
    print("\n_____________")
