room = {}
room["A"] = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room["B"] = input("Enter status of Room B (Clean/Dirty): ").capitalize()
position = input("Enter vacuum position (A/B): ").upper()
print("\nInitial State:")
print("Room A:", room["A"])
print("Room B:", room["B"])
print("Vacuum Position:", position)
while True:
    print("\n----------------------")
    print("Vacuum is in Room", position)
    if room[position] == "Dirty":
        print("Room", position, "is Dirty")
        print("Vacuum is cleaning...")
        room[position] = "Clean"
        print("Room", position, "is now Clean")
    else:
        print("Room", position, "is already Clean")
        if position == "A":
            position = "B"
        else:
            position = "A"
        print("Vacuum moved to Room", position)
    if room["A"] == "Clean" and room["B"] == "Clean":
        print("\n======================")
        print("Both rooms are CLEAN!")
        print("Vacuum cleaning completed.")
        print("======================")
        break
