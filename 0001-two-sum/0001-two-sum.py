class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in hashmap and hashmap[answer] != i:
                return [i, hashmap[answer]] 