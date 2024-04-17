# the format of the string to control output

# animal = "cow"
# item = "moon"
# sentence = f"The {animal}" \
#     f" jump over the {item}"

# print("The " + animal + " Jump over the " + item)
# print("The {} jump over the {}".format(animal, item))
# print("The {0} jump over the {1}".format(animal, item))
# print("The {animal} jump over the {item}".format(animal = animal, item=item))
# print(f"The {animal} jump over the {item}")
# print(f"The {animal.title()} jump over the {item.upper()}")
# print(sentence)

# text = "The {} Jump over the {}"
# print(text.format(animal, item))

name = "Bill"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you".format(name))
print("Hello my name is {:<10}. Nice to meet you".format(name))
print("Hello my name is {:>10}. Nice to meet you".format(name))
print("Hello my name is {:^10}. Nice to meet you".format(name))
print(f"{name:-^10}")

# number = 10000

# print("The number pie is {:.2f}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:x}".format(number))
# print("The number is {:e}".format(number))

# name = "Bill"
# city = "Pathum Thani"
# print("My name is %s I'm from %s" % (name,city))

# print("\"bill\"")
# x=10
# y=20
# print(f"x + y = {x+y}")