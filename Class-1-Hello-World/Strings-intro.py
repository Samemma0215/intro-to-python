print("hello world")

if 5>2:
    print("Nikhil is mean")

if -3<5: 
    print("Nikhil loves me")
    print("Nikhil should buy me a birkin")

print(["candy", "strip lashes", "glitter"])
print(2-1)

print(2+1)

print(2/1)

print(7/4)

print(7%4)

print(55%11)

print(2**3)

print(2+10*10+3)

my_puppy = 2

print(my_puppy)

my_puppy = ["acrylics", "cigarettes", "lana del rey", my_puppy]


print(type("strawberry lip balm"))

print(type(7))

print(type(["summer", "beach", "Jack and Coke"]))

print(type(1.72))

# "string"
# 012345

temp_string = "string"

print(temp_string)

print(len(temp_string))

temp_string2 = "I am Olivia"

temp_string2 = print(len("I am Olivia"))

# print(len(temp_string))

# print(temp_string(0))

print(temp_string[0])

print(temp_string[1])

print(temp_string[5])

print(temp_string[-3])

print(temp_string[2:])

print(temp_string[2:5])

print(temp_string[::2])

temp3 = "abcdefghijklmnopqrstuvwxyz"

print(temp3[::4])

print(temp3[:5:2])

my_name = " Samantha"

print("Hello" + my_name + " and Im super funny :)")

# a good way to format objects into strings, for string statements is . format ()
# 'String here {} then also {}'.format('Something 1', 'Something2')

# 'string here {} then also {}'.format('Inserted'))

print('String here {} then also {}'.format('ng1', 'ng2'))

print('String here {} then also {}'.format('ng1', 'ng2', 'ng3'))
      
print("the {0} {1} {1}".format('pink', 'pony', 'club'))

#this is basically indexed (above)

print("The {a} {a} {a}".format(a='pink', b='pony', c='club'))

# flow point = decimals 

test_value = 0.88
test_value2 = 3

print(test_value)
print(type(test_value))

# print("This is my salary: " + test_value2)
print("This is my salary " + str(test_value))

# string literal
# string literals allow you to bring outside variables immediately into string rather than passing them through .format(var)

#f string 
# this {} can container variables, operations, functions, and modifiers, within
print(f'this is my number {test_value2}')

print(f'This is 6 * 3'' + {6*3}')

print(f'This is 6 * 3: {6*3}')
