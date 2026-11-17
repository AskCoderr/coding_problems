class Solution:
    def isValid(self, s: str) -> bool:
        def pair(brkt):
            if brkt == ")":
                return "("
            if brkt == "]":
                return "["
            if brkt == "}":
                return "{"

        li = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                li.append(i)
            else:
                if len(li) == 0:
                    return False
                if li.pop() != pair(i):
                    return False

        if len(li) == 0:
            return True
        else:
            return False


print(Solution().isValid("([([)]])"))
# https://leetcode.com/problems/valid-parentheses/

# i donno why at first i tried to solve the problem with the following code silly me

# class Solution:
#     def isValid(self, s: str) -> bool:
#         var_vals = {"a": 0, "b": 0, "c": 0}
#         d = 0
#         li = []
#         brckt_vals = {"(": ("a", 1), ")": ("a", -1),
#                       "[": ("b", 1), "]": ("b", -1), "{": ("c", 1), "}": ("c", -1)}

#         while d < len(s):  # will change the condition
#             var_vals[brckt_vals[s[d]][0]] += brckt_vals[s[d]][1]
#             if var_vals["a"] < 0 or var_vals["b"] < 0 or var_vals["c"] < 0:
#                 return False
#             for i in var_vals.keys():
#                 if i not in li and var_vals[i] == 1:
#                     li.append(i)
#                 if i in li and var_vals[i] == 0:
#                     if li[-1] != li.pop(li.index(i)):
#                         return False
#             d += 1

#         if len(set(var_vals.values())) == 1 and tuple(set(var_vals.values()))[0] == 0:
#             return True
#         else:
#             return False

# the current problem is i am not giving a variable to each instance of a type of bracket so when there are
# 2 or more instances of the same bracket and one of them closes in the wrong order it does not catch the error
