print("\nDSA - LINEAR DATA STRUCTURE (Stack)  \n(LEARNING TASK 2 by JMLanuzo)\n")

# POP METHOD : https://www.w3schools.com/python/ref_list_pop.asp
 
class new_stack(): # creation of stack object
    def __init__(self, name):
        self.name = name
        self.stack = [] # element container, empty @creation of new stack
        self.height = self.find_height()

    # to add stack elements
    def push(self, userinput = None):

        # to add stack elements thru user input
        if userinput == None:
            while True:
                userinput = input(f'Enter elements of {self.name}: ')
                if userinput == "": 
                    print("***\nTHE STACK CANNOT BE EMPTY. \nPlease enter integers separated by spaces.\n***")
                else:
                    #  to check if user input is valid (integers separated with spaces)
                    self.list = userinput.split()
                    try:
                        for item in self.list:
                            int(item)
                            self.stack.append(item) # adding input into the stack
                            # from first number entered/typed to last
                        return
                    except:
                            self.stack = []
                            print("***\nINVALID INPUT. \nPlease enter integers separated by spaces.\n***")

        # to add stack elements from another stack/list
        else:
            for item in userinput:
                self.stack.append(item)

    # to display stack elements from bottom to top
    def display(self): 
        print(f'{self.name}: ' + ' '.join(self.stack))

    # to display stack elements from top to bottom
    def display2(self): 
        print(f'{self.name}: ' + ' '.join(self.stack[::-1]))

    # to find stack height
    def find_height(self):
        self.height = 0
        for item in self.stack:
            self.height += int(item)

    # to find AND display stack height
    def display_height(self):
        self.height = 0
        for item in self.stack:
            self.height = self.height + int(item)
        print(f'{self.name} total height: {self.height}')

    # to pop (top) element of stack
    def pop(self):
        self.stack.pop()

    # to pop element AND find the new stack height
    def pop_height(self):
        self.pop()
        self.find_height()    


def program(): 
    while True:
        
        # initialize Stacks 1, 2, 3
        # creates new stacks per loop of program
        stack1 = new_stack("Stack 1") 
        stack2 = new_stack("Stack 2") 
        stack3 = new_stack("Stack 3")

        stack1.push() # prompts user input
        stack2.push()
        stack3.push()

        print('----------------------------------------------')

        stack1.display_height() # displays the stacks' heights
        stack2.display_height()
        stack3.display_height()

        print('----------------------------------------------')

        # comparing stack heights and finding equal height
        while stack1.height != 0:

            # creation of holder to preserve stack elements
            holder2 = new_stack("Stack 2")
            holder2.push(stack2.stack) # pushing Stack 2 elements to holder

            # comparing Stack 1 height to Stack 2 heights*
            # heights*: initial height and heights after popping elements
            while stack1.height != holder2.height and holder2.height != 0:
                holder2.pop_height()

            # if no Stack 2 height matches with current Stack 1 height
            if holder2.height == 0: 
                stack1.pop_height() # reduces Stack 1 elements (& height)
                # comparison of Stack 1 height and Stack 2 heights* repeats after this

            # if Stack 1 height matches with Stack 2's
            else: 
                
                # comparing matched heights of Stack 1 & 2 to Stack 3 heights*
                while stack1.height != stack3.height and stack3.height != 0:
                    stack3.pop_height()

                # if no Stack 3 height matches with current Stack 1 & 2 heights
                if stack3.height == 0:
                    print('Stack heights will never be equal.')
                    break
                
                # if a Stack 3 height matches (3 Stacks have matching heights)
                else:
                    print(f'All stacks are equal at Height: {stack1.height}')
                    
                    # to display the elements of the stacks in equal heights
                    stack1.display2() 
                    holder2.display2()
                    stack3.display2()
                    break

        # if Stack 1 has no more elements to pop
        # (none of its heights* matches with Stack 2)
        # comparison of heights cannot continue
        if stack1.height == 0:
            print('Stack heights will never be equal.')
        
        print('----------------------------------------------')

        # option to loop/continue program
        while True:
            cont = input("Continue? (Y or N) ")
            if cont.upper() == 'Y': 
                print('----------------------------------------------')
                break
            elif cont.upper() == 'N':
                print("Thank you!\n")
                return
            # '.upper()' allows lowercase y and n input

            # if user inputs anything other than y or n
            else:
                print('***\nINVALID INPUT. \nPlease enter "Y" or "N".\n***')

program() # calls program function (runs interface/menu)
            
