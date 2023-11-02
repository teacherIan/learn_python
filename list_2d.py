my_list = []

for i in range(10):
    my_list.append(i)  # appends item to the end of the list

my_list.insert(0, 100)  # insert allows items to be inserted into a specific location
my_list.insert(5, 500)

while my_list:
    print(my_list.pop())  # pop will delete and return the final object in a list

# 2d lists are not a type in python unlike some programming languages.
# code like this would not work:
# my_2d_list = [][]

# 2d lists can be created by appending a list inside another list

my_2d_list = [[], [], []]  # this works

# like how we use a single for loop to deal with one list, we will need two loops for 2d arrays
# lets create a multiplication table as an example
multiplication_table = []
# I'll first initialize the list with 10 inner-lists
for i in range(10):
    multiplication_table.append([])

print(multiplication_table)


