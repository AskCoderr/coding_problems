class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = 0
        b = 0
        c = 0
        out = ""
        li = []

        if len(strs) == 1:
            return strs[0]

        for i in strs[strs.index(max(strs, key=len))]:
            li.append(i)

        strs.pop(strs.index(max(strs, key=len)))

        for i in strs:
            for k in i:
                if k == li[b]:
                    b += 1
                else:
                    break
            if b == 0:
                return out
            if c != 0:
                if b < a:
                    a = b
            else:
                a = b
            b = 0
            c += 1

        for m in range(a):
            out = out + li[m]

        return out


print(Solution().longestCommonPrefix(["flower", "flow", "fly"]))
# garbage candy code i hate it tbh
# https://leetcode.com/problems/longest-common-prefix/
