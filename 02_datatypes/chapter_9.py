### Set

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# Union - all unique entries
all_spices = essential_spices | optional_spices
print(f"All Spices: {all_spices}")

# intersection - only common entries
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only is essential spices: {only_in_essential}")

# membership 
print(f"Is 'cloves' in essential spices: {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices: {'cloves' in optional_spices}")


