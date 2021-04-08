class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, ln1: ListNode, ln2: ListNode) -> ListNode:
        pass


_ln1 = ListNode(3)
_ln1.next = 4
_ln1.next = 2
_ln2 = ListNode(4)
_ln2.next = 6
_ln2.next = 5
_s = Solution(_ln1, _ln2)
_ln_sum = _s.add_two_numbers(_ln1, _ln2)
pass
