#slicing have 3 parameters [start:stop:step]

s = "Bill Belle"

first_name = s[:4]
second_name = s[5:10]
reversed_name = s[::-1]

# print(first_name)
# print(second_name)
# print(reversed_name)

website = "http://google.com"
url = slice(7,13)
print(website[url]) 