class Solution:
    def __init__(self):
        self.dictionary = {}
        self.main_list = None
    
    def list_maker(self, triangle, position):
        lis = []
        var = 1
        for i in range(len(triangle) - position[1]):
            temp = []
            for k in range(var):
                temp.append(triangle[position[1]+i][position[0]+k])
            lis.append(temp)
            var += 1
            
        return lis
    
    def main(self, triangle, xy):
        if self.main_list == None:
            self.main_list = triangle
        current_element = [triangle[-1].index(min(triangle[-1])), len(triangle) - 1]
        summ = 0
        while current_element[1] >= 0:
            summ += triangle[current_element[1]][current_element[0]]
            minimums = []
            least_sum = [summ, current_element[0]]
            for i in range(current_element[1]+1):
                if triangle[current_element[1]][i] < triangle[current_element[1]][current_element[0]]:
                    minimums.append(i)
            if len(minimums) != 0:
                for i in minimums:
                    if (xy[0]+i, xy[1]+current_element[1]) not in self.dictionary:
                        new_list = self.list_maker(triangle, (i, current_element[1]))
                        new_sum = self.main(new_list, ((xy[0]+i), (xy[1]+current_element[1])))
                    else:
                        new_sum = self.dictionary[((xy[0]+i), (xy[1]+current_element[1]))]
                    if new_sum < least_sum[0]:
                        least_sum = [new_sum, i]
                summ = least_sum[0]
                current_element[0] = least_sum[1]
                    
                
            current_element[1] -= 1
            if current_element[0] == len(triangle[current_element[1]]):
                current_element[0] -= 1
            elif current_element[0] != 0:
                if triangle[current_element[1]][current_element[0]] > triangle[current_element[1]][current_element[0]-1]:
                    current_element[0] -= 1
        
        if xy not in self.dictionary:
            self.dictionary[xy] = summ
        return summ

    
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        return self.main(triangle, (0, 0))
        
li = [[2],[3,4],[6,5,7],[4,1,8,3]]        
print(Solution().minimumTotal(li))

# https://leetcode.com/problems/triangle/description/?envType=problem-list-v2&envId=dynamic-programming
