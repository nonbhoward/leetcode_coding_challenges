class ListNode:
    def __init__(self, val=0, _next_=None):
        self.val = val
        self.next = _next_


class Solution:
    def add_two_numbers(self, ln_addend_a: ListNode, ln_addend_b: ListNode) -> ListNode:
        carry = 0  # initial carry val
        ln_sum = ListNode()
        ln_sum_deep = ln_sum
        while carry or ln_addend_a or ln_addend_b:  # loop until all addends are resolved
            # fetch
            val_a = ln_addend_a.val if ln_addend_a else 0
            val_b = ln_addend_b.val if ln_addend_b else 0
            # math
            sum_of_abc = val_a + val_b + carry  # sum a, b, carry
            carry = 1 if sum_of_abc > 9 else 0  # decide if carry for next round
            sum_of_abc = sum_of_abc - 10 if carry else sum_of_abc  # adjust decimal before save
            # link
            ln_sum_deep.next = ListNode(sum_of_abc)
            ln_sum_deep = ln_sum_deep.next
            # increment
            ln_addend_a = ln_addend_a.next if ln_addend_a else None
            ln_addend_b = ln_addend_b.next if ln_addend_b else None
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
