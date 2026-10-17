# libraries for graph visualization
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# stores persons in the network as objects which has a list of connections
class Node(): 
    def __init__(self, name):
        self.name = name
        self.connections = []

    # Adds persons to list of friends/connection
    def add_connection(self, person):
        if person in self.connections:
            # also returns whether persons are already connected
            return True
        else:
            self.connections.append(person) 
            return False # if not, they are connected
                         # and a different message is displayed

# class that stores persons in the network as node objects
class SocialNetwork:
    def __init__(self):
        self.list = []
        self.graph = nx.Graph() 
        # also initializes the networkx library for convenient using

    # Adds new person/s to the network
    def add_contact(self):
        while True:
            # prompts user input (repeatedly)
            names = input("Enter name/s (separate names with a comma): ")

            if names != "": # breaks the loop if a string is entered
                print() 
                break

        # input is split into separate names if a comma is detected
        persons_list = names.split(",") 

        for name in persons_list: # iterates through each name detected in the input
            name = name.strip()   # removes spaces before and after the names
            existing = False      # indicator; to signal if name already exists

            for node in self.list:# checks every name in the network's list of people
                if node.name == name: # if the name is already in the network:
                    print(f"[ E R R O R ] \n   >> The name '{name}' is already in the network.\n   >> Try using a different name.")
                    existing = True # an error message is printed, indicator = true
                    break           # and looping is stopped
            if not existing: # if indicator is still False (name is not in the network)
                person = Node(name)      # name is converted into a node object
                self.list.append(person) # node is appended to network's list of people
                self.graph.add_node(person.name) # node is also added to the graph
                print(f"['{person.name}' added to the network.]") # success message

    # Adds connection between two people
    def add_connection(self):
        while True:
            # prompts user input (repeatedly)
            person1 = input("Enter person's name: ")
            person1 = person1.strip()
            if person1 == '8686': # termination code;
                return # stops operation when entered

            person1 = self.get_node(person1) # calls the getter function
            if person1: # to determine if person exists in the network
                print()
                break   # breaks loop if person exists

        while True:
            # prompts user input (repeatedly)
            persons = input("Enter connections (comma-separated): ")
            if persons == '8686': # termination code;
                return # stops operation when entered
            elif persons != "": 
                print() 
                break # breaks the loop if a string is entered

        # input is split into separate names if a comma is detected
        persons_list = persons.split(",")

        for name in persons_list: # iterates through each name detected in the input
            name = name.strip()
            name = self.get_node_add(name) # calls getter-adder function to
                                           # determine if name exists or is to be created

            # connects the persons to each other and prints a message
            if name:
                connected = person1.add_connection(name)
                self.graph.add_edge(person1.name, name.name)
                if connected:
                    print("[ E R R O R ] \n   >> Connection already established.")
                else: 
                    connected = name.add_connection(person1)
                    print(f"[ {name.name}'s connection with {person1.name} established. ]")

    def get_node(self, name): # getter function to know if name is in the network
        found = False # indicator
        for node in self.list:
            if node.name == name: # if person is found, indicator becomes true
                found = True
                return node
        if not found: # if person is not found, returns an error message
            print(f"[ E R R O R ]\n   >> '{name}' not in network.\n   >> Add them to the network first.\n   >> Type '8686' to cancel operation.")
            return None
        
    def get_node_add(self, name): # getter and adder function
        found = False
        for node in self.list: # determines if person is in the network
            if node.name == name:
                found = True
                return node
        if not found: # if not, adds the person into the network
            person = Node(name)
            self.list.append(person)
            self.graph.add_node(person.name)
            print(f"['{person.name}' added to the network.]")
            return person  

    # Finds all friends of a person.
    def get_friends(self):
        while True:
            # prompts user input
            person = input("Enter the person's name: ").strip()
            if person != "": 
                print() 
                break

        person = self.get_node(person) # calls getter function
        if person: # if person is in the network
            friends = person.connections # gets the person's list of connections
            print(f"Friends of {person.name}:") # and prints them
            for friend in friends:
                name = friend.name
                print(f"   - {name}")

    # Finds the shortest connection path between two people using BFS
    def shortest_connection(self, person1, person2):
        if person1 not in self.graph or person2 not in self.graph:
            return f"Both {person1} and {person2} must be in the network."

        # Initialize a queue using a list
        queue = [(person1, [person1])]  # Each element is a tuple (person, path)

        visited = set()  # Set to keep track of visited nodes
        visited.add(person1)

        while queue:
            current_person, path = queue.pop(0)  # Remove the first name from the list (FIFO)

            # checks if name is the target person; if so, returns the path
            if current_person == person2:
                return path

            # Explores the neighbors
            for neighbor in self.graph[current_person]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Append the neighbor to the queue and extend the current path
                    queue.append((neighbor, path + [neighbor]))

        return f"No connection found between {person1} and {person2}."

    # Suggests friends (mutual connections).
    def suggest_friends(self, person):
        if person not in self.graph:
            return f"{person} is not in the network."

        # stores friends and visited nodes as sets to avoid repeated traversing
        visited = set()
        friends = set()
        mutual_friends = {}

        # BFS to find direct friends and mutual friends
        queue = [person]
        visited.add(person) 

        while queue:
            current_person = queue.pop(0) # FIFO traversal
            for neighbor in self.graph[current_person]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if current_person == person:
                        # Add to direct friends and explore their neighbors
                        friends.add(neighbor)
                        queue.append(neighbor)
                    elif neighbor not in friends:
                        # Count as mutual friend
                        mutual_friends[neighbor] = mutual_friends.get(neighbor, 0) + 1

        suggested = sorted(mutual_friends.items(), key=lambda x: -x[1])
        return [f"{p} ({c} mutual friends)" for p, c in suggested] # prints suggested friends
    
    def display_network(self):
        # to determine the positions of the nodes and minimize edge intersecting edges
        pos = nx.kamada_kawai_layout(self.graph)  

        fig, ax = plt.subplots(figsize=(5, 5)) # creates figure to display graph
        ax.set_title("Social Network Graph", fontsize=16, pad=20) # formatting of graph

        nx.draw_networkx_edges(self.graph, pos, ax=ax) # draws edges between nodes

        label_pos = {node: (x, y - 0.1) for node, (x, y) in pos.items()} # labels nodes
        nx.draw_networkx_labels(self.graph, label_pos, ax=ax, font_size=12, font_color="black")

        node_icon = mpimg.imread("person.png") # customizes nodes into a picture icon

        img_size = 0.07 # icon size setting

        # calculates size of the graph to optimize and allocate space between the nodes
        for node, (x, y) in pos.items(): 
            ax.imshow(node_icon, extent=(x - img_size, x + img_size, y - img_size, y + img_size), zorder=1)
        x_vals, y_vals = zip(*pos.values())
        ax.set_xlim(min(x_vals) - 0.3, max(x_vals) + 0.3)
        ax.set_ylim(min(y_vals) - 0.3, max(y_vals) + 0.3)

        ax.axis('off')
        plt.show() # displays the final graph

def main():
    print("\nSocial Network Analysis") # prints project title

    network = SocialNetwork() # initializes social network object as network
    while True: # displays options (repeatedly)
        print("\n[0] Exit")
        print("[1] Add person(s) to network")
        print("[2] Add connection(s)")
        print("[3] Find all of a person's friends")
        print("[4] Find the shortest connection path of two people")
        print("[5] Suggest friends (mutual connections)")
        print("[6] View Social Network")

        choice = input("\nChoose an option: ")

        # if-elif-else statements for chosen option; calls corresponding functions
        if choice == "1": # adds person to network
            print("\n----------------------------------------------------\n")
            network.add_contact()
            print("\n----------------------------------------------------")

        elif choice == "2": # adds connections
            print("\n----------------------------------------------------\n")
            network.add_connection()
            print("\n----------------------------------------------------")

        elif choice == "3": # displays a person's friends
            print("\n----------------------------------------------------\n")
            network.get_friends()
            print("\n----------------------------------------------------")

        elif choice == "4": # gives shortest connection path b/w 2 people
            print("\n----------------------------------------------------")
            person1 = input("Enter the first person's name: ")
            person2 = input("Enter the second person's name: ")
            path = network.shortest_connection(person1.strip(), person2.strip())
            print(f"Shortest connection path: {path}")
            print("\n----------------------------------------------------")

        elif choice == "5": # finds suggested friends for a person
            print("\n----------------------------------------------------\n")
            person = input("Enter the person's name: ").strip()  
            suggestions = network.suggest_friends(person) 
            if suggestions:
                print(f"Friend suggestion/s for {person}:")
                for suggestion in suggestions:
                    print(f"   - {suggestion}")  
            else:
                print(f"No suggestions available for {person}.")
            print("\n----------------------------------------------------")

        elif choice == "6": # displays social network graph
            network.display_network()

        elif choice == "0": # terminates program
            print("\n----------------------------------------------------\n")
            print("Exiting the program. Goodbye!")
            print("\n----------------------------------------------------")
            break

        else: # if anything other than 0-6 is inputted, prints a message and restarts the loop
            print("Invalid input. Please select from the options.")

main() # starts the program interface