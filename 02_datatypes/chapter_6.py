# String

chai_type = "Ginger chai"
customer_name = "Riya"

print(f"Order for { customer_name } : { chai_type } please !")

chai_description = "Aromatic and Bold"
print(f"First word: { chai_description[:8] }")
print(f"Last word: { chai_description[12:] }")
print(f"Reverse string: { chai_description[::-1] }")

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(f"Encoded label: { encoded_label }")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")