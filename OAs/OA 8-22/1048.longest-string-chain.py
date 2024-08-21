#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        # Sort by length desc
        words.sort(key=len, reverse=True)    
        # Map word to index
        word_index = {}

        for i, w in enumerate(words):
            word_index[w] = i


        dp = {} # Map index to length of its chain

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 # Because one word by itself is considered chain len 1

            # Loop through the characters of current word, test preds by removing char
            for j in range(len(words[i])):
                w = words[i]
                pred = w[:j] + w[j+1:]
                print(pred)
                
                # If pred is a word from words, find longest chain
                if pred in word_index:
                    res = max(res, 1 + dfs(word_index[pred]))

            dp[i] = res # Map the index to the current length max chain len computed
            return res

        # Loop through, calling dfs at each starting word - not inefficient due to caching
        for i in range(len(words)):
            dfs(i)

        # Return the max chain legnth found 
        return max(dp.values())



# @lc code=end

