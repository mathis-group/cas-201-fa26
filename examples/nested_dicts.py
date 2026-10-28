
customer1 = {
    "name": "John Smith",
    "DOB": "01/01/1990",
    "address": {
        "number": "1234 E",
        "Street":"Main St",
        "city": "Tempe",
        "state": "AZ",
        "zip": 85281
    }
}


# Let's get the DOB
# bad_dob = customer1.get("DOD", "-")
# if bad_dob == "-":
#     raise Warning("Key didn't exist in dictionary")
# print(f"The DOB was: {bad_dob}")
c_DOB = customer1.get("DOB", "-")
print(f"{c_DOB}")

c_address = customer1.get("addres", dict())
c_city = c_address.get("city", None)
print(f"{c_city}")
