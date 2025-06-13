list1 = [1,2,3,4,5]

print(len(list1))

print(list1)

list2 = [22, "cheesecake bites", .5]

print(list2)

print(list2[0])

print(list2[1])

my_str = "abcdefg"

print(my_str[1:2])

#only prints out b because the first number is the start and the stop is the second number/value
# will not print the stop variable 

print(my_str[1:1])

print(list2[0])

print(list2[0:2])

temp_list = ["90", "21", 2 , 6]

print(temp_list[2:])

print(2 * 6)

print(temp_list[2] * temp_list[3])

tmp1 = ["one", "two", "three"]

tmp2 = ["four", "six"]

big_temp = tmp1 + tmp2

print(big_temp)

tmp1[0] = "test_value"

print(tmp1)

tmp1.append("seven")

print(tmp1)

tmp1.pop()

popped_value = tmp1.pop()
# tmp.pop() deleted the last value, if you do not specify the position of deletion
# making a new variable called popped_value 
# on the right-hand side there is another .pop() occurring but what is happening is that the popped value is being assigned to the new variable 
print(popped_value)

print(tmp1)

print(tmp1.pop(0))

print(tmp1)

print(tmp1.pop(0))

print(tmp1)

tmp3 = ("six", "seven", "eight", "nine", "ten")

tmp3 = list(tmp3)

tmp3.append("eleven")

print(tmp3)

alpha = ["b", "z", "h", "i"]

alpha.sort()

num_list = [0, 9, 1019290, 1, 3]
num_list.sort()

print(num_list)
print(alpha)

b_val = 'b'
print(ord(b_val))

alpha.reverse()

print(alpha)

tmp4 = ["1", "2"]

tmp4.pop()

print(tmp4)

tmp4.pop()

print(tmp4)

num_list.reverse()

C_val = "C"

print(ord(C_val))

num_list.sort(reverse=True)

print(num_list)