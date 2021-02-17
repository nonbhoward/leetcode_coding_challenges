class Solution:
    @staticmethod
    def two_sum(_nums: list, _target: int) -> list:
        indices = list()
        for ind_x, num_x in enumerate(_nums):
            for ind_y, num_y in enumerate(_nums):
                if ind_x == ind_y:
                    continue
                elif num_x + num_y == _target:
                    indices.append(num_x)
                    indices.append(num_y)
                    return indices


nums = [2, 7, 11, 15]
target = 9
s = Solution()
s.two_sum(nums, target)
