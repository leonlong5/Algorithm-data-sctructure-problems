# example 1:
#
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# Output: "wertf"
# Example 2:
#
# Input:
# [
#   "z",
#   "x"
# ]
#
# Output: "zx"
# Example 3:
#
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]

import collections
#problem want us to order the string by given words, words are sorted
#so we just need to compare vertically the letters, use the order to build a graph
#then do topological sort and bfs to get the order of the letters
class Solution:
    def alienOrder(self, words):
        # 1. use two map:set to store all the pre, suc
        pre = collections.defaultdict(set)
        suc = collections.defaultdict(set)

        #group adjecent pair words with zip, then group the letter between them
        #if two letters are not the same, we find an order, add to suc and pre set, remember to break
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break

        # 2. filter out the unique letters in all words
        s = set()
        for word in words:
            for c in word:
                s.add(c)

        # 3. add all the letters does not has pre edegs(indegree) to queue
        queue = collections.deque([])
        for c in s:
            if c not in pre:
                queue.append(c)

        # 4. BFS to pop char add to final result
        res = ''
        while queue:
            char = queue.popleft()
            res += char
            for c in suc[char]:
                pre[c].discard(char) #discard indegree
                if not pre[c]:       #when no more indegree, add this letter to queue
                    queue.append(c)
        if set(res) != s:        #edege case, if result chars not match s, return ''
            return ''
        return res


words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
solution = Solution()
data = solution.alienOrder(words)
print(data)