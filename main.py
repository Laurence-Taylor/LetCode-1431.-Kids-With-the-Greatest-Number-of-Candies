class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # find the max amount
        max_amount_candies = max(candies)
        # return the list 
        return [max_amount_candies <= candies[i] + extraCandies  for i in range(len(candies))]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.kidsWithCandies([2,3,5,1,3], 3))