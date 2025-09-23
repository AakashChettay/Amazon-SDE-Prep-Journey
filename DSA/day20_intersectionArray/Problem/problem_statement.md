Given two sorted arrays, nums1 and nums2, return an array containing the intersection of these two arrays. Each element in the result must appear as many times as it appears in both arrays.



The intersection of two arrays is an array where all values are present in both arrays.


Examples:
Input: nums1 = [1, 2, 2, 3, 5], nums2 = [1, 2, 7]

Output: [1, 2]

Explanation:

The elements 1, 2 are the only elements present in both nums1 and nums2

Input: nums1 = [1, 2, 2, 3, 3, 3], nums2 = [2, 3, 3, 4, 5, 7]

Output: [2, 3, 3]

Explanation:

The element 2 appears in both arrays only one time.

The element 3 appears in both arrays two times so we add element 3 equal to its number of occurrences.
