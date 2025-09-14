1. **Reverse a String I**
Given an input string as an array of characters, write a function that reverses the string.


Examples:
Input : s = ["h", "e", "l", "l", "o"]

Output : ["o", "l", "l", "e", "h"]

Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

Input : s = ["b", "y", "e" ]

Output : ["e", "y", "b"]

Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".

Input : s = ["h", "a", "n", "n", "a", "h"]

Output:
['h', 'a', 'n', 'n', 'a', 'h']
['h', 'n', 'a', 'n', 'a', 'h']
['h', 'n', 'a', 'a', 'n', 'h']
['h', 'a', 'n', 'a', 'n', 'h']

Constraints:
1 <= s.length <= 103
s consist of only lowercase and uppercase English characters.

2. **Check if String is Palindrome or Not**
Given a string s, return true if the string is palindrome, otherwise false.

A string is called palindrome if it reads the same forward and backward.

Examples:
Input : s = "hannah"

Output : true

Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Input : s = "aabbaaa"

Output : false

Explanation : The string when reversed is --> "aaabbaa", which is not same as original string, So we return false.

3. **Check if a Number is Prime or Not**
Given an integer num, return true if it is prime otherwise false.

A prime number is a number that is divisible only by 1 and itself.
Examples:
Input : num = 5

Output : true

Explanation : The factors of 5 are 1 and 5 only.

So it satisfies the prime number condition.

Input : num = 15

Output : false

Explanation : The factors of 15 are 1, 3, 5, 15 only.

As the number has factors other than 1 and itself, So it is not a prime number.

4. **Reverse an array**

Given an array nums of n integers, return reverse of the array.


Examples:
Input : nums = [1, 2, 3, 4, 5]

Output : [5, 4, 3, 2, 1]

Input : nums = [1, 3, 3, 3, 5]

Output : [5, 3, 3, 3, 1]

5. **Check if the Array is Sorted II**

Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

Examples:
Input : nums = [1, 2, 3, 4, 5]

Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Input : nums = [1, 2, 1, 4, 5]

Output : false

Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.