class Solution:
    def maxSlidingWindow(self, nums, k):
        # Edge case: k and nums length are the same
        if k == len(nums):
            nums.sort()
            return [nums[-1]]

        def getWindowMax(p1_ind):
            window_max = float("-inf")
            for i in range(k):
                window_max = max(window_max, nums[i + p1_ind])
            return window_max

        latest_window_max = getWindowMax(0)  # initialize window
        p1, p2, answer = 0, k - 1, [latest_window_max]

        while True:
            p2 += 1
            p1 += 1

            # Exit loop if p2 is out of bounds
            if p2 >= len(nums):
                break

            # If we ditch the largest number in the prev window...
            # Calc max again by looping through the whole window
            if nums[p1 - 1] == latest_window_max:
                latest_window_max = getWindowMax(p1)
            # If we ditch a diff number in the prev window's max
            # Save the larger num between the latest max nu and the new num we just reached
            else:
                latest_window_max = max(latest_window_max, nums[p2])

            answer.append(latest_window_max)

        return answer


sol = Solution().maxSlidingWindow([20, 3, -1, -3, 5, 6, 6, 7], 2)
print(sol)
