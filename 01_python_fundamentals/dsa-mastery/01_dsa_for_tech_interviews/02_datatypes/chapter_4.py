is_boiling = True
stir_count = 5 
total_actions = stir_count + is_boiling # True is treated as 1 in arithmetic operations 
# and this is known as implicit type conversion or type coercion. 
# So, total_actions will be 6 (5 + 1 ). 
# upcasting happens when a smaller data type is converted to a larger data type.
# In this case, the boolean value True is implicitly converted to the integer value 1,
# which is then added to the stir_count (5) to get the total_actions (6).
print(f"Total_actions: {total_actions}")


milk_present = 0 #no milk 
print(f"Is milk present? {bool(milk_present)}") # False, because 0 is considered False in boolean context

water_hot = True
tea_added = False
can_serve = water_hot and tea_added # False, because both conditions need to be True for can_serve to be True
print(f"Can we serve tea? {can_serve}")

