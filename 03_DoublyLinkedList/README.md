# Doubly Linked List in Data Structures (Python DSA)

## 1. What is a Doubly Linked List?

A Doubly Linked List is a linear data structure where each node contains three parts:

- Data (the value)  
- Prev (reference to the previous node)  
- Next (reference to the next node)

Nodes are stored in non-continuous memory and are connected using links.

NULL ← Node1 ⇄ Node2 ⇄ Node3 → NULL

---

## 2. Difference Between Singly and Doubly Linked List

| Singly Linked List     | Doubly Linked List             |
|------------------------|--------------------------------|
| One link (next)        | Two links (prev, next)         |
| Forward traversal only | Forward and backward traversal |
| Less memory usage      | More memory (extra pointer)    |

---

## 3. Why Do We Use Doubly Linked Lists?

Doubly Linked Lists allow:

- Two-way traversal (forward & backward)  
- Easy deletion (no need to track previous node separately)  
- Efficient navigation

---

## 4. Real Life Example

### Example 1: Browser Navigation 🌐  
- Forward button → Next page  
- Back button → Previous page  

Each page knows both:
- Which page comes next
- Which page came before

### Example 2: Train Coaches 🚆  
You can move:
- From coach 3 to coach 4 (forward)
- From coach 3 to coach 2 (backward)

---

## 5. Inserting Data at the End

### Situation

10 ⇄ 20 ⇄ 30 ⇄ NULL


Insert 40 at the end:

### Process

1. Create a new node.
2. Traverse to the last node.
3. Connect last node’s `next` to new node.
4. Connect new node’s `prev` to last node.

### Final Result

10 ⇄ 20 ⇄ 30 ⇄ 40 ⇄ NULL



---

## 6. Empty List Case

If list is empty:

Head → NULL



Insert first element (5):

NULL ← 5 → NULL



---

## 7. Time Complexity (Beginner View)

- Insertion at end: O(n)  
- Searching: O(n)  
- Deletion: O(n)  
- Traversal (forward/backward): O(n)

---

## 8. Applications of Doubly Linked List

- Browser back and forward navigation  
- Undo and Redo operations  
- Music players (previous and next song)  
- Navigation systems  
- Operating System process management  

---

## 9. Interview Friendly Definition

A Doubly Linked List is a linear dynamic data structure in which each node contains data and two references: one t