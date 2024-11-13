#add multiple cars at index 2.

Cars = ["Audi", "BMW", "Hyundai","BMW", "Mustang", "Maruti-Suzuki", "BMW", "Mahindra"]
# Cars.insert(2, ["Volvo", "Honda"])
Cars[2:2] = ["Volvo", "Honda"]
print(Cars)