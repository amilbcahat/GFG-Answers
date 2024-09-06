#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
    	#code here 
    	#Watch Video for logic 
    	def upperBound(arr, target) : 
    	    l , r = 0 , len(arr) - 1
    	    ans = len(arr)
    	    while l <= r : 
    	        m = (l + r) // 2 
    	        if arr[m] > target: 
    	            ans = m 
    	            r = m - 1
    	        else : 
    	            l = m + 1
    	    return ans 
    	            
    	def countSmallEqual(num) : 
    	    cnt = 0 
    	    for i in range(len(matrix)):
    	        cnt += upperBound(matrix[i] , num)
    	    return cnt
    	        
    	        
    	minElem , maxElem = float("inf") , float("-inf")
    	for i in range(len(matrix)) : 
    	    minElem = min(minElem , matrix[i][0])
    	    maxElem = max(maxElem , matrix[i][C - 1])
    	    
    	req = R * C // 2 
    	low , high = minElem , maxElem 
    	while low <= high : 
    	    mid = (low + high) // 2 
    	    smallerEqual = countSmallEqual(mid)
    	    if (smallerEqual <= req) :
    	         low = mid + 1
    	    else: 
    	         high = mid - 1
    	         
    	return low 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends