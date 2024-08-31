#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
    #Your code here
        l = 1 
        r = n 
        ans = 0
        while l <= r : 
            mid = (l + r) // 2
            if mid * mid > n : 
                r = mid - 1 
            else : 
                ans = mid  
                l = mid + 1
                
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends