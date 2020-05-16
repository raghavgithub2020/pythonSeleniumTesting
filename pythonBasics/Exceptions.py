ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:
    pass

#raise Exception("Product count not matched") # its one way to raise exceptions

#assert(ItemsInCart == 2) # its another way

# Like Try - Catch in java -- we have Try and Except options in python
try:
    with open('Raghav.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")


