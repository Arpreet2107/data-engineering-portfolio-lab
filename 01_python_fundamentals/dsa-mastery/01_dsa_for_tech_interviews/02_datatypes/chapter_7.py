#tuple is a collection which is ordered and unchangeable. it allows duplicate members
masala_spices=("cinnamon","cardamom","clove","nutmeg")
print(masala_spices[0])
print(masala_spices[1])
(spice1,spice2,spice3,spice4)=masala_spices
print(spice1)
print(f"the main masala spices are: {spice1}, {spice2}, {spice3} and {spice4}")

#swapping values
ginger_ratio,garlic_ratio=1,2
print(f"the ginger to garlic ration is {ginger_ratio}:{garlic_ratio}")
ginger_ratio,garlic_ratio=garlic_ratio,ginger_ratio
print(f"the ginger to garlic ration is {ginger_ratio}:{garlic_ratio}")

#membership test
print(f"Is clove there in masala spices?{ 'clove' in masala_spices}")
