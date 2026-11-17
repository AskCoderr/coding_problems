class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(string):
            lengt = len(string)
            if lengt % 2 == 0:
                b = int(lengt / 2)
                a = b - 1

            else:
                b = (lengt // 2) + 1
                a = b - 2

            while a >= 0:
                if string[a] != string[b]:
                    return False
                a -= 1
                b += 1
            return True

        length = len(s)
        li = [s[0], 1]
        for i in enumerate(s):
            if (i[0] + li[1]) >= length:
                break
            for k in enumerate(s[: i[0] + (li[1] - 1) : -1]):
                if i[1] == k[1]:
                    temp = s[i[0] : (length - k[0])]
                    if isPal(temp):
                        li[0] = temp
                        li[1] = len(temp)
                        break
        return li[0]


print(Solution().longestPalindrome("malayalamalayalam"))
