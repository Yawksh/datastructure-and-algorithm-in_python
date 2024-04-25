'''Implementation Using a For Loop
It can be a good idea to list what the code must contain or do before programming it:

Two variables to hold the previous two Fibonacci numbers
A for loop that runs 18 times
Create new Fibonacci numbers by adding the two previous ones
Print the new Fibonacci number
Update the variables that hold the previous two fibonacci numbers
Using the list above, it is easier to write the program:'''

prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for fibo in range(18):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo
