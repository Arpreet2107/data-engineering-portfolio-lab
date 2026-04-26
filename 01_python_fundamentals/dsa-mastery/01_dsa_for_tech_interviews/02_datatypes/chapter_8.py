ingridients = ["water","milk","black tea"]
print(ingridients[0])
ingridients.append("sugar")#append method is used to add an element at the end of the list
print(f"Ingridients after appending sugar: {ingridients}")
ingridients.insert(1,"ginger")#insert method is used to add an element at a specific index in the list
print(f"Ingridients after inserting ginger at index 1: {ingridients}")
ingridients.remove("milk")#remove method is used to remove an element from the list
print(f"Ingridients after removing milk: {ingridients}")

spice_options = ["cinnamon","cardamom","clove"]
chai_ingridients = ["water","milk"]
chai_ingridients.extend(spice_options)#extend method is used to add multiple elements to the end of the list
print(f"Chai ingridients after extending with spice options: {chai_ingridients}")

chai_ingridients.insert(2,"black tea")#insert method is used to add an element at a specific index in the list
print(f"Chai ingridients after inserting black tea at index 2: {chai_ingridients}")

last_added = chai_ingridients.pop()#pop method is used to remove and return the last element of the list
print(f"Last added spice removed: {last_added}")
print(f"Chai ingridients after popping last added spice: {chai_ingridients}")

print(f"Chai: {chai_ingridients}")
chai_ingridients.reverse()
print(f"Chai ingridients after reversing: {chai_ingridients}")
chai_ingridients.sort()#sort method is used to sort the elements of the list in ascending order
print(f"Chai ingridients after sorting: {chai_ingridients}")

sugar_levels = [1,2,3,4,5]
print(f"maximum sugar level: {max(sugar_levels)}")#max function is used to find the maximum element in the list
print(f"minimum sugar level: {min(sugar_levels)}")#min function is usedto find the minimum element in the list

#operator overloading allows us to use the + operator to concatenate two lists
base_liquids = ["water","milk"]
extra_flavour = ["ginger"]
full_liquid_mix = base_liquids + extra_flavour#concatenation of two lists
print(f"Full liquid mix: {full_liquid_mix}")

#operator overloading allows us to use the * operator to repeat a list
strong_brew = ["black tea", "water"] * 3  # repeating the list 3 times
print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON") #bytearray is a mutable sequence of bytes
raw_spice_data = raw_spice_data.replace(b"CINNA",b"CARD")#replace method is used to replace a specified value with another value in the bytearray
print(f"Bytes: {raw_spice_data}")

