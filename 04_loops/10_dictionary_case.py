users = [
    {"id": 1, "total": 100, "coupan": "P20"},
    {"id": 2, "total":200, "coupan": "F10"},
    {"id": 3, "total":150, "coupan": "P50"}
]

discounts = {
    "P20": 0.2,
    "F10": 0.1,
    "P50": 0.5
}

for user in users:
    coupan = user["coupan"]
    discount = discounts[coupan]
    total = user["total"]
    discounted_price = total * (1 - discount)
    print(f"User {user['id']} has a discounted price of {discounted_price}")    
    