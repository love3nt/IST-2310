# The Walrus Operator?
# What even is that...

# print(num := 99)

height = float(input('Please input the height: '))
width = float(input('Please input the width: '))

if (area := height * width) > 100:
    print('The area is too large')
else:
    print('The area is in range')