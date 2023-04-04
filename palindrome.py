class Solution:
    def isPalindrome(self, x: int) -> bool:
        l1=str(x)
        l2=[]
        for i in range ((len(l1)-1),-1,-1):
            l2.append(str(l1[i]))
            print(l2)
        l2String = "".join(l2)    
        comp = l2String == l1   
        print(l2String)
        return comp

sol= Solution()
print(sol.isPalindrome(x=323))

