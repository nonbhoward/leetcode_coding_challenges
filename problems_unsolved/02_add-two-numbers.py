class ListNode:
    def __init__(self, val=0, _next_=None):
        self.val = val
        self.next = _next_


class Solution:
    def add_two_numbers(self, ln1: ListNode, ln2: ListNode) -> ListNode:
        carry, nex = False, None
        ln_sum = ListNode()
        while ln1 and ln2:
            ln_sum.val = ln1.val + ln2.val if not carry else ln1.val + ln2.val + 1
            carry = True if ln_sum.val > 9 else False
            ln_sum.val = ln_sum.val - 10 if carry else ln_sum.val
            ln1, ln2, ln_sum.next = ln1.next, ln2.next, ListNode(val=ln_sum.val,
                                                                 _next_=None if not ln_sum.next else ln_sum.next)
        return ln_sum.next


_ln1 = ListNode(val=3,
                _next_=ListNode(val=4,
                                _next_=ListNode(val=2,
                                                _next_=None)))
_ln2 = ListNode(val=4,
                _next_=ListNode(val=6,
                                _next_=ListNode(val=5,
                                                _next_=None)))
_s = Solution()
_ln_sum = _s.add_two_numbers(_ln1, _ln2)
pass
