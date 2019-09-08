# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
import collections
class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)

        # 1. build an email : [accountId1, accountId2] map
        # so from an email, we can find all the accounts associate with it,
        # then keep serach for each email of each accounts, do dfs check merge accounts based on emails
        email_accounts_map = collections.defaultdict(list)
        for i in range(n):
            for email in accounts[i][1:]:
                email_accounts_map[email].append(i)

        # 2. do dfs merge accounts
        visited = set()
        result = []
        for i, account in enumerate(accounts):
            if i in visited: continue
            name = account[0]
            emails = set()
            self.dfs(accounts, i, visited, emails, email_accounts_map)
            result.append([name, *sorted(emails)])
        return result

    def dfs(self, accounts, i, visited, emails, email_accounts_map):
        if i in visited: return
        visited.add(i)
        for email in accounts[i][1:]:
            emails.add(email)
            for nei in email_accounts_map[email]:
                self.dfs(accounts, nei, visited, emails, email_accounts_map)


solution = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
data = solution.accountsMerge(accounts)
print(data)