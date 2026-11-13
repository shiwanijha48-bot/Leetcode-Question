class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                l = i+1
            count += i - l+1
        return count


'''
4089. Count Subarrays With Loose Bounds
Solved
Medium
premium lock icon
Companies
Hint
You are given an integer array nums and two integers minK and maxK.

A loose-bound subarray is a subarray in which every element is greater than or equal to minK and less than or equal to maxK.

Return the number of loose-bound subarrays in nums.

 

Example 1:

Input: nums = [1,4,7,3], minK = 1, maxK = 5

Output: 4

Explanation:

The loose-bound subarrays are [1], [4], [3], and [1, 4]. The minimum value in these subarrays is at least minK = 1 and the maximum value is at most maxK = 5.

Example 2:

Input: nums = [1,1], minK = 1, maxK = 1

Output: 3

Explanation:

The loose-bound subarrays are [1], [1], and [1, 1]. The minimum value in these subarrays is at least minK = 1 and the maximum value is at most maxK = 1.

 

Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
'''
