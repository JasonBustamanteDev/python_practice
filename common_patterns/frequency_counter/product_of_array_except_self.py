class Solution(object):
    def productExceptSelf(self, nums):
        answer = []

        # Create list of products by looping from L → R
        left_products = []
        latest_product = 1
        for num in nums: # O(n)
            latest_product = latest_product * num # O(1)
            left_products.append(latest_product) # O(1)

        # Create list of products by looping from R → L
        right_products = []
        latest_product = 1  # reinit
        for num in reversed(nums): # O(n)
            latest_product = latest_product * num # O(1)
            right_products.append(latest_product) # O(1)
        # Reverse the right products list (we avoided re-indexing by using append earlier)
        right_products.reverse() # O(n)

        # Calc each item in answer by multiplying products to the left / right of index i
        for i, num in enumerate(nums): # O(n) for loop + O(n) for enumerate = O(2n)
            left_index = i - 1
            right_index = i + 1

            if left_index < 0:
                lp = 1  # if there is no product left of i, multiply by 1
            else:
                lp = left_products[left_index]

            if right_index > len(nums) - 1:
                rp = 1  # if there is no product right of i, multiply by 1
            else:
                rp = right_products[right_index]

            answer.append(lp * rp) # Everything in this scope is O(1)

        return answer


sol = Solution().productExceptSelf([1, 2, 3, 4])
print(sol)  # [24,12,8,6]
sol = Solution().productExceptSelf([-1, 1, 0, -3, 3])
