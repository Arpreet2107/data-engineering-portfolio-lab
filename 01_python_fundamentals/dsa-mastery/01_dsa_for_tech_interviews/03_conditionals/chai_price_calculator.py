chai_size = input("Please enter the size of chai you want(Small/Medium/Large): ").lower()
print(f"{chai_size} chai has been selected.") #for validation   

if chai_size == "small":
    print("The price of small chai is 10Rupees.")
elif chai_size == "medium":
    print("The price of medium chai is 15Rupees.")
elif chai_size == "large":
    print("The price of large chai is 20Rupees.")
else:
    print("Unknown cup size selected. Please select the valid cup size from the menu.")