"""
The solution code for word ladder question on leetcode.

Author: Shun Nagasaki

Problem:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

===Example===
Input: beginWord = "hit",
endWord = "cog", 
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
=============
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # length of each word
        length = len(beginWord)
        data = defaultdict(list)
        
        # create a dictionary that holds adjacnt words
        # key: word with one missing letter 
        # ex. hit --> *it, h*t, hi*
        # value: all adjacent words
        # ex. *it --> hot, dot, lot
        for word in wordList:
            for i in range(length):
                data[word[:i]+'*'+word[i+1:]].append(word)
        
        # queue is used for BFS
        queue = deque([beginWord])
        # seen keeps track of which word is already seen in the shortest path
        seen = set()
        dist = 1
        
        # this becomes a simple BFS problem
        while queue:
            qlen = len(queue)

            for _ in range(qlen):
                curr = queue.popleft()
                # for the current word, grab adjacent word list from dictionary.
                # do this for each pattern of the current word
                # ex. curr = hot --> do it for *it, h*t, hi*
                for i in range(length):
                    adj_words = data[curr[:i]+'*'+curr[i+1:]]
                    # for each word in adjacent word list, check if it's already seen.
                    # if it is, then skip it
                    # if the word is the endWord, then just return the current distance + 1.
                    # make sure to add the word to the 'seen' set so that we can skip it next time we encounter it
                    # add the word to the queue for BFS purpose
                    for word in adj_words:
                    
                        if word in seen:
                            continue

                        if word == endWord:
                            return dist + 1

                        seen.add(word)
                        queue.append(word)
            
            dist += 1
        
        # return 0 if there is no path from beginWord to endWord
        return 0