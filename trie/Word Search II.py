"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.



Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
    words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 10^4
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.

Hide Hint #1
    You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
Hide Hint #2
    If the current candidate does not exist in all words' prefix, you could stop backtracking immediately.
    What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not?
    How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem:
    Implement Trie (Prefix Tree) first.

"""
from typing import List
from functools import lru_cache
from collections import Counter


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word

    def __str__(self):
        return str(self.root)


class Solution:
    def __init__(self):
        self.res = []

    def valid_word(self, word_counter, board_counter):
        for k in word_counter:
            try:
                if word_counter[k] > board_counter[k]:
                    return False
            except KeyError:
                return False
        return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        board_tmp = []
        for i in board:
            board_tmp.extend(i)
        board_counter = Counter(board_tmp)
        trie = Trie()
        for word in words:
            word_counter = Counter(word)
            if self.valid_word(word_counter, board_counter):
                trie.insert(word)

        m = len(board)
        n = len(board[0])

        @lru_cache(100000)
        def backtrack(i, j, node):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            c = board[i][j]
            if c not in node.children:
                return
            node = node.children[c]
            if node.word is not None:  # found a word
                self.res.append(node.word)
                node.word = None  # remove the duplicate

            # all candidate
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ix, jy = i + x, j + y

                backtrack(ix, jy, node)

        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie.root)
        return self.res


if __name__ == '__main__':
    board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    words = ["oa", "oaa"]
    # board = [["a", "b", "c", "e"], ["z", "z", "d", "z"], ["z", "z", "c", "z"], ["z", "a", "b", "z"]]
    # words = ["abcdce"]

    # board = [["a", "a"]]
    # words = ["a"]

    solution = Solution()
    res = solution.findWords(board, words)
    print(res)
