
'''Finding The nth Fibonacci Number Using Recursion
To find the nth Fibonacci number we can write code based on the mathematic formula for Fibonacci number n:
F(n)=F(n1)+F(n−2)

This just means that for example the 10th Fibonacci number is the sum of the 9th and 8th Fibonacci numbers.'''




def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(5))



'''Step 1: We call F(5).

Since n is greater than 1, we move to the else block.

Step 2: F(5) calls F(4) and F(3).

F(4):
n is still greater than 1, so we call F(4 - 1) + F(4 - 2) => F(3) + F(2).
F(3):
n is still greater than 1, so we call F(3 - 1) + F(3 - 2) => F(2) + F(1).
Step 3: F(3) calls F(2) and F(1).

F(2):n is still greater than 1, so we call F(2 - 1) + F(2 - 2) => F(1) + F(0).
F(1):n is 1, so it returns 1.
Step 4: F(2) calls F(1) and F(0).

F(1) returns 1.
F(0) returns 0.
Step 5: F(4) gets F(3) (which is 2) and F(2) (which is 1).

F(3) is calculated in the earlier steps and found to be 2.
F(2) is calculated in the earlier steps and found to be 1.
So, F(4) returns F(3) + F(2) => 2 + 1 = 3.
Step 6: F(5) gets F(4) (which is 3) and F(3) (which is 2).

F(4) is calculated in the earlier steps and found to be 3.
F(3) is calculated in the earlier steps and found to be 2.
So, F(5) returns F(4) + F(3) => 3 + 2 = 5.
Therefore, F(5) returns 5, which is the 5th Fibonacci number.
'''
