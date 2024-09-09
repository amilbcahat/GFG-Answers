class Solution:
    def delete_node(self, head, x):
        #code here
        
        dummy = Node(-1)
        dummy.next = head 
        head.prev = dummy
        
        cur = head 
        p = 1 
        
        while cur : 
            tmp = cur.next
            if p == x : 
                prev , nxt = cur.prev , cur.next 
                if prev : 
                    prev.next = nxt 
                
                if nxt : 
                    nxt.prev = prev 
                
            cur = tmp
            p += 1
        return dummy.next

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = Node(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def printList(head):
    if not head:
        return

    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.delete_node(head, int(input().strip()))
        printList(resHead)

# } Driver Code Ends