#User function Template for python3
from collections import defaultdict
class Solution:
    def substrCount (self,s, k):
        # your code here
        #Solution - https://leetcode.com/problems/subarrays-with-k-different-integers/submissions/1284779076/
        def atmost(k) : 
            l = 0 
            res = 0 
            countMap = defaultdict(int)
            distinct = set()
            
            for r in range(len(s)) : 
                distinct.add(s[r])
                countMap[s[r]] += 1
                
                while l <= r and len(distinct) > k : 
                    countMap[s[l]] -= 1 
                    if countMap[s[l]] == 0 : 
                        distinct.remove(s[l])
                    l += 1 
                    
                res += (r - l + 1)
                
            return res 
        return atmost(k) - atmost(k - 1)
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends