# INSTRUCTIONS
# Given an array of integers, return indices of two numbers such that they add up to a specific target.        \
# You may assume that each input would have exactly one solution, and you may not use the same element twice  \
# -------------------------------------------------------------------------------------------------------------\


# this solution is brute force, meaning it is O(n^2)
num1 = [1, 2, 3]
target2 = 5
def two_sum_one(nums, target):
    # we need to loop through nums once

    # loop through all nums but last
    for i in range(len(nums)-1):
        # i + 1 will start at next index
        for j in range(i + 1, len(nums)):
            # check if nums of index i and nums of index j are equal to target
            if nums[i] + nums[j] == target:
                return([i, j])

print(two_sum_one(num1, target2))


def two_sum_two(nums, target):
    # create dictionary to store values
    seen = {}

    # enumerate grabs the number VALUE not just index
    # i is the index and num is the number value (enumerate grabs both)
    for i, num in enumerate(nums):
        # this first checks if the values are in seen yet
        if target - num in seen:
            # seen[target-num] means seen[index]
            return([seen[target - num], i])
        # if the value does not exist, it will add it to seen
        elif num not in seen:
            seen[num] = i
print(two_sum_two(num1, target2))