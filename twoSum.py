class Solution:
    def two_sum_brute_force(self, nums: list, target: int) -> list:
        for outer_index in range(len(nums)):
            for inner_index in range(len(nums)):
                if not outer_index == inner_index:
                    if nums[outer_index] == target - nums[inner_index]:
                        return outer_index, inner_index

    def two_sum_alt(self, nums: list, target: int) -> list:
        print(nums)
        print(target)


launcher = Solution()
print("Brute force solution starts here : ")
print(launcher.two_sum_brute_force(nums=[2, 7, 11, 15], target=9))
print("Alternative solution starts here : ")
print(launcher.two_sum_alt(nums=[2, 7, 11, 15], target=9))

# end
