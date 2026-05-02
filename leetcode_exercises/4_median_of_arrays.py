"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List


def find_median_sorted_arrays_1(nums1: List[int], nums2: List[int]) -> float:
    merged = sorted(nums1 + nums2)
    return (merged[len(merged) // 2] + merged[(len(merged) - 1) // 2]) / 2


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:

    nums_a, nums_b = (nums2, nums1) if (len(nums2) < len(nums1)) else (nums1, nums2)
    m, n = len(nums_a), len(nums_b)
    print(f"nums_a: {nums_a}, nums_b: {nums_b}")
    print(f"m: {m}, n: {n}")
    left = 0
    right = m
    while left <= right:
        partition_a = (left + right) // 2
        partition_b = (m + n + 1) // 2 - partition_a
        print(f"partition_a: {partition_a}, partition_b: {partition_b}")

        max_left_a = float("-inf")  if partition_a - 1 < 0 else nums_a[partition_a - 1]
        min_right_a = float("inf") if partition_a >= m else nums_a[partition_a]
        max_left_b = float("-inf") if partition_b - 1 < 0 else nums_b[partition_b - 1]
        min_right_b = float("inf") if partition_b >= n else nums_b[partition_b]

        if max_left_a > min_right_b:
            right = partition_a - 1
        if max_left_b > min_right_a:
            left = partition_a + 1

        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2
            else:
                return max(max_left_a, max_left_b)


if __name__ == "__main__":
    # nums1 = [1,2,3,4,5]
    # nums2 = [6,7,8,9,10,11,12,13,14,15,16,17]
    nums2 = [1, 3]
    nums1 = [2]
    # nums1 = [1,2, 5]
    # nums2 = [3,4]
    print(f"nums1: {nums1}, nums2: {nums2}")
    print(f"median of the two sorted arrays: {find_median_sorted_arrays_1(nums1, nums2)}")
    print(f"median of the two sorted arrays: {find_median_sorted_arrays(nums1, nums2)}")
