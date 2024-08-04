class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        match_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        if s[0] not in match_map:
            return False
        i = 0
        while len(s):
            char_current = s[i]
            if char_current not in match_map:
                return False
            target = match_map[char_current]
            if i + 1 < len(s) and s[i + 1] == target:
                s = s[0:i] + s[i + 2:]
                i = 0
            else:
                i += 1
            if i == len(s) - 1:
                return False
        if len(s) == 0:
            return True
        else:
            return False


if __name__ == "__main__":

    solution = Solution()
    s = "[({(())}[()])]"

    print(solution.isValid(s))

    s_list = [
        '()', '({[]})', '{}[]()(}', '{}[]()', "){", "(([]){})", "[([]])", '[([])[]][]','{[]}()'
    ]
    for index, string_test in enumerate(s_list):
        result = solution.isValid(string_test)
        print(f'{index}  is {result}')
