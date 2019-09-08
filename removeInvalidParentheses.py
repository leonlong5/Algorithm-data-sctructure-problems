# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        res = []
        self.dfs(s, res, l, r, 0)
        return res

    def dfs(self, s, res, l, r, start):
        if l == 0 and r == 0 and self.isValid(s):
            res.append(s)
            return
        n = len(s)
        for i in range(start, n):
            if i > start and s[i] == s[i - 1]: continue
            new_s = s[:i] + s[i + 1:]

            if s[i] == ')' and r > 0: self.dfs(new_s, res, l, r - 1, i)
            if s[i] == '(' and l > 0: self.dfs(new_s, res, l - 1, r, i)

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
            if count < 0: return False
        return count == 0
