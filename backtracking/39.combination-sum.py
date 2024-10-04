def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    subset = []

    def dfs(i, cur_sum):
        if cur_sum == target:
            res.append(subset.copy())
            return
        if i >= len(candidates) or cur_sum > target:
            return

        subset.append(candidates[i])
        # add the current element over and over
        dfs(i, cur_sum + candidates[i])

        subset.pop()
        # Backtrack up tree, this time incrementing the pointer to the next elem
        dfs(i + 1, cur_sum)

    dfs(0, 0)

    return res
