class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def add_two_numbers(self, ln1: ListNode, ln2: ListNode) -> ListNode:
        carry = False
        while ln1 and ln2:
            l_sum = ln1.val + ln2.val if not carry else ln1.val + ln2.val + 1
            carry = True if l_sum > 9 else False
            l_sum = l_sum - 10 if carry else l_sum
            ln1, ln2 = ln1.next, ln2.next


_ln1 = ListNode(val=3,
                _next=ListNode(val=4,
                               _next=ListNode(val=2,
                                              _next=None)))
_ln2 = ListNode(val=4,
                _next=ListNode(val=6,
                               _next=ListNode(val=5,
                                              _next=None)))
_s = Solution()
_ln_sum = _s.add_two_numbers(_ln1, _ln2)
pass
