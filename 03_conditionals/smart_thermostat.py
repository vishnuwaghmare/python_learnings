devise_status = "active"
temprature = 30

if devise_status == "active":
    if temprature > 35:
        print("High temprature alert!")
    else: 
        print("Temprature is normal")
else:
    print("Device is offline")