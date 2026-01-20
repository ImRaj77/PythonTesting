greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition Matches")
else:
    print("Condition doesn't matches")
print("Independent of if else")


# for loop
obj=[2,3,5,7,9]
for a in obj:
    print(a*2)
print("************")
# Sum of first 5 natural numbers 1+2+3+4+5 = 15
summation = 0
for a in range(1,6):
    summation = summation + a
print(summation)
print("************")
for k in range(1,10,2):
    print(k)
print("************")

for m in range(5):
    print(m)
print("************")

# While loop
it = 10
while it>1:
    if it == 9:
        it=it-1
        continue
    if it == 3:
        break
    print(it)
    it=it-1
print("************")

name = "my name is raja"
words = name.split(" ")

reversed_sent = ""
for i in range(len(words)-1, -1, -1):
    reversed_sent = reversed_sent + words[i] + " "

print(reversed_sent)
