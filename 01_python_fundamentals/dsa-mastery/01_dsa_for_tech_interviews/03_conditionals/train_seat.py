seat_type = input("Enter the seat type(Sleeper/AC/General/First Class): ").lower()

match seat_type:
    case "sleeper":
        print("You have selected Sleeper class.")
    case "ac":
        print("You have selected AC class.")
    case "general":
        print("You have selected General class.")
    case "first class":
        print("You have selected First Class.")
    case _:
        print("Invalid seat type selected.")