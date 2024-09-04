class Solution:
    def rowWithMax1s(self, arr):
        # code here
        maxOne = float("-inf")
        res = -1 
        for i in range(len(arr)) : 
            l = 0 
            r = len(arr[i]) - 1
            ans = -1
            while l <= r : 
                mid = (l + r) // 2  
                if arr[i][mid] == 1 :
                    ans = mid 
                    r = mid - 1 
                else : 
                    l = mid + 1 
                    
            if ans >= 0 : 
                if maxOne < len(arr) - ans : 
                    maxOne = len(arr) - ans 
                    res = i 
                    
        return res 
            
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    tc = int(data[idx])
    idx += 1
    results = []

    for _ in range(tc):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        ans = Solution().rowWithMax1s(arr)
        results.append(ans)

    for result in results:
        print(result)

# } Driver Code Ends