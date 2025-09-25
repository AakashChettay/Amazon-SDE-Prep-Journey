class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            #print("L: "+str(low)+" H: "+str(high))
            mid = int((low + high) / 2)
            #print("Mid: "+ str(mid))
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

