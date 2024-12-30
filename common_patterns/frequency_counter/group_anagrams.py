class Solution(object):
    def groupAnagrams(self, strs):
        answer = []
        anagram_obj = {}

        for anagram in strs:
            reordered_anagram = "".join(sorted(anagram))
            matches = anagram_obj.get(reordered_anagram, [])
            matches.append(anagram)
            anagram_obj[reordered_anagram] = matches

        for reordered_anagram in anagram_obj:
            answer.append(anagram_obj[reordered_anagram])

        return answer


demo = Solution()
soln = demo.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(soln)
