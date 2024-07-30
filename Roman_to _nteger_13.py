class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        length = len(s)

        for i in range(length):
            # 获取当前和下一个罗马数字的值
            current_value = roman_to_value[s[i]]
            if i + 1 < length:
                next_value = roman_to_value[s[i + 1]]
                if current_value < next_value:
                    total -= current_value
                else:
                    total += current_value
            else:
                total += current_value

        return total


if __name__ == '__main__':
    solution = Solution()
    result = solution.romanToInt('XLI')
    print(result)

