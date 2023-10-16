# lesson one: basic python
# includes types, scope, function creation/calls and loops
import sys

# writing syntax:
# python uses snake case which_is_written_like_this

# types:
# python is a dynamic language.  Meaning type with be inferred from usage
my_first_var = 1  # python will infer the type should be integer
my_second_var = "1"  # python will infer the type should be text(string)
my_third_var = 1.0  # python will infer the type should be a floating point number

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
# note that with f-strings, you do not need to explicitly cast to a string type




