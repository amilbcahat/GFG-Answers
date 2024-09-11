#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        cur = head 
        prev = None 
        while cur : 
            tmp = cur.next
            cur.next = prev 
            prev = cur 
            cur = tmp
            
        head = prev 
        
        cur = head 
        carry = 1
        summ = 0 
        while cur : 
            summ = carry + cur.data 
            nodeData = summ % 10 
            carry = summ // 10 
            cur.data = nodeData
            prev = cur
            cur = cur.next
            
            
        if carry >= 1 : 
            prev.next = Node(carry)
            
            
        cur = head 
        prev = None 
        while cur : 
            tmp = cur.next
            cur.next = prev 
            prev = cur 
            cur = tmp
            
        head = prev
        return head
                
            
            
    
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        first = arr[0]
        for i in arr:
            list1.insert(i)
        n1 = list1.size
        resHead = Solution().addOne(list1.head)

        n2 = 0
        current = resHead
        while current is not None:
            current = current.next
            n2 += 1
        if n2 == 1:
            if n1 > 1:
                print("Return the modified linkedlist")
            if n1 == 1:
                if first < 9:
                    PrintList(resHead)
                    print()
                else:
                    print("Return the modified linkedlist")
        else:
            PrintList(resHead)
            print()

# } Driver Code Ends