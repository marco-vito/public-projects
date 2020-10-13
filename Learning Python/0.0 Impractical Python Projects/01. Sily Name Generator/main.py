import nameGenerator


def main():
    print(
        "Welcome to the Medieval Name Generator! For every one of us that's tired to spend hours choosing a name for a "
        "D&D character that will die in one session anyway. Just pick a name at random and then chose everything else "
        "from there.\n")

    while True:
        print("Chose a male or female name, or type in 'exit' to quit the application")
        new_input = input()
        if new_input.lower() == "exit":
            break
        else:
            print(nameGenerator.randomName(new_input))

        print("\n")
        print("You can always try to get a better name")


if __name__ == "__main__":
    main()
