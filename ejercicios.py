class Solution:
    def fizzBuzz(self, n: int): 
        L1 = []
        #breakpoint()
        for i in range (1,n):
            if i % 5 == 0 and i % 3 == 0: 
                L1.append("Fizz Buzz")
                
            elif i % 5 == 0: 
                L1.append("Buzz")
                
            elif i % 3 == 0: 
                L1.append("Fizz")
                
            else: 
                L1.append(str(i))
                #breakpoint()
        return L1           

s = Solution() 
print(s.fizzBuzz(3))