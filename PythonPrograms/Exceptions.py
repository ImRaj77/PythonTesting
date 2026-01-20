
items_in_cart = 0
# 2 items are in the cart

if items_in_cart != 2:
#     raise Exception("Products cart count is not matching")
    pass

assert(items_in_cart == 0)          # We can Explicitly fail the test with assert

# try, catch

try:
    with open('filelog.txt','r') as reader:
        reader.read()
except:
    print("Exception caught and test failed")

try:
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning all the resources")