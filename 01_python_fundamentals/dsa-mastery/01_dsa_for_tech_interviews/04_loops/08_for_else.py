staff = [("John", 25), ("Jane", 30), ("Doe", 35)]

for name,age in staff:
    if age <=30:
        print(f"{name} is eligible to manage the staff ")
        break
else:
    print(f"No eligible staff found to manage the staff") 