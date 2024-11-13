# find the last index of "Tata" form the list.

Cars = ["Audi", "Tata", "Hyundai","BMW", "Mustang", "Tata", "BMW", "Mahindra"]

index_possition_at_tata_instance_occured_last = len(Cars) - 1 - Cars[::-1].index("Tata")
print(index_possition_at_tata_instance_occured_last)
