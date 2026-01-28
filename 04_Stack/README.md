# Stack in Data Structures (Python DSA)

## 1. What is a Stack?

A Stack is a linear data structure that follows the **LIFO principle**:  
**Last In, First Out**.

This means the element that is inserted last will be removed first.

---

## 2. Real Life Example

### Example 1: Stack of Plates 🍽️  
Plates are kept one on top of another.
- You put a plate on top (push).
- You remove the top plate first (pop).

### Example 2: Browser Back Button 🌐  
The last visited page is the first one to be closed.

---

## 3. Basic Operations in Stack

- **Push**: Add an element to the top of the stack.  
- **Pop**: Remove the top element from the stack.  
- **Peek/Top**: View the top element without removing it.  
- **IsEmpty**: Check if the stack is empty.

---

## 4. How Stack Works (Visualization)

Top
↓
| 30 |
| 20 |
| 10 |
Bottom


Push 40:

| 40 | ← Top
| 30 |
| 20 |
| 10 |

Pop (remove top):

| 30 | ← Top
| 20 |
| 10 |

---

## 5. Why Do We Use Stack?

- Function call management (Call Stack)
- Expression evaluation
- Undo/Redo operations
- Parenthesis checking
- Reversing data

---

## 6. Time Complexity (Beginner View)

| Operation | Time Complexity |
|------------|----------------|
| Push       | O(1)           |
| Pop        | O(1)           |
| Peek       | O(1)           |
| Search     | O(n)           |

---

## 7. Applications of Stack

- Undo / Redo in editors  
- Browser navigation  
- Compiler syntax checking  
- Depth First Search (DFS)  
- Backtracking problems  

---

## 8. Interview Friendly Definition

A Stack is a linear data structure that follows the Last In First Out (LIFO) principle, where insertion and deletion of elements take place only at one end called the top.