class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    solution = Solution()
    result = solution.addBinary('1001', '01')
    print(result)
