from random import shuffle


class Solution:
    @staticmethod
    def letter_case_perm(_string: str) -> list:
        digits, _string = '0123456789', list(_string)

        def count_non_digits(_str: list) -> tuple:
            p_count, pols = 0, list()
            for _chr in _str:
                if _chr not in digits:
                    p_count += 1
                    pols.append(1)
            p_total = 2 ** p_count
            return p_total, pols

        permutation_total, polarities = count_non_digits(_string)
        permutations = list()
        for permutation in range(1, permutation_total + 1):
            perm = list()
            for _i, _char in enumerate(_string):
                try:
                    polarities[_i] = -1 * polarities[_i] if _i % permutation == 0 else polarities[_i]
                    perm.append(_char.upper() if polarities[_i] > 0 else _char.lower())
                except Exception as ex:
                    print(ex)
            permutations.append(perm)
        return permutations


test_strings = ['a', 'ab', 'abc', 'abcd']
key = list('abcdefghij')
meta_permutations = dict()
for test_string in test_strings:
    s = Solution()
    shuffle(key)
    meta_permutations[''.join(key)] = s.letter_case_perm(test_string)
pass
