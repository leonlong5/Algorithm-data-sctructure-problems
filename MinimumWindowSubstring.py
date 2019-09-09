S = "ADOBECODEBANC"
T = "ABC"
# Output: "BANC"

import collections
def minWindow(s, t):
    if not s or len(s) < len(t): return ''

    #first count the letter in t
    counter = collections.Counter(t)

    #use sliding window
    left = 0      #window left boundary
    total = len(t)    #total keep tracking num of char used in t

    #used minStart to track cur minimum window start position and its length minLen
    #this is used to check two cases:
    #1 when complete, thw whole string is no valid
    #2 when complete, the whole string is a valid string
    # if case 1 the minLen would smaller than len(s)

    min_start = 0
    min_len = len(s)

    for right, c in enumerate(s):
        if c in counter:
            if counter[c] > 0: total -= 1  #only counter[c] > 0, we reduce valid total
            counter[c] -= 1

            while total == 0:       #while total == 0 we know we find a window, update minStart
                if min_len > right - left:
                    min_start = left
                    min_len = right - left

                if s[left] in counter:
                    counter[s[left]] += 1
                    if counter[s[left]] > 0:
                        total += 1
                left += 1
    if min_len == len(s):
        return ''
    return s[min_start:min_start+min_len+1]


data = minWindow(S, T)
print(data)