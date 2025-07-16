# Stack vs Heap: Memory Management & Data Structures

This document covers the differences between Stack and Heap from two perspectives:
1. **Memory Management** - How programs allocate and manage memory
2. **Data Structures** - How data is organized and accessed

---

## 🧠 Memory Management: Stack vs Heap

### Stack Memory

**Definition**: A region of memory that stores temporary variables created by functions. It follows LIFO (Last In, First Out) principle.

#### Characteristics:
- **Fast Access**: Very fast allocation and deallocation
- **Automatic Management**: Memory is automatically managed
- **Limited Size**: Typically 1-8 MB (varies by system)
- **Sequential**: Memory addresses are contiguous
- **Scope-Based**: Variables are automatically cleaned up when going out of scope

#### What's Stored:
- Local variables
- Function parameters
- Return addresses
- Function call information

#### Memory Layout:
```
High Memory Address
+------------------+
|   Function C     |  ← Stack Pointer (SP)
|   Local vars     |
+------------------+
|   Function B     |
|   Parameters     |
+------------------+
|   Function A     |
|   Return addr    |
+------------------+
Low Memory Address
```

### Heap Memory

**Definition**: A region of memory used for dynamic allocation where variables are allocated and freed in any order.

#### Characteristics:
- **Slower Access**: Slower allocation and deallocation
- **Manual Management**: Programmer controls allocation/deallocation
- **Large Size**: Limited by available system memory
- **Fragmented**: Memory addresses may not be contiguous
- **Global Access**: Can be accessed from anywhere in the program

#### What's Stored:
- Dynamically allocated objects
- Large data structures
- Objects with unknown size at compile time

#### Memory Layout:
```
Low Memory Address
+------------------+
|  Free Block      |
+------------------+
|  Allocated       |
|  Object A        |
+------------------+
|  Free Block      |
+------------------+
|  Allocated       |
|  Object B        |
+------------------+
High Memory Address
```

### Memory Comparison Table

| Aspect | Stack | Heap |
|--------|-------|------|
| **Speed** | Very Fast | Slower |
| **Size** | Limited (MB) | Large (GB) |
| **Management** | Automatic | Manual |
| **Fragmentation** | No | Yes |
| **Thread Safety** | Thread-specific | Shared |
| **Allocation** | Compile-time | Runtime |
| **Access Pattern** | LIFO | Random |
| **Memory Leaks** | No | Possible |

### Code Examples

#### Stack Allocation (C++)
```cpp
void function() {
    int x = 10;           // Stack allocated
    char arr[100];        // Stack allocated
    
    // Memory automatically freed when function ends
}
```

#### Heap Allocation (C++)
```cpp
void function() {
    int* ptr = new int(10);           // Heap allocated
    int* arr = new int[100];          // Heap allocated
    
    // Must manually free memory
    delete ptr;
    delete[] arr;
}
```

#### Python (Automatic Memory Management)
```python
def function():
    x = 10                    # Stack reference, heap object
    my_list = [1, 2, 3, 4]   # Stack reference, heap object
    
    # Python's garbage collector handles cleanup
```

---

## 📚 Data Structures: Stack vs Heap

### Stack Data Structure

**Definition**: A linear data structure that follows LIFO (Last In, First Out) principle.

#### Operations:
- **Push**: Add element to top - O(1)
- **Pop**: Remove element from top - O(1)
- **Top/Peek**: View top element - O(1)
- **IsEmpty**: Check if stack is empty - O(1)

#### Implementation:
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.items) == 0
```

#### Use Cases:
- Function call management
- Expression evaluation
- Undo operations
- Browser history
- Depth-First Search (DFS)

#### Visual Representation:
```
Push 3 →  |   |    |   |    | 3 |
Push 2 →  |   | →  | 2 | →  | 2 |
Push 1 →  |   |    | 1 |    | 1 |
          +---+    +---+    +---+
```

### Heap Data Structure

**Definition**: A complete binary tree that satisfies the heap property. Can be Max-Heap or Min-Heap.

#### Types:
- **Max-Heap**: Parent ≥ Children
- **Min-Heap**: Parent ≤ Children

#### Operations:
- **Insert**: Add element - O(log n)
- **Extract Max/Min**: Remove root - O(log n)
- **Peek**: View root element - O(1)
- **Heapify**: Convert array to heap - O(n)

#### Implementation (Min-Heap):
```python
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        heapq.heappush(self.heap, item)
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        raise IndexError("Heap is empty")
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        raise IndexError("Heap is empty")
    
    def size(self):
        return len(self.heap)
```

#### Use Cases:
- Priority queues
- Heap sort algorithm
- Finding kth largest/smallest elements
- Graph algorithms (Dijkstra's, Prim's)
- Job scheduling systems

#### Visual Representation (Min-Heap):
```
        1
       / \
      3   2
     / \ / \
    4  5 6  7
```

### Data Structure Comparison Table

| Aspect | Stack | Heap |
|--------|-------|------|
| **Access Pattern** | LIFO | Priority-based |
| **Primary Operations** | Push/Pop | Insert/Extract |
| **Time Complexity** | O(1) | O(log n) |
| **Structure** | Linear | Binary Tree |
| **Memory Layout** | Contiguous | Tree-based |
| **Use Case** | Function calls, Undo | Priority tasks |

---

## 🔄 Key Differences Summary

### Memory Management
| Stack Memory | Heap Memory |
|-------------|-------------|
| Fast allocation/deallocation | Slower allocation/deallocation |
| Automatic memory management | Manual memory management |
| Limited size | Large size |
| No fragmentation | Can be fragmented |
| LIFO access pattern | Random access pattern |
| Thread-safe (per thread) | Requires synchronization |

### Data Structures
| Stack DS | Heap DS |
|----------|---------|
| LIFO principle | Priority-based |
| Simple linear structure | Binary tree structure |
| O(1) operations | O(log n) operations |
| Fixed access pattern | Flexible priority access |
| Used for sequential processing | Used for priority processing |

---

## 🎯 When to Use What?

### Use Stack Memory When:
- Working with local variables
- Small, temporary data
- Function parameters
- Automatic cleanup is needed

### Use Heap Memory When:
- Large data structures
- Dynamic allocation
- Unknown size at compile time
- Need to persist beyond function scope

### Use Stack Data Structure When:
- Need LIFO behavior
- Function call tracking
- Expression parsing
- Undo functionality

### Use Heap Data Structure When:
- Need priority-based access
- Finding min/max efficiently
- Implementing priority queues
- Graph algorithms requiring priority

---

## 📝 Common Interview Questions

1. **What happens when stack memory is exhausted?**
   - Stack overflow error occurs

2. **What causes memory leaks?**
   - Heap memory not properly deallocated

3. **Can stack grow dynamically?**
   - No, stack size is typically fixed

4. **Which is faster: stack or heap allocation?**
   - Stack allocation is much faster

5. **How does garbage collection relate to heap?**
   - GC automatically manages heap memory in languages like Java, Python

---

## 🔗 Related Topics
- Memory management
- Garbage collection
- Priority queues
- Binary trees
- Algorithm complexity
- System programming

## 📚 Further Reading
- Computer Systems: A Programmer's Perspective
- Introduction to Algorithms (CLRS)
- Operating System Concepts
- Data Structures and Algorithm Analysis
