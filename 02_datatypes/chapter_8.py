# Mutable Datatypes
# List

ingredients = ["water", "milk", "back tea"]
print(f"Ingredients are: {ingredients}")

ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

ingredients.remove("milk")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Chai: {chai_ingredients}")

chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")


chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_level = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_level)}")
print(f"Minimum sugar level: {min(sugar_level)}")

# Operator Overloading

base_liquid = ["water", "milk"]
extra_favour = ["ginger"]

full_liquid_mix = base_liquid + extra_favour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["back tea"] * 3
print(f"Strong brew: {strong_brew}")

strong_brew = ["back tea", "water"] * 3
print(f"Strong brew: {strong_brew}")


# Bytearray

raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytearray: {raw_spice_data}")

raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Replaced Bytes: {raw_spice_data}")