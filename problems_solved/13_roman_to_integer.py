class Solution:
    def roman_to_int(self, s: str) -> int:
        def value_of_(_char) -> int:
            values = {
                'I':    1,
                'V':    5,
                'X':    10,
                'L':    50,
                'C':    100,
                'D':    500,
                'M':    1000
            }
            return values[_char]

        def subtractor_set_(_prev, _curr) -> bool:
            subtractor_sets = {
                'I':    ['V', 'X'],
                'X':    ['L', 'C'],
                'C':    ['D', 'M']
            }
            if _prev in subtractor_sets and _curr in subtractor_sets[_prev]:
                return True
            return False

        value, previous_char, subtraction_possible = 0, '', False
        for char in s:
            value = value + value_of_(char)
            if subtractor_set_(previous_char, char):
                value = value - 2 * value_of_(previous_char)
            previous_char = char
        return value


_rs = "IV"
_s = Solution()
_int_val = _s.roman_to_int(_rs)
pass
