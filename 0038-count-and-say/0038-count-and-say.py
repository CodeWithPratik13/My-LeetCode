class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            ans = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    ans.append(str(count))
                    ans.append(s[i - 1])
                    count = 1

            ans.append(str(count))
            ans.append(s[-1])

            s = "".join(ans)

        return s