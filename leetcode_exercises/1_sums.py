"""Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target. You may assume that each input would have exactly one solution, and you may not use
the same element twice. You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            print(f"i: {i}, j: {j}")
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_2(nums, target):
    seen = {}
    for i, el in enumerate(nums):
        remaining = target - el
        if remaining in seen:
            return [seen[remaining], i]
        seen[el] = i
    return []


if __name__ == "__main__":
    nums = [3, -2, 4]
    target = 2

    res = two_sum_2(nums, target)
    print(res)
