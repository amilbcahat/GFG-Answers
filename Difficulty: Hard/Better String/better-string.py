#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def betterString(self, str1, str2):
        #https://www.youtube.com/watch?v=IMCk_ZniHeE
        if len(str1) > len(str2) : 
            return str1
        
        if len(str1) < len(str2) : 
            return str2
        # Code here
        def countSub(strr): 
            dp = [0] * (len(strr) + 1)
            dp[0] = 1 
            
            indexMap = {}
            
            for i in range(1, len(strr) + 1) : 
                dp[i] = 2 * dp[i - 1] 
                
                if strr[i - 1] in indexMap : 
                    dp[i] = dp[i] - dp[indexMap[strr[i - 1]]] 
                indexMap[strr[i - 1]] = i - 1
                
            return dp[len(strr)]
        
        ans1 = countSub(str1)
        ans2 = countSub(str2)
        
        if ans2 <=  ans1 : 
            return str1
        else : 
            return str2
                
            
                
        # str1 = str1.strip()
        # str2 = str2.strip()
        # res1 = []
        # res2 = []
        # def dfs(i, curStr, strr , res) : 
        #     if i >= len(strr) : 
        #         res.append(curStr) if curStr else None
        #         return 
            
        #     #include 
        #     dfs(i + 1 , curStr + strr[i], strr, res)
        #     #dont include
        #     dfs(i + 1 , curStr, strr, res)
            
        #     return 
        
        # dfs(0 , "" , str1, res1)
        # dfs(0 , "" , str2, res2)
        
        # res1 = set(res1)
        
        # res2 = set(res2)
        # if len(res1) >= len(res2) : 
        #     return str1
        # else : 
        #     return str2
         

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends