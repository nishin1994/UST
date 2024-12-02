# Write a program to create a circular queue using dictionaries in python
# Maximum length of the queue is 5:
# if it crosses the maximum length it has to delete the latest added element
# in the queue and add the new element to the queue

class CircularQueue:
    def __init__(self):
        self.dict_queue = {}
        
        self.max_len = 5
        self.len = 0
        self.head = 0
        self.tail = 0

    def add_ele(self,new_ele):
        if self.len < self.max_len:
            # Keep on adding to queue until max length
            self.dict_queue[self.len%self.max_len]=new_ele
        else:
            # Remove the latest element with the equation below
            # Here the index of latest element has been found and replaced
            self.dict_queue[self.max_len-(self.len%self.max_len)-1]=new_ele
            # shift the elements
            for i in range(0,len(self.dict_queue)-1):
                temp = self.dict_queue[i]
                self.dict_queue[i]=self.dict_queue[i+1]
                self.dict_queue[i+1]=temp 
        self.len+=1
        
        return self.dict_queue


def main():
    queue = CircularQueue()
    queue.add_ele(1)
    queue.add_ele(2)
    queue.add_ele(3)
    queue.add_ele(4)
    queue.add_ele(5)
    #queue.add_ele(6)
    #queue.add_ele(7)
    #queue.add_ele(8)
    #queue.add_ele(8)
    #queue.add_ele(8)
    x=queue.add_ele(6)
    print(x)

if __name__ == "__main__":
    main()


def test_1():
    list = [1,2,3,4,5,6]
    queue = CircularQueue()
    for i in list:
        x = queue.add_ele(1)
    
    if not len(x) == 5:
        return 1
    if x[0] != 2 or x[1] != 3 or x[2] != 4 or x[3] != 6 or x[4] != 1:
        return 1