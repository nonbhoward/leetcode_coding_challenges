import string
import random


class ListNode:  # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_sum = ListNode(0)
        carry = 0  # gets set to 1 for next loop when summed > 9
        while l1 or l2:
            if l1:
                this_val = l1.val
                l1 = l1.next
            else:
                this_val = 0
            print("this_val is " + str(this_val))
            if l2:
                that_val = l2.val
                l2 = l2.next
            else:
                that_val = 0
            print("that_val is " + str(that_val))
            if carry == 0:
                summed = this_val + that_val
            else:
                summed = this_val + that_val + carry
            print(summed)


listNode1 = ListNode(0)
listNode2 = ListNode(0)
for y in random.choice(string.digits):
    listNode1.val = y
for z in random.choice(string.digits):
    listNode2.val = z
print(listNode1)
print(listNode2)
Solution.add_two_numbers(Solution(), listNode1, listNode2)

#end
