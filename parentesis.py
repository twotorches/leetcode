class Solution:
    def isValid(self, s: str) -> bool:
        answer = True
        for element in s:
            if element == "(" :
                answer = True
            elif element == "{" :
                answer = True
            elif element == "[" :
                answer = True
        return answer
    
sol = Solution()
print(sol.isValid("()[]{}"))    

             
