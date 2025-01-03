import string


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        string_length = len(s)
        # Edge case: 0 length string
        if string_length == 0:
            return 0
        # Edge case: 1 length string
        if string_length == 1:
            return 1

        possible_chars = string.digits + string.ascii_letters + string.whitespace + string.punctuation
        char_freq = { letter: [] for letter in possible_chars}

        p1, p2, max_length = 0, 1, 1
        char_freq[s[p1]] = [p1]  # record p1 data in freq object

        while p2 < string_length:
            p2_char = s[p2]
            char_freq[p2_char].append(p2)  # record in freq obj

            # If p2 points to a unique char, record new max length, update, freq_obj, then iterate p2
            if len(char_freq[p2_char]) < 2:
                max_length = max(max_length, p2 - p1 + 1)
                p2 += 1
                continue

            # If p2 points to a duplicate character, choose 1 of 2 options
            p1_target = char_freq[p2_char][0] + 1
            decount_iterations = p1_target - p1
            redo_substring_iterations = p2 - p1_target

            # Edge case: If p1_target is out of bounds, exit the function (happens when dupe letter is last)
            if p1_target >= string_length:
                return max_length

            # OPTION 1: REDO SUBSTRING
            elif redo_substring_iterations < decount_iterations:
                # Reset freq_obj
                possible_chars = string.digits + string.ascii_letters + string.whitespace + string.punctuation
                char_freq = { letter: [] for letter in possible_chars}
                # Reposition p1 at p1_target index and add the data to our freq object
                p1 = p1_target
                char_freq[s[p1]] = [p1] 
                p2 = p1 + 1 # Position p2 1 spot after
                continue
            
            # OPTION 2: DECOUNT
            # Remove data from freq_object up to but not including p1_target, then move 
            else:
                # Remove data from freq_object up to but not including p1_target
                for i in range(p1, p1_target):
                    deleting_char = s[i]
                    char_freq[deleting_char].remove(i)
                # Position p1 at p1_target_index
                p1 = p1_target
                # Remove data for p2 since the logic @top of while loop will re-record it
                char_freq[p2_char].pop(-1)
                continue

        return max_length

sol = Solution().lengthOfLongestSubstring("zz")

# sol = Solution().lengthOfLongestSubstring("hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
print(sol)
