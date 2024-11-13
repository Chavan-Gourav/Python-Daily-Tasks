#remove all occurences of BMW from the list.

Cars = ["Audi", "BMW", "Hyundai","BMW", "Mustang", "Maruti-Suzuki", "BMW", "Mahindra"]

Filtered_Cars_List = [Car for Car in Cars if Car != "BMW"]
print(Filtered_Cars_List)