class Solution:
    def generateParenthesis(n: int) -> list[str]:
        currentstring = []
        mainstring = []
        def recursecall(left,right)->None:
            nonlocal currentstring
            nonlocal mainstring
            if left == 0 and right == 0:
                mainstring.append(''.join(currentstring))
            if left>0:
                currentstring.append('(')
                recursecall(left-1,right)
            if right>0 and left<right:
                currentstring.append(')')
                recursecall(left,right-1)
            if len(currentstring)>0:
                currentstring.pop()
        recursecall(n,n)
        return mainstring
n = 3 
res = Solution.generateParenthesis(n)
print(res)