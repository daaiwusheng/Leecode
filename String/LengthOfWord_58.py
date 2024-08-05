class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        worlds = s.split(' ')
        for item in reversed(worlds):
            if item != '':
                return len(item)
        return 0


if __name__ == '__main__':
    solution = Solution()
    # s = "   fly me   to   the moon  "
    # s = "Hello World"
    # s = "luffy is still joyboy"
    s = 'a'
    print(solution.lengthOfLastWord(s))
