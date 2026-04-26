chai_order = dict(type="masala chai",siza="large",sugar=2)
print(f"Chai order:{chai_order}")


chai_recipe = {}#empty dictionary
chai_recipe["base"] = "black tea"#adding key and value to the dictionary
chai_recipe["liquid"] = "milk"
#accessing values in the dictionary
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe liquid: {chai_recipe['liquid']}")    
del chai_recipe["liquid"]
print(f"Chai recipe: {chai_recipe}")   

#creating a dictionary with different data types as values
chai_ingridients = {
    "base": "black tea",
    "liquid": "milk",
    "spices": ["cardamom", "cinnamon", "clove"],
    "sweetener": "sugar"
}
print(f"Chai ingridients: {chai_ingridients}")
print(f"Ingridients details(keys): {chai_ingridients.keys()}")#returns a view object that displays a list of all the keys in the dictionary
print(f"Ingridients details(values): {chai_ingridients.values()}")#returns a view object that displays a list of all the values in the dictionary
print(f"Ingridienta detials(items):{chai_ingridients.items()}")#returns a view object that displays a list of dictionary's key-value tuple pairs

#membership test for dictionary
print(f"Is sugar there in chai_order? {'sugar' in chai_order}")
print(f"Is liquid there in chai_order? {'liquid' in chai_order}")

last_item = chai_order.popitem 
print(f"Last item removed from chai_order: {last_item}")
print(f"Chai order after popitem: {chai_order}")

#update method to add multiple key-value pairs to a dictionary
extra_spices ={"cardmom":"crushed","ginger":"grated"}#creating a new dictionary with extra spices
chai_recipe.update(extra_spices)#updating the chai_recipe dictionary with the extra_spices dictionary
print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size: {chai_size}")
#using get method to access a value that may not exist in the dictionary
customer_note = chai_order.get("customer_note", "No special instructions")
print(f"Customer note: {customer_note}")