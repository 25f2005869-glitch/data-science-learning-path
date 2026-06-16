# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Trie Prefix Search
# Day         : 71
# Description : Prefix search and autocomplete using Trie.
# ==========================================================

class TrieNode:

    def __init__(self):

        self.children = {}

        self.end_of_word = False


class Trie:

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:

                node.children[char] = TrieNode()

            node = node.children[char]

        node.end_of_word = True

    def _dfs(self, node, prefix, results):

        if node.end_of_word:

            results.append(prefix)

        for char, child in node.children.items():

            self._dfs(

                child,

                prefix + char,

                results

            )

    def prefix_search(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:

                return []

            node = node.children[char]

        results = []

        self._dfs(

            node,

            prefix,

            results

        )

        return results


trie = Trie()

words = [

    "APPLE",

    "APPLICATION",

    "APPLY",

    "APE",

    "BALL"

]

for word in words:

    trie.insert(word)

print("Words Starting With APP:\n")

print(trie.prefix_search("APP"))