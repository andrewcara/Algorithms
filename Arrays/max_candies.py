class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        return [candy+extraCandies >= maxCandies for candy in candies]
        