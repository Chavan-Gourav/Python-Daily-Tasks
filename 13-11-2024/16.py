# extend the list of Cars with ["Ferrari", "Lambo"] only if list contain "BMW"

Cars = ["Audi", "Tata", "Hyundai","BMW", "Mustang", "Tata", "Mahindra"]

if "BMW" in Cars:
    Cars.extend(["Ferrari", "Lambo"])
    print("More Cars are added!")

else:
    print("List Cars doesn't have any BMW!")