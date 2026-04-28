favourite_chai=[
    "Masala Chai","Green tea","Masala Chai",
    "Lemon Tea","Green tea","Elaichi Chai"
]

unique_chai= {chai for chai in favourite_chai if "Tea" in favourite_chai}
print(unique_chai)

recipes={
    "Masala Chai":["ginger","cardamom","clove"],
    "Elaichi Chai":["cardamom","milk"],
    "Spicy Chai":["ginger","black pepper","clove"],
}

unique_spices = {spice for ingridients in recipes.values() for spice in ingridients}
print(unique_spices)