class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]

        for i in range(1, len(triangle)):
            row = triangle[i]
            new_dp = [0] * len(row)

            for j in range(len(row)):
                if j == 0:
                    new_dp[j] = dp[j] + row[j]

                elif j == len(row) - 1:
                    new_dp[j] = dp[j - 1] + row[j]

                else:
                    new_dp[j] = min(dp[j - 1], dp[j]) + row[j]

            dp = new_dp

        return min(dp)