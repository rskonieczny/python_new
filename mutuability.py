my_string = "Hello, Python!"
try:
    my_string[7] = 'W'
except TypeError as e:
    print(e)

my_list = [1, 2, 3, 4]
my_list[2] = 30
print(my_list)

original_list = [1 , 2 , 3]
new_list = original_list
new_list[1] =200
print[original_list]

independent_copy = original_list[:]
independent_copy[1]=20
print(original_list)
print(independent_copy)

a=10
b=a
b=5
print(a)
print(b)

lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1)



