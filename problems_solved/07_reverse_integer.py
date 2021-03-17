class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        def sign_detected_in_(_number) -> bool:
            return True if _number == '-' else False

        def in_range(_number_reversed) -> bool:
            lower_limit = -2 ** 31
            upper_limit = 2 ** 31 - 1
            return True if lower_limit < _number_reversed < upper_limit else False

        numbers_as_list = list(str(x))
        numbers_length = len(numbers_as_list)
        numbers_reversed = list()
        index_rev = 0
        for countdown_index in range(numbers_length, 0, -1):
            if countdown_index == numbers_length and sign_detected_in_(numbers_as_list[0]):
                numbers_reversed.append(numbers_as_list[index_rev])
                index_rev += 1
            if countdown_index <= numbers_length:
                countdown_index -= 1
            if numbers_as_list[countdown_index] != '-' and int(numbers_as_list[countdown_index]) in digits:
                numbers_reversed.append(numbers_as_list[countdown_index])
            index_rev += 1
        reversed_result = int(''.join(numbers_reversed))
        return reversed_result if in_range(reversed_result) else 0


_x = -123
s = Solution()
rev = s.reverse(_x)
pass
