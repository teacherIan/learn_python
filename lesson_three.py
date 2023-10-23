# Lesson input, lists and dictionaries

# inputting data into Python is extremely easy
name = input("Please input your name:")  # note: all inputted data is a string datatype.
print("Your name is: " + name)
num = int(input("Please enter a number"))
print(num + 5)  # this works correctly as I changed the datatype to int

# dictionaries store data in key / value pairs

first_dictionary = {
    "name": "Ian",
    "age": 40,
    "job": "teacher"
}
# use the get method to return the value from a key
print(first_dictionary.get("name"))  # prints 'Ian'
print(first_dictionary.get("age"))  # prints 40

# dictionaries have a few ways of being updated
first_dictionary.update([('location', 'China')])
print(first_dictionary)
first_dictionary['home'] = "USA"
print(first_dictionary)

# lists store indexed data
my_list = [1, "2", 3.0, first_dictionary]  # lists can store different types of data

#


