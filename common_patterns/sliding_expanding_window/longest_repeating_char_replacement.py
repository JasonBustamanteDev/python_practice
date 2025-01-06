import string


class Solution(object):
    def characterReplacement(self, s, k):
        string_length = len(s)
        if string_length == 1:
            return 1  # Edge case: 1 char string

        p1, p2, max_length = 0, 1, 1
        freq = {}
        freq[s[p1]] = 1
        freq[s[p2]] = freq.get(s[p2], 0) + 1

        def is_window_valid():
            # FORMULA: validWindow = windowLength - highestFrequencyCharCount <= k
            window_length = p2 - p1 + 1
            highest_freq_char_count = 0
            for char in freq:
                highest_freq_char_count = max(highest_freq_char_count, freq[char])

            return window_length - highest_freq_char_count <= k

        while p2 < string_length:
            # If the window is valid
            if is_window_valid() == True:
                max_length = max(max_length, p2 - p1 + 1)
                p2 += 1  # expand window
                # Update freq object if p2 is still in bounds
                if p2 < string_length:
                    freq[s[p2]] = freq.get(s[p2], 0) + 1
                continue

            # If the window is not valid
            else:
                freq[s[p1]] -= 1  # decount freq obj

                p1 += 1  # Shorten window
                continue

        return max_length


sol = Solution().characterReplacement("AABABBA", 1)
print(sol)
