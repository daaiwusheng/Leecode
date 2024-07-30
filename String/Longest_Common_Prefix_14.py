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

    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # 以第一个字符串为基准
        prefix = strs[0]

        # 遍历列表中的每一个字符串
        for s in strs[1:]:
            # 逐个字符比较
            i = 0
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1
            # 更新当前前缀
            prefix = prefix[:i]
            # 如果前缀为空，直接返回
            if not prefix:
                return ""

        return prefix


if __name__ == '__main__':
    so = Solution()
    # strs = ["flower", "flow", "flight"]
    strs = ["cardog", "carracecar", "car"]
    # strs = ["baac", "acb", "bacc", "cb"]
    result = so.longestCommonPrefix(strs)
    print(result)