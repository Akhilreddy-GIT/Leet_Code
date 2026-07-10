class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        root = TrieNode()

        # Insert all numbers from arr1
        for num in arr1:
            node = root
            for ch in str(num):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

        ans = 0

        # Find longest matching prefix for each number in arr2
        for num in arr2:
            node = root
            length = 0
            for ch in str(num):
                if ch not in node.children:
                    break
                node = node.children[ch]
                length += 1
            ans = max(ans, length)

        return ans