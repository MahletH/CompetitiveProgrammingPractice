class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openning,closing,result,current,open_):
            if not openning and not closing:
                result.append("".join(current))
            if openning:
                current.append(openning.pop())
                dfs(openning,closing,result,current,open_+1)
                current.pop()
                openning.append('(')
            if closing and open_:
                current.append(closing.pop())
                dfs(openning,closing,result,current,open_-1)
                current.pop()
                closing.append(')')
        result=[]
        openning=['(' for i in range(n)]
        closing=[')']*n
        dfs(openning,closing,result,[],0)
        return result