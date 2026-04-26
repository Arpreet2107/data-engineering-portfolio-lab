#Integer 
black_tea_grams = 120
ginger_tea_grams = 342
total_tea_grams = black_tea_grams + ginger_tea_grams
print(f"total tea in grams: {total_tea_grams}")

remaining_tea = black_tea_grams - ginger_tea_grams
print(f"remaining tea in grams: {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serve= milk_litres/servings
print(f"milk per serve in litres: {milk_per_serve}")

total_tea_bags = 7
pots = 4 
bags_per_pot = total_tea_bags//pots
print(f"whole tea bags per pot: {bags_per_pot}")

cardamom_pods = 10
pods_per_cup = 3
leftover_pods = cardamom_pods%pods_per_cup
print(f"the leftover cardamom pods: {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
flavor_strength = base_flavor_strength**scale_factor
print(f"flavor strength: {flavor_strength}")
