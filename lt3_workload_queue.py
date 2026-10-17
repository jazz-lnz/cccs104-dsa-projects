print("QUEUE - Linked List Implementation")

class QNode: # for creating Queue node object
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue: # for creating Queue object
    def __init__(self, name):
        self.name = name
        self.head = None

    # to print queue name and contents
    def print_queue(self):
        # in case of an empty queue
        if self.head == None: 
            print(f"{self.name}: Empty")

        else: # if queue is not empty
            list = [] # holder for queue elements
            ptr = self.head
            while ptr:
                # adding elements to list
                list.append(str(ptr.data))
                ptr = ptr.next
            print(f"{self.name}: {' '.join(list)}")

    # to find total queue workload
    def qload(self):
        ptr = self.head
        load = 0
        while ptr != None:
            # adding every element value as workload
            load += int(ptr.data)
            ptr = ptr.next
        return load
    
    # to add element/node at tail
    def enqueue(self, value):
        # in case of an empty queue
        if self.head == None:
            self.head = QNode(value)

        else: # if queue not empty
            ptr = self.head
            # to find last node
            while ptr.next != None:
                ptr = ptr.next
            # adding new node after last node
            ptr.next = QNode(value)

    # delete element/node at start
    def dequeue(self):
        # in case of an empty queue
        if self.head == None:
            print("Cannot dequeque. Queue is empty.")

        else: # if queue not empty
            ptr = self.head
            self.head = ptr.next # setting new node as head

# creating our 3 queues
q1 = Queue("Queue 1")
q2 = Queue("Queue 2")
q3 = Queue("Queue 3")

# to check input & choose which queue the input will be added to
def input_enq():
    while True: 
        uinput = input("Input Value of Workload: ") # input prompt
        try:
            uinput = int(uinput) # testing if input is a valid integer
            break
        except:
            print("    INVALID INPUT \n    Please enter an integer.")

    # comparing queue workloads
    if (q1.qload() <= q2.qload()) and (q1.qload() <= q3.qload()):
        # if Queue 1 has the least workload
        q1.enqueue(uinput)
    elif (q2.qload() < q1.qload()) and (q2.qload() <= q3.qload()):
        # if Queue 2 has the least workload
        q2.enqueue(uinput)
    else: # if Queue 3 has the least workload
        q3.enqueue(uinput)

# to choose which queue to dequeue from
def choose_dq():
    # putting queues in a list for iteration 
    queues = [q1, q2, q3]

    # setting a ceiling value for queue head values
    c = float('inf')

    for q in queues:
        # finding the queue with lowest head value
        # enables dequeueing when there are empty queues 
        if q.qload() != 0 and q.head.data < c:
            c = q.head.data
            chosen_q = q # queue with lower/st head value
    if c == float('inf'):
        print("-------------------------------------")
        print("CANNOT DEQUEUE. \nAll Queues empty.")
    else:
        chosen_q.dequeue()
            
# menu/interface function
def program():
    while True:

        print("-------------------------------------")
        q1.print_queue()
        q2.print_queue() # displaying queues at every loop of menu
        q3.print_queue()
        print("-------------------------------------")

        print("[0] Exit \n[1] Enqueue Workload \n[2] Dequeue Workload")

        while True:
            choice = input("Choice: ")

            # E X I T 
            if choice == "0":
                print("Thank you!")
                print("-------------------------------------\n")
                return
            
            # E N Q U E U E
            elif choice == "1":
                print("-------------------------------------")
                input_enq()
                break

            # D E Q U E U E
            elif choice == "2":
                choose_dq()
                break

            # if user input is not 0, 1, or 2
            else: 
                print("    INVALID INPUT") 

program() # calls program function/runs the menu