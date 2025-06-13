my_dict = {'key1' : 'value1' , 'key2' : 'value2'}

print(my_dict)
print(type(my_dict))

print(my_dict['key1'])

shopping_list = {'vape' : 20 , 'poppers' : 5}

print(shopping_list['vape'])

tmp1 = {'k1' : [0,1,2] , 'k2' : [my_dict]}

print(tmp1['k2'])

tmp2 = {'k1' : '0,1,2' , 'k2' : [0,1,2], 'k3' : {'inside_key' : 100, 'inside_key2' : 200}}

print(tmp2['k2'][1])

print(tmp2['k3']['inside_key2'])