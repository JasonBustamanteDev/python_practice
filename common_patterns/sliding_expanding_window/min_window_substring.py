from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        min_substring = ""  # Return empty string if no substring exists

        # Edge case t is longer than s (no matches possible)
        if len(s) < len(t):
            return ""

        p1, p2 = 0, len(t) - 1
        freq_t, freq_window = Counter(t), Counter({})
        for i in range(len(t)):
            freq_window[s[i]] += 1  # Initialize freq_window for our first window

        def moveP1Forward():
            nonlocal p1
            p1 += 1
            freq_window[s[p1 - 1]] -= 1

        def moveP1Backward():
            nonlocal p1
            p1 -= 1
            freq_window[s[p1]] += 1

        def isValidWindow(current_freq_object):
            diff = freq_t - current_freq_object  # O(1)
            return len(diff) == 0

        def optimizeWindow(freq_window):
            while p1 < len(s):
                # Decount freq obj then shorten window
                moveP1Forward()

                # If window is no longer valid, the previous iteration's window was fully optimized
                # Undo most recent shorten, update freq object, return indexes
                if isValidWindow(freq_window) is False:
                    moveP1Backward()
                    return

        # Find all optimized windows which contain the chars in t
        while True:
            is_window_valid = isValidWindow(freq_window)

            # If window is not valid and we still got sliding room, iterate p2 and update freq object
            if is_window_valid is False and p2 + 1 < len(s):
                p2 += 1
                freq_window[s[p2]] += 1
                continue

            # If window is not valid and we run out of sliding room, end loop
            elif is_window_valid is False and p2 + 1 >= len(s):
                break

            # IF WINDOW IS VALID
            # Optimize the window (p1 and p2 may be moved, while freq object gets updated)
            optimizeWindow(freq_window)

            # Save the potential min substring
            potential_substring = s[p1 : p2 + 1]
            current_min_length = len(min_substring)
            potential_length = len(potential_substring)
            if current_min_length == 0 or potential_length < current_min_length:
                min_substring = potential_substring

            # Reposition p1 and p2 so that we can look for new valid windows
            # print([min_substring, p1, p2])
            p1 += 1
            p2 += 1
            if p2 >= len(s):
                break
            freq_window[s[p1 - 1]] -= 1
            freq_window[s[p2]] += 1

        return min_substring


sol = Solution().minWindow("BCSAS", "ABC")
print(sol)
