# 1:append()
#add the value to the last index of list
people = ["Fronk","Ohm"]
people.append("Bill")
print(1,people)

# 2:clear()
#empty list
people = ["Fronk","Ohm"]
people.clear()
print(2,people)

# 3:copy()
#copy the list
people = ["Fronk","Ohm"]
people2 = people.copy()
print(3,people2)

# 4:count()
#count the number of values in the list
people = ["Fronk","Ohm","Fronk","Ohm"]
print(4,people.count("Fronk"))

# 5:extend()
#add the list in method to the end of the list
people = ["Fronk","Ohm"]
people.extend(["Bill"])
print(5,people)

# 6:index()
#find index of the element in the list
people = ["Fronk","Ohm"]
print(6,people.index("Fronk"))

# 7:insert()
#insert the element in the list
people = ["Fronk","Ohm"]
people.insert(1,"Bill")
print(7,people)

# 8:pop()
#delete the element from the list by id
people = ["Fronk","Ohm"]
pop = people.pop(0)
print(8,people)
print(8,pop)

# 9:remove()
#delete the element from the list by name
people = ["Fronk","Ohm"]
people.remove("Ohm")
print(9,people)

# 10:reverse()
#reverse the direction of the list
people = ["Fronk","Ohm"]
people.reverse()
print(10,people)

# 11:sort()
#sort the list from low to high
people = ["Fronk","Ohm","Bill","bob"]
people.sort()
print(11,people)
people.sort(reverse=True)
print(11,people)
