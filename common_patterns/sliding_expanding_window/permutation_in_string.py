from collections import Counter
import string


class Solution:
    def checkInclusion(self, s1, s2):
        # Edge case s1 longer than s2 (no permutations possible)
        if len(s1) > len(s2):
            return False

        p1, p2 = 0, len(s1) - 1

        freq_s1 = Counter({char: 0 for char in string.ascii_lowercase})
        for i in range(len(s1)):
            freq_s1[s1[i]] += 1

        freq_window = Counter({char: 0 for char in string.ascii_lowercase})
        for i in range(len(s1)):
            freq_window[s2[i]] += 1

        while p2 < len(s2):
            # Check to see if the current freq_window matches freq_s1
            if freq_window == freq_s1:
                return True  # O(1) since the set of chars is limited

            # Slide window forward, but end the loop if p2 goes out of bounds (keyError)
            p1 += 1
            p2 += 1
            if p2 >= len(s2):
                break

            # Update the freq_window
            freq_window[s2[p1 - 1]] -= 1  # decount char we ditched
            freq_window[s2[p2]] += 1  # count char we just encountered

        return False


s1 = "ab"
s2 = "adboaa"
sol = Solution().checkInclusion(s1, s2)
print(sol)
