favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai" 
]

unique_chai = {chai for chai in favourite_chais if len(chai) < 10}

print(unique_chai)

recepes = {
    "Masala Chai" : ["Ginger", "Cardimom", "Clove" ],
    "Elaichi Chai" : ["Cardimom", "Milk" ],
    "Spicy Chai" : ["Ginger", "Black pepper", "Clove" ]
}

unique_spices = { spice for ingredients in recepes.values() for spice in ingredients }

print(unique_spices)