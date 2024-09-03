#User function Template for python3

class Solution:
    def kthElement(self, k, A, B):
        if len(A) > len(B) : 
            A , B = B , A 
        
        left = k 
        n1 , n2 = len(A) , len(B)
        
        l = max(0 , k - n2)
        r = min(n1 , k)
        
        while l <= r : 
            mid1 = (l + r) // 2 
            mid2 = left - mid1 
            
            l1 , l2 , r1 , r2 = float("-inf") , float("-inf") , float("inf") , float("inf")
            
            if mid1 < n1 : 
                r1 = A[mid1]
            if mid2 < n2 : 
                r2 = B[mid2]
            if mid1 - 1 >= 0 : 
                l1 = A[mid1 - 1]
            if mid2 - 1 >= 0 : 
                l2 = B[mid2 - 1]
                
            if l1 <= r2 and l2 <= r1 : 
                return max(l1 , l2)
            elif l1 > r2 : 
                r = mid1 - 1 
            else : 
                l = mid1 + 1
        return 0
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends