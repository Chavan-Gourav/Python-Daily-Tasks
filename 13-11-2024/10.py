#Append multiple cars ["Jaguar", "Fiat"] in th list.

Cars = ["Audi", "BMW", "Hyundai","BMW", "Mustang", "Maruti-Suzuki", "BMW", "Mahindra"]
More_Cars = ["Jaguar", "Fiat"]
# # All_Cars = Cars + More_Cars
# Cars.extend(More_Cars)
# # print(All_Cars)
# print(Cars)

'''Another solution is to unpack both lists inside a new list 
and assign it back to the copy of the original list'''
#my_list[:] = [*my_list, *new_items]
Cars[:] = [*Cars, *More_Cars]
print(Cars)
