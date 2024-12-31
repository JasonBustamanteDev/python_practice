import re


class Solution(object):
    def isPalindrome(self, s):
        # Remove non alphanumeric chars and decapitalize each one
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()

        answer = True
        p1 = 0
        p2 = len(s) - 1

        # Niche case: Empty string
        if len(s) == 0:
            return answer

        while True:
            char1 = s[p1]
            char2 = s[p2]

            # End condition: when 2 pointers meet or cross each other
            if p1 >= p2:
                break

            # If chars match, increment p1 and decrement p2
            if char1 == char2:
                p1 += 1
                p2 -= 1
            # If chars don't match return False b/c it is not a valid palindrome
            else:
                answer = False
                break

        return answer


sol = Solution().isPalindrome("")
print(sol)
