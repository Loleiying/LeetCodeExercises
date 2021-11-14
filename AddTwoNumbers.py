# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:52:50 2020

@author: Liying Lu
"""
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
	def setNext(self, next):
		self.next = next
	def setValue(self, value):
		self.value = value
		
	def getValue(self):
		return self.value
	def getNext(self):
		return self.next
	
	def __str__(self):
		result = [self.value]
		nextNode = self.next
		while nextNode != None:
			result.append(nextNode.getValue())
			nextNode = nextNode.getNext()
		return result
		

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		value = l1.getValue()+l2.getValue()
		inc = 0
		if value <= 9:
			headNode = ListNode(value=value)
		else:
			inc = 1
			headNode = ListNode(value=value-10)
		
		l1Next = l1.getNext()
		l2Next = l2.getNext()
		nextNode = headNode.getNext()
		while (l1Next or l2Next):
			value = l1Next.getValue()+l2Next.getValue()+inc
			if value <= 9 and value >= 0:
				nextNode.setNext(ListNode(value=value))
			elif value >= 10:
				inc = 1
				nextNode.setNext(ListNode(value=value-10))
			l1Next = l1Next.getNext()
			l2Next = l1Next.getNext()
			nextNode = nextNode.getNext()
			
		return headNode
	

sol = Solution()


            
            
        
            
            
            
        