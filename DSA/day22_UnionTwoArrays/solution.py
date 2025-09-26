class Solution:
    def unionArray(self, nums1, nums2):
        union = []
        s = set()
        for num in nums1:
            s.add(num)
        for num in nums2:
            s.add(num)
        for num in sorted(s):
            union.append(num)
        return union