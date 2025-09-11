1. Sum of First N Numbers

Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.


Examples:
Input : N = 4

Output : 10

Explanation : first four natural numbers are 1, 2, 3, 4.

Sum is 1 + 2 + 3 + 4 => 10.

Input : N = 2

Output : 3

Explanation : first two natural numbers are 1, 2.

Sum is 1 + 2 => 3.

```
class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        if N==1:
            return 1
        return N + self.NnumbersSum(N-1)
```
2. Factorial of a Given Number

Given an integer n, return the factorial of n.

Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).


Examples:
Input : n = 3

Output : 6

Explanation : Factorial = 1 * 2 * 3 => 6

Input : n = 5

Output : 120

Explanation : Factorial = 1 * 2 * 3 * 4 * 5 => 120

```
class Solution:
    def factorial(self, n):
        if n==0 or n==1:
            return 1
        return n*self.factorial(n-1)
```

3. Sum of Array Elements

Given an array nums, find the sum of elements of array using recursion.


Examples:
Input : nums = [1, 2, 3]

Output : 6

Explanation : The sum of elements of array is 1 + 2 + 3 => 6.

Input : nums = [5, 8, 1]

Output : 14

Explanation : The sum of elements of array is 5 + 8 + 1 => 14.

```
class Solution:
    def recursion(self, nums, n):
        if n == 0:
            return nums[0]
        return nums[n] + self.recursion(nums, n-1)
    def arraySum(self, nums):
        return self.recursion(nums, (len(nums)-1))
```

4. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Examples:
Input : n = 2

Output : 1

Explanation : F(2) = F(1) + F(0) => 1 + 0 => 1.

Input : n = 3

Output : 2

Explanation : F(3) = F(2) + F(1) => 1 + 1 => 2.

```
class Solution:
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
```

