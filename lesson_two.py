# lesson 2: loops
# includes loops(for, while)

# for loops are used when you know the amount of times something should happen
# for loops are 0 indexed
# lets first look at a c/java-style for loop and think about the different parts:
 '''
JAVA
for(int i = 0; i < 10; i * 2) {
    System.out.println(i)
}
 '''
# Classic loop syntax. This loop would print the numbers 1 - 10
# Lets think about the different parts before switching back to python
# 1st: int i = 0 -> i stands for iterator, but is not special and anything could be used
# 2nd:  i < 10 -> Logic statement.  If false, the for loop ends.  If true, it continues
# 3rd:  System.out.println(i) -> Whatever is inside the loop will run
# 4th: increment -> i++ is the same as i = i + 1 but i = i + 5 or anything will also work


for i in range(0, 10, 2):
    print(i)