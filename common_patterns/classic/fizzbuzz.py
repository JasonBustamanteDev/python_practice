class Solution(object):
    def fizzBuzz(self, n):
        answer = []

        for i in range(1, n + 1):
            remainder3 = i % 3
            remainder5 = i % 5

            if remainder3 + remainder5 == 0:
                answer.append("FizzBuzz")
            elif remainder3 == 0:
                answer.append("Fizz")
            elif remainder5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer


sol = Solution().fizzBuzz(15)
print(sol)
