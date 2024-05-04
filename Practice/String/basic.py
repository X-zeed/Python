name = input("Enter your full name : ")
phone_number = input("Enter your phone number #")

long = len(name) # length of string name
find = name.find("l") # find the first character in the string
rfind = name.rfind("l") # find the first character in the string
cap = name.capitalize() # upper case of the first character of string
up = name.upper() # upper case of the string
low = name.lower() # lower case of the string
digital = name.isdigit() # check that the string is a digit or not
alpha = name.isalpha() # check that the string is a character or not
count = phone_number.count("-") # count the number of the character from the phone_number
replace = phone_number.replace("-"," ") # replace the first character from the phone_number by the second character 


print(replace)