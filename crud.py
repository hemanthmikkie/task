import requests

BASE_URL = "http://localhost:3000"

while True:

    print("\n====== CRUD OPARATIONS ======")
    print("1.GET All")
    print("2.GET By ID")
    print("3.POST")
    print("4.PUT")
    print("5.PATCH")
    print("6.DELETE")
    print("7.EXIT")

    choice = input("Enter Choice: ")

    if choice == "7":
        break

    resource = input("Resource (mobiles/laptops/tablets/headphones/smartwatches): ")

    if choice == "1":

        r = requests.get(f"{BASE_URL}/{resource}")
        print(r.json())

    elif choice == "2":

        id = input("ID: ")
        r = requests.get(f"{BASE_URL}/{resource}/{id}")
        print(r.json())

    elif choice == "3":

        data = {
            "id": int(input("ID: ")),
            "brand": input("Brand: "),
            "model": input("Model: "),
            "price": int(input("Price: "))
        }

        r = requests.post(f"{BASE_URL}/{resource}", json=data)
        print(r.json())

    elif choice == "4":

        id = input("ID: ")

        data = {
            "id": int(id),
            "brand": input("Brand: "),
            "model": input("Model: "),
            "price": int(input("Price: "))
        }

        r = requests.put(f"{BASE_URL}/{resource}/{id}", json=data)
        print(r.json())

    elif choice == "5":

        id = input("ID: ")
        price = int(input("New Price: "))

        r = requests.patch(
            f"{BASE_URL}/{resource}/{id}",
            json={"price": price}
        )

        print(r.json())

    elif choice == "6":

        id = input("ID: ")

        r = requests.delete(f"{BASE_URL}/{resource}/{id}")

        print("Deleted Successfully")