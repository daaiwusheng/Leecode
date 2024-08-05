class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        count = 0
        index = -1
        i = 0
        while i < len(haystack) and len(haystack) - i >= len(needle) - count:
            char_hays = haystack[i]
            if count < len(needle):
                if char_hays == needle[count]:
                    if count == 0:
                        index = i
                    count += 1
                    i += 1
                elif char_hays != needle[count]:
                    if index > -1:
                        i = index + 1
                    else:
                        i += 1
                    index = -1
                    count = 0

            if count == len(needle):
                return index

        return -1


if __name__ == '__main__':
    solution = Solution()
    haystack = 'mississippi'
    needle = "issip"

    haystack = 'a'
    needle = "a"

    haystack = 'a'
    needle = "aa"

    haystack = 'abcabdef'
    needle = "ef"

    result = solution.strStr(haystack, needle)
    print(result)
