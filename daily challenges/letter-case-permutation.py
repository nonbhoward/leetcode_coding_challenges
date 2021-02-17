from random import shuffle


class Solution:
    @staticmethod
    def letter_case_perm(_s: str) -> list:
        digits, lower, upper = '0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        permutations = [_s]
        _s = list(_s)
        perm_count = 0
        for i, char in enumerate(_s):
            if char in digits:
                continue
            perm_count += 1
            _s[i] = char.upper() if char in lower else char.lower()
            # FIXME does not capture all permutations.. only some
            permutations.append(''.join(_s))
        assert len(permutations) == 2 ** perm_count, 'permutation missing'
        return permutations


test_strings = ['a', 'ab', 'abc', 'abcd']
key = list('abcdefghij')
meta_permutations = dict()
for test_string in test_strings:
    s = Solution()
    shuffle(key)
    meta_permutations[''.join(key)] = s.letter_case_perm(test_string)
pass
