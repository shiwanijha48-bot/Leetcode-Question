class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        a = []
        for i in nums:
            maxi = int(''.join(sorted(str(i), reverse=True)))
            a.append((maxi-i, maxi))
        a.sort(reverse=True)
        ans = sum(nums)
        for i in range(k):
            ans += a[i][0]
        return ans

'''
4093. Maximize Sum After At Most K Digit Rearrangements
Solved
Medium
premium lock icon
Companies
Hint
You are given an integer array nums of length n and an integer k.

In one operation, you may choose any element of nums and rearrange its decimal digits in any order to form a new integer.

Return the maximum possible sum of the array after performing at most k operations.

 

Example 1:

Input: nums = [123,45], k = 1

Output: 366

Explanation:

We choose nums[0] = 123 and rearrange its digits to form 321.
The array becomes [321, 45]. Thus, the total sum is 321 + 45 = 366.
Example 2:

Input: nums = [102,90,14], k = 2

Output: 341

Explanation:

We choose nums[0] = 102 and rearrange its digits to form 210.
We choose nums[2] = 14 and rearrange its digits to form 41.
The array becomes [210, 90, 41]. Thus, the total sum is 210 + 90 + 41 = 341.
 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= n
  '''
