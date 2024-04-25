'''Implementation Using Recursion
Recursion is when a function calls itself.

To implement the Fibonacci algorithm we need most of the same things as in the code by using looping, 
but we need to replace the for loop with recursion.

To replace the for loop with recursion, we need to encapsulate much of the code in a function, 
and we need the function to call itself to create a new Fibonacci number as long as the produced number of Fibonacci numbers is below, 
or equal to, n-2 n is the number of fibonacci numbers
for this eaxple we will generate 20 numbers'''
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)

''' the output will be 
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 '''
