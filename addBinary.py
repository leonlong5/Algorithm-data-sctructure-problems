# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
def addBinary(self, a: str, b: str) -> str:
    n = len(a) - 1
    m = len(b) - 1
    carry = 0
    res = ''
    while n >= 0 or m >= 0 or carry == 1:
        cur = carry
        if n >= 0:
            cur += int(a[n])
            n -= 1
        if m >= 0:
            cur += int(b[m])
            m -= 1
        carry = cur // 2
        cur = cur % 2
        res = str(cur) + res
    return res