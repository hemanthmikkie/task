# import requests
# import json

# api = "http://localhost:3000/mobiles/2"

# send_data = {
#   "id":22,
#   "brand": "IQOO",
#   "model": "z7 proo",
#   "price": 39999
# }

# try:
#   # Use `json=` with a Python object so requests sets Content-Type correctly
#   res = requests.post(api, json=send_data, timeout=10)
#   print(res.status_code)
#   try:
#     print(res.json())
#   except ValueError:
#     print(res.text)
# except requests.exceptions.RequestException as e:
#   print("Request failed:", e)

# response = requests.get(api)

# print("Status Code:", response.status_code)

# for mobile in response.json():
#     print(mobile)


# update_price = {
#     "price": 42999
# }

# response = requests.patch(api, json=update_price)

# print("Status Code:", response.status_code)
# print(response.json())






import requests

api = "http://localhost:3000/mobiles"

while True:
    print("\n====== Mobile CRUD ======")
    print("1. Add Mobile")
    print("2. View All Mobiles")
    print("3. View Mobile by ID")
    print("4. Update Mobile")
    print("5. Delete Mobile")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        data = {
            "id": int(input("Enter ID: ")),
            "brand": input("Enter Brand: "),
            "model": input("Enter Model: "),
            "price": int(input("Enter Price: "))
        }

        response = requests.post(api, json=data)
        print(response.json())

    elif choice == "2":
        response = requests.get(api)
        for mobile in response.json():
            print(mobile)

    elif choice == "3":
        mobile_id = input("Enter ID: ")
        response = requests.get(f"{api}/{mobile_id}")

        if response.status_code == 200:
            print(response.json())
        else:
            print("Record Not Found")

    elif choice == "4":
        mobile_id = input("Enter ID to Update: ")

        data = {
            "id": int(mobile_id),
            "brand": input("Brand: "),
            "model": input("Model: "),
            "price": int(input("Price: "))
        }

        response = requests.put(f"{api}/{mobile_id}", json=data)
        print(response.json())

    elif choice == "5":
        mobile_id = input("Enter ID to Delete: ")

        response = requests.delete(f"{api}/{mobile_id}")

        if response.status_code == 200:
            print("Deleted Successfully")
        else:
            print("Delete Failed")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")