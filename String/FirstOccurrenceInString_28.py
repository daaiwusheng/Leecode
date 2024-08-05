class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 获取haystack和needle的长度
        h_len = len(haystack)
        n_len = len(needle)

        # 如果needle为空，返回0
        if n_len == 0:
            return 0

        # 如果needle长度大于haystack长度，返回-1
        if n_len > h_len:
            return -1

        # 遍历haystack
        for i in range(h_len - n_len + 1):
            # 检查当前子字符串是否等于needle
            if haystack[i:i + n_len] == needle:
                return i

        # 如果没有找到，返回-1
        return -1


if __name__ == '__main__':
    solution = Solution()
    haystack = 'mississippi'
    needle = "issip"

    # haystack = 'a'
    # needle = "a"

    # haystack = 'a'
    # needle = "aa"

    # haystack = 'abcabdef'
    # needle = "ef"

    result = solution.strStr(haystack, needle)
    print(result)
