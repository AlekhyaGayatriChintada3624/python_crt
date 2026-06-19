front=0
rear=-1
queue=[None]*5
size=0
def enqueue(value):
    if size==len(queue):
        return "queue overflow"
        rear+=1
        size+=1
        queue[rear]=value

#queue
def dequeue():
    if size==0:
        return False
    front+=1
    return True
def peek():
    return queue[front]
def isFull():
    return size==len(queue)
def isEmpty():
    return size==0