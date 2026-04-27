value = 124
remainder = value % 5

if remainder:
    print(f"{value} is not divisible by 5, remainder is {remainder}")

#walrus operator
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
value = 124
if (remainder := value % 5):
    print(f"{value} is not divisible by 5, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]
if(requested_size := input("Enter the chai cup size: ").lower()) in available_sizes:
    print(f"Serving {requested_size} chai cup")
else: 
    print(f"Sorry, we don't have {requested_size} chai cup")

flavors =["masala", "ginger", "cardamom"]

print("Available flavors:",flavors)

while(flavor := input("Enter the flavor you want: "))not in flavors:
    if flavor in flavors:
        print(f"Serving {flavor} chai")
    else:
        print(f"Sorry, we don't have {flavor} chai")

print(f"Serving {flavor} chai")