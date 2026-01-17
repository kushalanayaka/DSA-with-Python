Singly Linked List in Data Structures (Python DSA)


1. What is a Linked List?

A Linked List is a linear data structure where elements (called nodes) are stored in non-continuous memory.

Each node contains:
  -Data (the value)
  -Next (reference to the next node)

Instead of using index like arrays, linked lists use links to move from one node to another.

Real Life Example
Think of a train 🚆
Each coach is connected to the next coach.
You can’t directly jump to the 5th coach; you must pass through the 1st, 2nd, 3rd, and 4th.


Engine → Coach1 → Coach2 → Coach3 → NULL


2. What is a Singly Linked List?

In a Singly Linked List, each node points only to the next node, not the previous one.

    Head → Node1 → Node2 → Node3 → NULL

You can move forward only, not backward.

Real Life Example
A music playlist 🎵
Each song knows which song comes next, but it doesn’t know the previous one.


3. Why Do We Use Linked Lists?

Arrays have fixed size and shifting problems during insertion/deletion.


Linked Lists solve this by:
    -Dynamic memory allocation
    -Easy insertion and deletion
    -No shifting of elements

Example
Imagine students standing in a line:
    -In array: everyone must shift if one student enters in between.
    -In linked list: only the links change.


4. Inserting Data at the End (Tail Insertion)
Situation
You already have this list:

10 → 20 → 30 → NULL

Now you want to add 40 at the end.

Real World Example
A queue in a cinema hall 🎬
A new person always stands at the end of the line.
Process:
  -Start from the head.
  -Move step by step until the last node.
  -Connect the last node to the new node.

Final result:
10 → 20 → 30 → 40 → NULL



5. Empty List Case

If no node exists:
Head → NULL

Insert first element (say 5):
Head → 5 → NULL

This is like opening a new WhatsApp group and adding the first member.



6. Time Complexity (Beginner View)

Inserting at end (without tail pointer): O(n)
Because we must travel through all nodes.
Searching: O(n)
Deletion: O(n)

7. Where Linked Lists Are Used?

   -Music players (next song)
   -Image viewers (next image)
   -Browser forward navigation
   -Undo operations (using variations of linked lists)
   -Operating System memory management

8. Interview Friendly Definition

A Singly Linked List is a dynamic linear data structure where each element stores data and a reference to the next node, allowing sequential access and efficient insertions and deletions without shifting elements.