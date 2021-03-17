class Solution:
    def is_palindrome(self, x: int) -> bool:
        int_as_list = list(str(x))
        half_length_of_int_as_list = int(len(int_as_list) / 2)
        for idx_forward, val_forward in enumerate(int_as_list):
            idx_backward = -1 * int(idx_forward + 1)
            val_backward = int_as_list[idx_backward]
            if idx_forward == 0 and val_forward == '-':
                return False
            if val_forward == val_backward:
                if idx_forward > half_length_of_int_as_list:
                    return True
                continue
            else:
                return False
        return True


_x = 12345678987654321
s = Solution()
is_pal = s.is_palindrome(_x)
pass
