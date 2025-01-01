class Solution(object):
    def threeSum(self, nums):
        unique_answers = set()  # holds unique tuples
        nums.sort()  # Order the nums list (lowest to highest)

        # Instant end: all numbers are positive
        if nums[0] > 0:
            return []
        # Instant end: all numbers are negative
        if nums[0] < 0 and nums[-1] < 0:
            return []

        p1, p2, p3 = 0, 1, 2

        # Iterate p1 up to and excluding the second last nums integer
        for i in range(len(nums) - 2):
            p1 = i
            p2 = p1 + 1
            p3 = len(nums) - 1

            p1_val = nums[p1]
            target_sum = p1_val * -1

            # Optimization: No 3sum combinations are possible if p1 is on a positive number
            if p1_val > 0:
                break

            # Perform 2sum on the subarray to the right of p1
            while p2 < p3:
                # Optimization: Skip 2sum if there are no possible combinations that add up to 0
                # Can tell there's no chance if we get the sum of p1_val + final_2_ints  and it's negative
                if (p1_val + nums[-1] + nums[-2]) < 0:
                    break

                p2_val, p3_val = nums[p2], nums[p3]
                sum = p2_val + p3_val

                if sum < target_sum:
                    p2 += 1
                elif sum > target_sum:
                    p3 -= 1
                else:
                    # 3sum found:
                    # Save answers in the unique_answers set which refuses entry to previously seen triplets
                    unique_answers.add(tuple((p1_val, p2_val, p3_val)))
                    # Constrict both 2sum pointers (no point to moving only one of p2 or p3)
                    # The only way we could get another target_sum is if we encounter duplicates, which we deliberately ignore anyway
                    p2 += 1
                    p3 -= 1

        return [list(triplet) for triplet in unique_answers]


sol = Solution().threeSum([-1, 0, 1, 2, -1, -4])  # [[-1,-1,2],[-1,0,1]]
print(sol)
