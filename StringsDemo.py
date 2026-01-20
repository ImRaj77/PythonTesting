str = "RahulShettyAcademy.com"
str1 = "Constructing firm"
str3 = "RahulShetty"
str4 = "Raja"

print(str[1])                   # a
print(str[-1])                  # m

print(str[0:5])                 # Rahul

print(str + " is a " + str1)    # concat

print(str3 in str)              # True # subString check
print(str4 in str)              # False

var = str.split(".")
print(var)
print(var[0])

str5 = "   Great Indian  "
print(str5.strip())             # remove whitespaces / trim the String
print(str5.lstrip())            # remove left side whitespaces
print(str5.rstrip())            # remove right side whitespaces

