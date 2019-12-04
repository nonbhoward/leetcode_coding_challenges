import string
import random


class ListNode:  # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_sum = ListNode(0)  # initialize l3_sum as a ListNode object
        l3_sum_tail = l3_sum  # initialize l3_sum_tail as a ListNode object
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
            summed = this_val + that_val if carry == 0 else this_val + that_val + carry
            carry = 1 if summed > 9 else 0
            print("summed is " + str(summed))
            l3_sum_tail.next = ListNode(summed)
            l3_sum = l3_sum_tail.next
            return l3_sum


listNode1 = ListNode(0)
listNode2 = ListNode(0)
for _ in range(2):
    listNode1.val = random.choice(string.digits)
    listNode2.val = random.choice(string.digits)
print(listNode1)
print(listNode2)
Solution.add_two_numbers(Solution(), listNode1, listNode2)

#end
