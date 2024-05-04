# 1:capitalize()
# upper case of the first character of string
text = 'hello'
print({1} , text.capitalize())

# 2:casefold()
# lower case of the string
text = 'MaRIo'
print({2} , text.casefold())

# 3:center()
# center the string by parameter in the method
text = 'Duddid'
print({3} , text.center(20))

# 4:count()
# count the number of the character from the string
text = "abc_abc_abc_abc_abc_abc_abc_abc_abc_abc_abc"
print({4} , text.count("ab",0,20))

# 5:encode()

text = "Elon Musk"
print({5} , text.encode(encoding='UTF-8',errors='strict'))

# 6:endswitch()
# check that the string end with a character in the method or not
text = "apple"
print({6} , text.endswith("e"))

# 7:expandtabs()

text = "text1\ttext2\ttext3"
print({7} , text.expandtabs(6))

# 8:find()
# find the first character in the string
text = "Bill Belle"
print({8} , text.find("B",0,6))

# 9:format()

text = "{a} is kick {b}. "
print({9} , text.format(a="Bill", b="Belle"))
text = "{} is kick {}. "
print({9} , text.format("Bill", "Belle"))

# 10:format_map()

co = {
    "x" : 10,
    "y" : -5,
}
text = "{x} {y}"
print({10} , text.format_map(co))

# 11:index()

text = "I walk through to Belle"
print({11} , text.index("through",0,14))

# 12:isalnum()
# check that the string is a character and number or not
text = "Bill53162"
print({12} , text.isalnum())

# 13:isalpha()
# check that the string is a character or not
text = "bill"
print({13} , text.isalpha())

# 14:isascii()
# check taht the all of character of string is ascii
text = "Bill?!"
print({14} , text.isascii())

# 15:isdecimal()
# if the string is a decimal it is also a digit and numeric
text = "213"
print({15} , text.isdecimal())

# 16:isdigit()
# if the string is a digit it is also a digit and numeric
text = "⓪⓵⓶⓷⓸⓹⓺⓻⓼⓽"
print({16} , text.isdigit())

# 17:isnumeric()
# if the string is a digit it is also a digit and numeric
text = "๑๒๓๔๕๖๗๘๙"
print({17} , text.isdigit())

# 18:isdentifier()
# check that you can use name of virable from the string in method 
text = 'B_ill'
print({18} , text.isidentifier())

# 19:islower()
# check the string is lower case or not
text = "bill"
print({19} , text.islower())

# 20:isprintable()
# check the string can print or not
text = "print"
print({20} , text.isprintable()) 

# 21:isspace()
# check the string have only space or not
text = "     "
print({21} , text.isspace())

# 22:istitle()
# check the string have only title or not
text = "Billxzeed"
print({22} , text.istitle())

# 23:isupper()
# check the string is upper case or not
text = "BILL"
print({23} , text.isupper())

# 24:join()
# join the string
text = " "
print({24} , text.join(["text1","text2","text3"]))

# 25:ljust()
# 
text = "text"
print({25} , text.ljust(20,"-"))

# 26:lower()
#
text = "BILL"
print({26} , text.lower())

# 27:lstrip()

text = "Some time."
print({27} , text.strip("Some"))

# 28:maketrans()
# 29:translate()
# these two things are make changing to string
text = "That is Bacon."
tran = text.maketrans("B","n")

print({28} , tran)
print({29} , text.translate(tran))

# 30:partition()
# split the string with parameters in method
text = "a+b=c"
print({30} , text.partition("="))

# 31:removeprefix()
#
text = "Bill"
print({31} , text.removeprefix("Bi"))

# 32:removesuffix()
#
text = "Mister Everyone"
print({32} , text.removesuffix("one"))

# 33:replace()
#
text = "Wachirawit Tanleng Wachirawit Wachirawit"
print({33} , text.replace("Wachirawit","Belle",2))

# 34:rfind()
#
text = "Wachirawit"
print({34} , text.rfind("a",0,7))

# 35:rindex()
#
text = "Wachirawit"
print({35} , text.rindex("t",0,10))

# 36:rjust()
#
text = "Bill"
print({36} , text.rjust(20,"-"))

# 37:rpartition()
#
text = "Bill-Belle-Soft"
print({37} , text.rpartition("-"))

# 38:rsplit()
# 39:split()
text = "Bill Wachirawit"
print({38} , text.rsplit(sep=" "))
text = "www.google.com"
print({38} , text.rsplit(sep="."))
text = "This is the string"
print({39} , text.split(maxsplit=2))

# 40:rstrip()
#
text = "My name is Bill Wachirawit"
print({40} , text.rstrip("Wachirawit"))

# 41:splitlines()
#
text = "Bill\nWachirawit\nTanleng"
print({41} , text.splitlines(keepends=True))

# 42:startwith() 
#
text = "Bill"
print({42} , text.startswith("B"))

# 43:strip()
#
text = "Bill xzeed"
print({43} , text.strip("Bill "))

# 44:swapcase()
#
text = "Bill Wachirawit"
print({44} , text.swapcase())

# 45:title()
#
text = "bill Wachirawit tanleng"
print({45} , text.title())

# 46:upper()
#
text = "bill wachirawit"
print({46} , text.upper())

# 47:zfill()
#
text = "bill"
print({47} , text.zfill(20))