
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 999
        for string_candicate in strs:
            current_length = len(string_candicate)
            if min_length > current_length:
                min_length = current_length
        number_of_strs = len(strs)
        common_prefix = ''
        candicate_char = ''
        for index in range(0, min_length):
            count = 0
            for j, string_candicate in enumerate(strs):
                char = string_candicate[index]
                if j == 0:
                    candicate_char = char
                if candicate_char == char:
                    count += 1
            if count == number_of_strs:
                common_prefix += candicate_char
            else:
                if index > 0:
                    return common_prefix
                else:
                    return ''
        return common_prefix


if __name__ == '__main__':
    so = Solution()
    # strs = ["flower", "flow", "flight"]
    strs = ["cardog", "carracecar", "car"]
    # strs = ["baac", "acb", "bacc", "cb"]
    result = so.longestCommonPrefix(strs)
    print(result)