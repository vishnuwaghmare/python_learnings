# Dictionary

chai_order = dict(type="Masala chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {} # Empty dictionary
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe: {chai_recipe}")
print(f"Recipe base: {chai_recipe['base']}")

del chai_recipe["liquid"] # delete element from dictionary
print(f"Recipe: {chai_recipe}")

# membership

print(f"Is suagr is in the order? {'sugar' in chai_order}")

# print(f"Order details (keys) {chai_order.keys()}")
# print(f"Order details (values) {chai_order.values()}")
# print(f"Order details (items) {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom" : "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order["size"]
print(f"chai size is: {chai_size}")

chai_type = chai_order.get("type", "No Type") # get method take 2 params one is value and another one is default value when first one is missing
print(f"Chai type is: {chai_type}")

customer_note = chai_order.get("note", "No Note") # get method take 2 params one is value and another one is default value when first one is missing
print(f"Customer note is: {customer_note}")



