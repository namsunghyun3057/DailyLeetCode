class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        ans = []
        for i in candies:
            if max < i: max = i
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max:
                ans.append(True)
            else: ans.append(False)
        return ans