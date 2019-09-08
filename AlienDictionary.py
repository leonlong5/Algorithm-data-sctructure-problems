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
# class Solution:
#     def alienOrder(self, words):
#         pre = collections.defaultdict(set)
#         suc = collections.defaultdict(set)
#
#         for a,b in zip(words, words[1:]):

