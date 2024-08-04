class Solution:
    def isValid_0(self, s: str) -> bool:
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

    def isValid(self, s: str) -> bool:
        # Dictionary to hold matching pairs
        match_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        # Stack to keep track of opening brackets
        stack = []

        for char_curret in s:
            if char_curret in match_map:
                stack.append(char_curret)
            elif char_curret in match_map.values():
                if stack and match_map[stack[-1]] == char_curret:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return not stack




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
