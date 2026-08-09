class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = [None, None]

class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        BIT = 30  # since nums[i] can be up to ~1e9 < 2^30
        
        root = TrieNode()
        
        def insert(num):
            node = root
            for i in range(BIT, -1, -1):
                bit = (num >> i) & 1
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        def query(x):
            # root has no children means trie is empty
            if root.children[0] is None and root.children[1] is None:
                return -1
            node = root
            result = 0
            for i in range(BIT, -1, -1):
                bit = (x >> i) & 1
                want = 1 - bit  # opposite bit maximizes XOR
                if node.children[want] is not None:
                    result |= (1 << i)
                    node = node.children[want]
                else:
                    node = node.children[bit]
            return result
        
        # Sort nums, sort queries by mi
        nums.sort()
        indexed_queries = sorted(range(len(queries)), key=lambda i: queries[i][1])
        
        answer = [-1] * len(queries)
        idx = 0  # pointer into sorted nums
        n = len(nums)
        
        for qi in indexed_queries:
            x, m = queries[qi]
            # insert all nums <= m into trie
            while idx < n and nums[idx] <= m:
                insert(nums[idx])
                idx += 1
            answer[qi] = query(x)
        
        return answer