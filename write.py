# read the file and store all the lines in list
# reverse the list
# Write this back into the file
with open('test.txt','r') as reader:          # with this we do not need to open() and close the file
    content = reader.readlines()              #
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)