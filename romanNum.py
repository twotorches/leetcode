class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I":1,"V":5, "X":10, "L":50,"C":100, "D":500, "M":1000}
        totalNum = 0
        for (i,letter) in enumerate(s):
            value = romanDict[letter]
            if i< len(s)-1 and value < romanDict[s[i+1]]:
                totalNum = totalNum - value 
            else:
                totalNum = totalNum + value
        return totalNum        
sol = Solution()
print(sol.romanToInt("XIV"))
{}