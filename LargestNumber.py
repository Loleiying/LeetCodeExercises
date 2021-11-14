# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:54:02 2021

@author: Liying Lu

From Leetcode
179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"

"""

class Solution(object):
	def largestNumber(self, nums):
		"""
		Parameters
		----------
		nums : list[int]
			A list of non-negative integers.

		Returns
		-------
		A string that arranges the integers in nums such that they form the largest number.

		"""
		remainder = [n%10 for n in nums]
		largest = []
		print(remainder)
		# finding the largest remainder
		while max(remainder) >= 0:
			max_index = remainder.index(max(remainder))
			largest.append(nums[max_index])
			remainder[max_index] = -1
		
		# final step
		largestNumber = ''.join([str(n) for n in largest])
		return largestNumber
		

sol = Solution()
nums = [3,30,34,5,9]
nums = [34323, 3432]
answer = sol.largestNumber(nums)
print(answer)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		