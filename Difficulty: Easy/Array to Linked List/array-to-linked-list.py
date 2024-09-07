#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        # code here
        dummy = tmp = Node(0)
        
        for i in range(len(arr)): 
            new = Node(arr[i])
            tmp.next = new 
            tmp = tmp.next 
        
        return dummy.next

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        # n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
# } Driver Code Ends