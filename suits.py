def get_suits():
    suits = set()
    while True:
        try:
            num_suits = int(input("How many suits? "))
            if num_suits < 2:
                raise ValueError("Error, must be at least 2 suits!")
            break
        except ValueError:
            print("Error, must input an integer which is at least 2, not blank or non-numeric!")

    while len(suits) < num_suits:
        suit = input("Input suit: ").strip().title()

        if not suit:
            print("Error, no input!")
            continue

        if ' ' in suit:
            print("Error, must be a single word!")
            continue

        if suit in suits:
            print("Error, duplicate suit!")
            continue

        suits.add(suit)

    print("Thank you. The suits are:")
    print(", ".join(suits))


if __name__ == "__main__":
    get_suits()
