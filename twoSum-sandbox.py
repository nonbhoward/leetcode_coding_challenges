# initialize a list
someList = ['a', 'b', 'c', 'd', 'e', 'f', 3, 4, 5, 6, 7, 8]
print(someList)

# create enumerated list object
enumList = enumerate(someList)
print(enumList)  # can't view an enumerate object without consideration
print(list(enumList))  # view the enumerated result with the list() constructor

# two-variable for-loop testing
print("begin for loop tests with enum")
nums = [2, 7, 11, 15]
for loop_index, enumVal in enumerate(nums):
    print("the loop index is " + str(loop_index) + " and the enumerated enumVal is " + str(enumVal))


# end

