class Solution:
    def intersectionArray(self, nums1, nums2):
        i, j = 0, 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i+=1
                else:
                    j+=1
        return ans