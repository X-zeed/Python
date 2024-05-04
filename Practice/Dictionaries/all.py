# 1:values()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
print(1,users.values())

# 2:keys()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
print(2,users.keys())

# 3:pop()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
poped = users.pop(2)
print(3,poped)
print(3,users)

# 4:popitem()
#pop the last item off the dictionary
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
users.popitem()
print(4,users)

# 5:copy()
#
dict={
    0:['a','b'],
    1:['c','d']
}
mydict=dict.copy()
print(5,dict)
print(5,mydict)

# 6:get()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
print(6,users.get(1))
print(6,users.get(999,"missing!"))

# 7:setdefault()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
print(7,users.setdefault(1,"missing!"))
print(7,users.setdefault(999,"missing!"))
print(users)

# 8:clear()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
users.clear()
print(8,users)

# 9:fromkey()
#
users=["Bill","Fronk","Ohm"]
dict=dict.fromkeys(users)
print(9,dict)

# 10:items()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
print(10,users.items())

for k,v in users.items():
    print(10,k,v)
    
# 11:update()
#
users={
    0:"Bill",
    1:"Fronk",
    2:"Ohm"
}
users.update({
    2:"mafuck",
    3:"nahee"
})
print(11,users)