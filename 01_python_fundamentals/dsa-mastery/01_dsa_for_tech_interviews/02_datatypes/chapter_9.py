essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices= {"cloves","ginger","black pepper"}
#union of two sets gives us a set of all unique elements from both sets
all_spices = essential_spices | optional_spices #union of two sets
all_spices1 = essential_spices.union(optional_spices) #union method to combine two sets
print(f"All spices (using | operator): {all_spices}")
print(f"All spices (using union method): {all_spices1}")

#intersection of two sets gives us a set of common elements from both sets
common_spices = essential_spices & optional_spices 
common_spices1 = essential_spices.intersection(optional_spices) #intersection method to find common elements between two sets
print(f"Common spices (using & operator): {common_spices}")
print(f"Common spices (using intersection method): {common_spices1}")

#difference of two sets gives us a set of elements that are in the first set but not in the second set
only_essential = essential_spices - optional_spices
only_essential1 = essential_spices.difference(optional_spices) #difference method to find elements that are in the first set but not in the second set
print(f"Only essential spices (using - operator): {only_essential}")
print(f"Only essential spices (using difference method): {only_essential1}")

#membership testing to check if an element is in a set
print(f"Is cardamom an essential spice? {'cardamom' in essential_spices}")
print(f"Is cloves an essential spice? {'cloves' in essential_spices}")

#frozenset is an immutable version of a set, it cannot be modified after creation
frozen_spices = frozenset(["cardamom","ginger","cinnamon"])
print(f"Frozen spices: {frozen_spices}")