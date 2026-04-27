flavours = ["Ginger","Out of stock","Lemon","Discontinued","Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break

print(f"Out side of the loop")