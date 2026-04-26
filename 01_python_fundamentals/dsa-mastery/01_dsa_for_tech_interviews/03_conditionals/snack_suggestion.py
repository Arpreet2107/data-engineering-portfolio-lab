snack = input("What snack do you want to eat?").lower()
print(f"User has choosen {snack} as their snack")#for validation 

if snack == "cookies" or snack =="samosa":
    print(f"{snack} is a great choice! Your snack will be ready in 5 minutes.")
elif snack == "chips":  
    print("Chips is a great choice, but currently we are out of stock. Please choose another snack.")
else:
    print("Sorry, the selected snack is not available. Please choose another snack from the menu.")

