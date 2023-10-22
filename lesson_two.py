import random # import for random number generation

section = "******************************"
print(section)

# lesson 2: loops
# includes modulus operator, loops(for, while)

# modulus operator
# the modulus operator gives the remainder from doing division
mod_one = 6 % 2
print(f"remainder 6 % 2 = {mod_one}")  # gives 0 because 6 / 2 has a remainder of 0

mod_two = 7 % 2
print(f"remainder 7 & 2 = {mod_two}")  # prints the remainder of 1

# for loops are used when you know the amount of times something should happen
# for loops are 0 indexed
# lets first look at a c/java-style for loop and think about the different parts:
"""
JAVA
for(int i = 0; i < 10; i * 2) {
    System.out.println(i)
}
"""
# Classic loop syntax. This loop would print the numbers 1 - 10
# Lets think about the different parts od this statement before switching back to python
# 1st: int i = 0 -> i stands for iterator, but is not special and anything could be used
# 2nd:  i < 10 -> Logic statement.  If false, the for loop ends.  If true, it continues
# 3rd:  System.out.println(i) -> Whatever is inside the loop will run
# 4th: increment -> i++ is the same as i = i + 1 but i = i + 5 or anything will also work


print(section)
# python for loops:
for i in range(10):
    print(f"range(10) current i = {i}")  # prints out 0 - 9

print(section)

for i in range(5, 10):
    print(f"range(5, 10) current i = {i}")  # prints 5 - 9.

print(section)

#  Note, the first number(5) is included while the second number(10) is excluded

# We can also do more advanced counting

for i in range(0, 100, 20):
    print(f"range(10) current i = {i}")  # counts by 20 -> 20,40,60,80 but 100 is excluded

print(section)

# while loops
# Used when you don't know how many times a loop should run

random_number = random.randint(1, 10)
the_number_five = 5
has_looped = 0

while random_number != the_number_five:
    has_looped += 1
    print(f"This loop has run {has_looped} times")
    random_number = random.randint(1, 10)


print(f"it took {has_looped} times for random_number to equal 5")








