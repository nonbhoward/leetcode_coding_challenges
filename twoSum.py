class Solution:
    # my brute force solution before seeking alternatives
    def two_sum_brute_force(self, nums: list, target: int) -> list:
        for outer_index in range(len(nums)):
            for inner_index in range(len(nums)):
                if not outer_index == inner_index:
                    if nums[outer_index] == target - nums[inner_index]:
                        return outer_index, inner_index

    # alternative solution from discussion forum
    def two_sum_hash_table(self, nums, target):
        seen_values = {}  # initialize a dictionary (hash table)
        for loop_index, test_value_from_nums in enumerate(nums):
            test_value = target - test_value_from_nums
            if test_value in seen_values:
                return [seen_values[test_value], loop_index]
            seen_values[test_value_from_nums] = loop_index
        return []

launcher = Solution()
print("Brute force solution starts here : ")
print(launcher.two_sum_brute_force(nums=[2, 7, 11, 15], target=9))
print("Alternative solution starts here : ")
print(launcher.two_sum_hash_table(nums=[2, 7, 11, 15], target=9))

# end
