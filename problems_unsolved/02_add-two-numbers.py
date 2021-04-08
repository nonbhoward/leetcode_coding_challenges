class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, ln1: ListNode, ln2: ListNode) -> ListNode:
        for _ in range(10):
            print(f'value is {ln1.val}')
            ln1 = ln1.next


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
