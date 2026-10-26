chai_types = ["Masala", "Ginger", "Cardamom", "Masala", "Ginger", "Cardamom"]

strong_chai = list(filter(lambda x: x != "Masala", chai_types))
print(strong_chai)
