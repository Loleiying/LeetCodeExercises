# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:50:47 2020

@author: Liying Lu
"""
class Solution(object):
	def twoSum(self, nums, target):
		"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
		for i in range(len(nums)):
			#print(i)
			for j in range(i+1,len(nums)):
				#print(i, j)
				if nums[i]+nums[j] == target:
 					return [i,j]
		return None
	
sol = Solution()
nums = [3,2,4]
target = 6
answer = sol.twoSum(nums, target)
print(answer)
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))