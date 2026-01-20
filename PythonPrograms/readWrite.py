
file = open('test.txt')

# Read all the contents of the file
# print(file.read(6))            # Read n number of characters by passing parameter

# print(file.readline())         # Read line by line from the file
# print(file.readline())

# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()

for line in file.readlines():      # read all the file and store it in a list
    print(line)

file.close()
