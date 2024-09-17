#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
	    mod = 10 ** 9 + 7
		# code here
		dp = {}
		def dfs(i , curSum) :
		    if i >= len(arr) and curSum == sum : 
		        return 1 
		        
		    if i >= len(arr) or curSum > sum :
		        return 0
		        
		    if (i , curSum) in dp : 
		        return dp[(i , curSum)]
		        
		    total = 0 
		    
		    total += dfs(i + 1 , curSum + arr[i]) % mod 
		    total += dfs(i + 1 , curSum) % mod 
		    
		    dp[(i , curSum)] = total % mod 
		    
		    return total % mod
		    
		return dfs(0 , 0)
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends