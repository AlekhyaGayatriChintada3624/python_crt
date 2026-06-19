front=0
rear=-1
queue=[None]*5
size=0
def Enqueue(Value):
    if size==len(queue):
        return "queue overflow is occured"
    rear+=1
    size+=1
    queue[Value]=Value
    return Value

def dequeue():
    if size==0:
        return "queue over ridding is ocured"
    front+=1
    
    
def queue_empty():
    if size==0:
        return "queue is empty"
def queue_full():
    if size==len(queue):
        return "queue space is filled"

def peek():
    return queue[front]


print(Enqueue(10))
print(Enqueue(3))
print(Enqueue(4))
print(Enqueue(7))
print(dequeue())
print(peek())


