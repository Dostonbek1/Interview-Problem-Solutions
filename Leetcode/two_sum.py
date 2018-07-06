class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        hash_set = set()

        for i in range(len(nums)):
            x = target - nums[i]
            if x >= 0 and x in hash_set:
                return nums.index(x), i
            hash_set.add(nums[i])
        return None

test_list = [-3,4,3,90]
target = 0

test = Solution()
print(test.twoSum(test_list, target))
