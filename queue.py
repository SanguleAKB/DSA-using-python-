class Queue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    def enqueue(self,data):
        self.queue.append(data)
        print(f"Enqueued : {data}")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is underflow..")
        else:
            ele_pop = self.queue.pop(0)
            print("Poped element :",ele_pop)

    def front(self):
        print("Front element : ",self.queue[-1])

    def rear(self):
        print("Rear element : ",self.queue[0])

    def size(self):
        print("Length of queue : ",len(self.queue))

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.size()
queue.rear()
queue.front()
queue.dequeue()
queue.dequeue()