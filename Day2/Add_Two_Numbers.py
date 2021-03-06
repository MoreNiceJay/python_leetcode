#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:

    def addTwoNumbers(self, l1, l2):
        head = temp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            l1temp = l1.val if l1 else 0
            l2temp = l2.val if l1 else 0


            tempVal = (l1temp + l2temp + carry) % 10

            print("T:" , tempVal)
            carry = (l1temp + l2temp + carry) // 10
            print("C:", carry)
            temp.next = ListNode(tempVal)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next








l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# while l1 != None:
#     print (l1.val)
#     l1 = l1.next



a=Solution()
t = a.addTwoNumbers(l1 , l2)
while t != None:
    print(t.val)
    t = t.next

