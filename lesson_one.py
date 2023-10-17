# lesson one: basic python
# includes types, function creation/calls and loops, scope(LEGB Rule), logic statements
# This lesson includes everything needed for warmup-1 problems on codingBat  https://codingbat.com/python
import sys

# writing syntax:
# python uses snake case which_is_written_like_this

# types:
# python is a dynamic language.  Meaning type with be inferred from usage
my_first_var = 1  # python will infer the type should be integer
my_second_var = "1"  # python will infer the type should be text(string)
my_third_var = 1.0  # python will infer the type should be a floating point number
my_forth_var = True  # python will infer the type should be boolean

# print can be used to print to the console.
# In a real program this would generally be used only in development
print("Hello")
# you can also print out variables like so:
print("My second var is: " + my_second_var)
# this is called string concatenation. This can only be done on strings
# different types can be used but only after being cast to a String type:
print("My first var is: " + str(my_first_var))
# for more complex strings you can use what's known as an F-string
# which lets you use {} notation
print(f"my first var is {my_first_var} and my second var is {my_second_var} and my third var is {my_third_var}")


# note that with f-strings, you do not need to explicitly cast the type to string

# functions
# defined using the def keyword followed by the name of the function, parentheses and a colon
# anything within the function will need to be indented.  the function will end once the indentation ends

def print_hello():
    print("Hello from print_hello")  # I live within print_hello as I am indented


print("hello")  # I am not inside print_hello as I am not indented
# functions are called by writing the function name followed by parentheses
print_hello()
# and can be called as many times as required
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()


# parameters can be added to a function to make the functionality dynamic
def print_name_and_age(name, age):
    print(f"my name is {name} and my age is {age}")


print_name_and_age("Ian", 25)
print_name_and_age("Bob", 40)


# the return keyword specifies that a function will send back a value.
# for now understanding the basic usage of return is fine, but we will discuss this more in future lessons
def add(num_one, num_two):
    return num_one + num_two


print(add(5, 2))

# logical statements
# an if statement example is written below:
if True:
    print("This will always print")

if False:
    print("this will never print")

# logical statements can be written inplace of True / False
# == checks equality
if 2 == 2:
    print("This will print because 2 does equal 2")

# != checks inequality
if 3 != 2:
    print("This will also print as 3 does not equal 2")

# and/or
if 2 == 2 and 3 != 2:
    print("This will not print, as both statements need to be true")

if 2 == 2 or 3 != 2:
    print("This will print, as only one statement needs to be true")

# this completes the first lesson.
# please practice at https://codingbat.com/python warmup-1





