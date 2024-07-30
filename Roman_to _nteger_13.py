class Solution:
    def romanToInt(self, s: str) -> int:
        numbers_from_string = []
        for roman_char in s:
            if roman_char == 'I':
                numbers_from_string.append(1)
            elif roman_char == 'V':
                numbers_from_string.append(5)
            elif roman_char == 'X':
                numbers_from_string.append(10)
            elif roman_char == 'L':
                numbers_from_string.append(50)
            elif roman_char == 'C':
                numbers_from_string.append(100)
            elif roman_char == 'D':
                numbers_from_string.append(500)
            else:
                numbers_from_string.append(1000)
        length_of_numbers = len(numbers_from_string)
        result_number = 0
        for index, number in enumerate(numbers_from_string):
            if index < length_of_numbers - 1:
                next_number = numbers_from_string[index+1]
                if number < next_number:
                    result_number -= number
                else:
                    result_number += number
            else:
                result_number += number
        return result_number


if __name__ == '__main__':
    solution = Solution()
    result = solution.romanToInt('XLI')
    print(result)

