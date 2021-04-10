class ListNode:
    def __init__(self, val=0, _next_=None):
        self.val = val
        self.next = _next_


class Solution:
    def add_two_numbers(self, ln_addend_a: ListNode, ln_addend_b: ListNode) -> ListNode:
        # init carry and initial ListNode object to store the sum
        carry = 0
        ln_sum = ListNode()
        while ln_addend_a and ln_addend_b:
            # sum values and determine if carry required
            sum_of_ab = ln_addend_a.val + ln_addend_b.val
            carry = 1 if sum_of_ab > 9 else 0
            # adjust value decimal place if carry
            ln_sum.val = sum_of_ab + carry - 10 if carry else sum_of_ab
            # increment each part
            ln_addend_a, ln_addend_b = ln_addend_a.next, ln_addend_b.next
            # ln1, ln2, ln_sum.next = ln1.next, ln2.next, ListNode(val=ln_sum.val,
            #                                                      _next_=None if not ln_sum.next else ln_sum.next)
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
