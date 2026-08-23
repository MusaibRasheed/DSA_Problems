from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        email_to_index = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(i, email_to_index[email])
                else:
                    email_to_index[email] = i

        groups = defaultdict(set)
        for i in range(len(accounts)):
            root = find(i)
            groups[root].update(accounts[i][1:])

        result = []
        for root, emails in groups.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result