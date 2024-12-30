class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        # Create a frequency object the counts the appearances of each int
        for num in nums:  # O(n)
            freq[num] = freq.get(num, 0) + 1  # O(1)

        # Create a list of objects containing the KVPs of freq
        freq_list = []
        for key in freq:  # O(n)
            freq_list.append({"int": key, "count": freq[key]})  # O(1)

        # Sort freq_list using the count
        def count_val(d):
            return d.get("count")  # O(1)

        # O(n log n), but is guaranteed to be better than worst case (freq object much smaller than n)
        freq_list.sort(key=count_val, reverse=True)

        return [obj["int"] for obj in freq_list[0:k]]  # return new list of top K int


sol = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(sol)
