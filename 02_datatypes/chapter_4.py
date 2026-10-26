# Boolean

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = 1 # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = 11213432423 # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = "Some milk is present" # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = None # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False
can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")

tea_added = True
can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")

tea_added = False
can_serve = water_hot or tea_added
print(f"Can serve chai? {can_serve}")

water_hot = False
tea_added = False
can_serve = water_hot or tea_added
print(f"Can serve chai? {can_serve}")

water_hot = False
tea_added = False
can_serve = water_hot and not tea_added
print(f"Can serve chai? {can_serve}")

water_hot = False
tea_added = False
can_serve = not water_hot and not tea_added
print(f"Can serve chai? {can_serve}")