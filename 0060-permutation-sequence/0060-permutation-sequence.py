class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        result = ""
        factorial = 1
        for i in range(1, n):
            factorial *= i
        k -= 1 
        for i in range(n, 0, -1):
            index = k // factorial
            result += nums[index]
            nums.pop(index)
            k = k % factorial
            if i > 1:
                factorial //= (i - 1)
        return result