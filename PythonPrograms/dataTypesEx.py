# List: Data type which allows multiple values of same or different data types
# List is mutable but not Tuple that is the only difference among them

values = [1,2,"Rahul",2.7,True]
print(values[-1])  # print the last index
print(values[2])
print(values[1:3])  # the last index won't print here
print(values[1:])

values.insert(3,"Shetty")

print(values)

values.append("End")

print(values)

values[2]="RAHUL"
print(values)

del values[-1]
print(values)

fruits=["apple","banana","cherry","date","elderberry"]
print("{}{}".format("First fruit: ",fruits[0]))
print("{}{}".format("Last fruit: ",fruits[-1]))
print("{}{}".format("Fruits from index 1 to 2: ",fruits[1:3]))

# Tuple - same as List but it's immutable
print("Tuple Examples")

val = (1,2,"Rahul",4.7)
print(val[2])


# Dictionary
dic = {"a":2, 4: "BCD", "c": "Hello"}
print(dic[4])
print(dic["c"])

#
dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Shetty"
dict["mobile"] = "9130922282"
print(dict)
print(dict["mobile"])


car= {"make": "Toyota","model": "Camry","year": 2020,"color": "Blue"}
print("{}{}".format("Car model: ",car["model"]))
car["owner"]="Rahul"
print("{}{}".format("Updated car dictionary: ",car))