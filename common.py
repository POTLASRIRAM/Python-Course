class SLL:
    def __init__(self,val):
        self.d = val
        self.next = None
def pLL(head):
    while(head!=None):
        print(head.d)
        head=head.next

def take_ip():
    val = int(input())
    head=None
    while(val!=-1):
        nNode = SLL(val)
        if (head == None):
            head = nNode
        else:
            temp = head 
            while(temp.next!=None):
                temp = temp.next
            temp.next = nNode
        val = int(input())
    return head

newHead = take_ip()
pLL(newHead)