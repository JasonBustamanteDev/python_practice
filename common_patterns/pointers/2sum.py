class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums) # sort lowest to highest

        p1 = 0
        p2 = len(nums) - 1
        
        while p1 < p2:
            p1_val = sorted_nums[p1]
            p2_val = sorted_nums[p2]
            sum = p1_val + p2_val

            if sum == target:
                pair_num_1 = p1_val
                pair_num_2 = p2_val
                break
            elif sum > target:
                p2 -= 1
            elif sum < target:
                p1 += 1

        # Locate the original index positions of both ints in pair
        i1 = nums.index(pair_num_1)
        if pair_num_1 == pair_num_2:
            i2 = nums.index(pair_num_2, i1 + 1)
        else:
            i2 = nums.index(pair_num_2)
            
        return [i1, i2]

        

s = Solution().twoSum([3, 3], 6)
print(s)