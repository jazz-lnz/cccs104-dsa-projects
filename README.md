# CCCS 104 Projects: Data Structures and Algorithms
**Individual & Collaborative Learning Portfolio (BSCS 2A)**

## Student Information
- **Name:** Jessica Mae T. Lanuzo
- **Program:** Bachelor of Science in Computer Science
- **Course:** CCCS 104 – Data Structures and Algorithms

---

## Project Overview

This repository is a collection of Python applications developed for **CCCS 104 (Data Structures and Algorithms)**. It demonstrates the implementation and practical application of foundational **linear data structures** (Singly Linked Lists, Stacks, and Queues) and **non-linear data structures** (Graphs and Breadth-First Search algorithms) through interactive command-line interfaces (CLIs) and network visualizations.

---

## Methodology

Each learning task and final project was implemented in Python with a focus on algorithmic logic, pointer manipulation, and resilient user input handling:

1. **Custom Abstract Data Type (ADT) Implementation:** Built node-and-pointer structures from scratch (`Node` and `LL` for Singly Linked Lists; `QNode` and `Queue` for Linked-List Queues; `new_stack` for array-backed LIFO Stacks) to explicitly manage memory references (`head`, `next`, and traversal pointers) rather than relying on high-level built-in methods.
2. **Algorithmic Problem Solving:**
   - **Pointer Traversal:** Used single and dual tracking pointers (`ptr`, `p1`, `p2`, `tail`) for $O(1)$ head operations and $O(n)$ positional insertions, deletions, and value searches.
   - **Stack Height Equalization (LIFO):** Applied non-destructive state comparison using a temporary holder stack (`holder2`) while iteratively popping top elements (`pop_height()`) to determine the maximum equal height across three integer stacks.
   - **Queue Load Balancing (FIFO):** Implemented dynamic workload routing that calculates cumulative queue loads (`qload()`) before enqueuing at the tail, paired with priority-like head comparison (`float('inf')` ceiling) when dequeuing.
   - **Graph Traversal & Social Network Analysis (BFS):** Combined custom adjacency lists (`self.connections`) with `networkx.Graph()`, using Breadth-First Search (BFS) queues and `set()` tracking to compute shortest connection paths and rank mutual-friend recommendations via lambda sorting.
3. **Defensive Input Validation:** Guarded CLI prompts using `while True` loops paired with `try-except` (`int()`) blocks for signed integer validation and `.isdigit()` checks for non-negative index positions.

---

## Results & Key Outcomes

- **4 Complete DSA Modules:** Delivered working, menu-driven Python applications covering Singly Linked Lists (`lt1_singly_linked_list.py`), LIFO Stacks (`lt2_equal_stacks.py`), FIFO Linked-List Queues (`lt3_workload_queue.py`), and Undirected Social Network Graphs (`finals_social_network_graph.py`).
- **Edge-Case Resilience:** Handled empty-structure operations, out-of-bounds indices, duplicate graph nodes/edges, non-integer inputs, and operation cancellation codes (`8686`) without runtime crashes.
- **Visual Graph Rendering:** Integrated `networkx` (Kamada-Kawai layout) and `matplotlib` to render custom avatar-based social network graphs (`person.png`) that minimize intersecting edges.

---

## Repository Structure

```text
cccs104-dsa-projects/
├── lt1_singly_linked_list.py       # Learning Task 1: Singly Linked List CLI
├── lt2_equal_stacks.py             # Learning Task 2: Equal Stacks Height Finder (LIFO)
├── lt3_workload_queue.py           # Learning Task 3: Workload-Balancing Multi-Queue (FIFO)
├── finals_social_network_graph.py  # Final Project: Social Network Analysis & BFS Graph Visualizer
├── person.png                      # Custom node avatar icon used by finals_social_network_graph.py
└── README.md                       # Portfolio documentation
```

---

## Module Guide

### 1. Singly Linked List CLI (`lt1_singly_linked_list.py`)
A menu-driven program implementing a custom Singly Linked List (`Node` and `LL` classes) with 10 sequential operations and comprehensive boundary checks.

- **Role:** Lead Developer & Documentation
- **Supported Operations:**
  - `[1] Insert At Start` (`ins_start`): Inserts an integer node at the list head.
  - `[2] Insert At End` (`ins_end`): Traverses to the tail node and appends a new integer node.
  - `[3] Insert At Position` (`ins_pos`): Inserts a node at a `0`-based index position if preceding nodes exist.
  - `[4] Delete At Start` (`del_start`): Unlinks the head node and promotes `head.next`.
  - `[5] Delete At End` (`del_end`): Unlinks the tail node using a penultimate pointer.
  - `[6] Delete At Position` (`del_pos`): Unlinks the node at a specified `0`-based index.
  - `[7] Delete Number` (`del_num`): Searches for and deletes the first node matching a target integer.
  - `[8] Search Number` (`search_num`): Outputs the `0`-based index of a target integer if present.
  - `[9] Display Number At Position` (`dis_num`): Prints the integer stored at a given `0`-based index.
  - `[10] Display List` (`display_list`): Traverses and prints all elements from head to tail.
  - `[0] Exit`: Prompts for `[0] Yes / [1] No` confirmation before closing.

---

### 2. Equal Stacks Height Finder (`lt2_equal_stacks.py`)
An individual project implementing the Last-In, First-Out (LIFO) **Stack** data structure (`new_stack` class) to determine whether three stacks of integers can reach an equal cumulative height by popping elements from the top.

- **Role:** Sole Developer & Documentation
- **How It Works:**
  1. Prompts the user to input space-separated integers (positive, negative, or zero) for `Stack 1`, `Stack 2`, and `Stack 3` (first integer entered is placed at the bottom of the stack; last integer is at the top).
  2. Calculates and displays the initial total height (sum of elements) for each stack (`display_height()`).
  3. Iteratively compares stack heights using a temporary `holder2` stack and `pop_height()` to remove top elements until all three stacks match in height or exhaust their elements.
  4. Displays the matching height and prints each stack's remaining elements ordered from **top to bottom** (`display2()`), or outputs `"Stack heights will never be equal."`
- **Sample Run:**
  ```text
  Enter elements of Stack 1: 1 1 1 2 3
  Enter elements of Stack 2: 2 3 4
  Enter elements of Stack 3: 1 4 1 1
  ----------------------------------------------
  Stack 1 total height: 8
  Stack 2 total height: 9
  Stack 3 total height: 7
  ----------------------------------------------
  All stacks are equal at Height: 5
  Stack 1: 2 1 1 1
  Stack 2: 3 2
  Stack 3: 4 1
  ```

---

### 3. Workload-Balancing Multi-Queue (`lt3_workload_queue.py`)
A First-In, First-Out (FIFO) **Queue** implementation built with a Singly Linked List (`QNode` and `Queue` classes) that manages and balances integer workloads across three parallel queues (`Queue 1`, `Queue 2`, and `Queue 3`).

- **How It Works:**
  - **Real-Time Queue Monitor:** Displays the current elements of `Queue 1`, `Queue 2`, and `Queue 3` (`Empty` or space-separated values) at the start of every menu cycle (`print_queue()`).
  - `[1] Enqueue Workload` (`input_enq()`): Prompts for an integer workload, calculates the sum of active workloads in each queue (`qload()`), and automatically appends (`enqueue()`) the new node to the tail of whichever queue currently has the **lowest total workload**.
  - `[2] Dequeue Workload` (`choose_dq()`): Evaluates all non-empty queues, compares the integer values at their heads (`q.head.data`), and removes (`dequeue()`) the front node from the queue with the **smallest head workload value**.
  - `[0] Exit`: Terminates the program loop.

---

### 4. Social Network Analysis Graph (`finals_social_network_graph.py`)
Developed around the narrative *"The Reunion Network"* (mapping alumni connections to reunite missing classmates, with real-world applications in post-disaster missing-person location), this application models social relationships as an undirected **Graph** using custom adjacency lists and `networkx`.

- **Role:** Core Developer (Code, Code Demo, Documentation)
- **Core Features & Menu Options:**
  - `[1] Add person(s) to network` (`add_contact`): Accepts single or comma-separated names, prevents duplicates, and creates `Node` objects and `networkx` graph vertices.
  - `[2] Add connection(s)` (`add_connection`): Establishes bidirectional edges between an existing person and comma-separated contacts (automatically adding new contacts if they do not yet exist, or canceling if `8686` is typed).
  - `[3] Find all of a person's friends` (`get_friends`): Lists all direct adjacency connections for a specified person.
  - `[4] Find the shortest connection path of two people` (`shortest_connection`): Uses **Breadth-First Search (BFS)** with a FIFO queue and `visited` set to return the shortest chain of acquaintances linking two individuals (e.g., `['Ann', 'Jess', 'Mae']`).
  - `[5] Suggest friends (mutual connections)` (`suggest_friends`): Traverses friends-of-friends via BFS, counts shared connections, and sorts recommendations in descending order of mutual friends.
  - `[6] View Social Network` (`display_network`): Renders a visual graph using the **Kamada-Kawai layout** (`nx.kamada_kawai_layout`) to minimize edge crossings, displaying custom node icons (`person.png`) and labeled edges in Matplotlib.

---

## Developer Takeaways & Reflections

- **Translating Visualizations to Code (LT1 & LT2):** Converting visual diagrams of node insertion, pointer relinking, and stack popping into code highlighted the importance of mapping out all edge cases and user input variations before writing the implementation.
- **Targeted Exception Handling (LT1):** Combining `try-except` (`int()`) for general integer validation with `if-else` (`.isdigit()`) for non-negative index validation inside `while` loops keeps console programs resilient against invalid inputs.
- **Workload Balancing & Multi-Queue Coordination (LT3):** Designing the `qload()` method to compare cumulative queue weights before enqueueing tasks illustrated how FIFO structures can be adapted for load balancing, while using `float('inf')` for empty-queue checks ensured robust priority-based dequeueing across parallel queues.
- **Practical Graph Applications (Finals):** Applying searching algorithms (BFS), sets, and sorting to build a working social network analyzer and visualizing it with `networkx` and `matplotlib` demonstrated how classroom data structures solve real-world connectivity problems.

---

## How to Run

### Prerequisites
1. **Python 3.8+** installed.
2. For `finals_social_network_graph.py`, install `networkx` and `matplotlib` and ensure `person.png` is in the same directory as the script:
   ```bash
   pip install networkx matplotlib
   ```

### Running the Programs
```bash
# Run Learning Task 1: Singly Linked List
python lt1_singly_linked_list.py

# Run Learning Task 2: Stack Equal Height Finder
python lt2_equal_stacks.py

# Run Learning Task 3: Workload-Balancing Multi-Queue
python lt3_workload_queue.py

# Run Finals: Social Network Analysis & Graph Visualizer
python finals_social_network_graph.py
```
