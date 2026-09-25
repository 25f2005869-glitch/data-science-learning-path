/*
============================================================
             DATA STRUCTURES & ALGORITHMS
                     JAVASCRIPT
============================================================

Author      : Saloni Tiwari
Programme   : IIT Madras BS Degree — Diploma Level

============================================================
Topics Covered
============================================================
01. DSA Basics
02. Arrays
03. Strings
04. Searching
05. Sorting
06. Recursion
07. Linked List
08. Doubly Linked List
09. Circular Linked List
10. Stack
11. Queue
12. Hashing
13. Binary Tree
14. Binary Search Tree
15. Heap
16. Graph
17. BFS
18. DFS
19. Dijkstra Algorithm
20. Prim's Algorithm
21. Kruskal's Algorithm
22. Greedy Algorithms
23. Divide and Conquer
24. Backtracking
25. Dynamic Programming
26. Trie
27. Disjoint Set Union
28. Bit Manipulation
29. Mathematical Algorithms

============================================================
Author: Saloni Tiwari
IIT Madras BS Degree — Diploma Level
============================================================
*/


/* ============================================================
   1. ARRAYS
   ============================================================ */

function printArray(arr) {
    console.log(arr.join(" "));
}

function reverseArray(arr) {

    let left = 0;
    let right = arr.length - 1;

    while (left < right) {

        [arr[left], arr[right]] =
            [arr[right], arr[left]];

        left++;
        right--;
    }

    return arr;
}

function maximumElement(arr) {

    let maximum = arr[0];

    for (const value of arr) {
        maximum = Math.max(maximum, value);
    }

    return maximum;
}

function minimumElement(arr) {

    let minimum = arr[0];

    for (const value of arr) {
        minimum = Math.min(minimum, value);
    }

    return minimum;
}


/* ============================================================
   2. STRINGS
   ============================================================ */

function reverseString(str) {
    return str.split("").reverse().join("");
}

function isPalindrome(str) {

    return str === reverseString(str);
}


/* ============================================================
   3. LINEAR SEARCH
   ============================================================ */

function linearSearch(arr, key) {

    for (let i = 0; i < arr.length; i++) {

        if (arr[i] === key) {
            return i;
        }
    }

    return -1;
}


/* ============================================================
   4. BINARY SEARCH
   ============================================================ */

function binarySearch(arr, key) {

    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {

        const mid =
            Math.floor(
                left + (right - left) / 2
            );

        if (arr[mid] === key) {
            return mid;
        }

        if (arr[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}


/* ============================================================
   5. BUBBLE SORT
   ============================================================ */

function bubbleSort(arr) {

    const result = [...arr];

    for (let i = 0;
         i < result.length - 1;
         i++) {

        let swapped = false;

        for (let j = 0;
             j < result.length - i - 1;
             j++) {

            if (result[j] > result[j + 1]) {

                [result[j], result[j + 1]] =
                    [result[j + 1], result[j]];

                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
    }

    return result;
}


/* ============================================================
   6. SELECTION SORT
   ============================================================ */

function selectionSort(arr) {

    const result = [...arr];

    for (let i = 0;
         i < result.length - 1;
         i++) {

        let minimumIndex = i;

        for (let j = i + 1;
             j < result.length;
             j++) {

            if (
                result[j] <
                result[minimumIndex]
            ) {
                minimumIndex = j;
            }
        }

        [
            result[i],
            result[minimumIndex]
        ] = [
            result[minimumIndex],
            result[i]
        ];
    }

    return result;
}


/* ============================================================
   7. INSERTION SORT
   ============================================================ */

function insertionSort(arr) {

    const result = [...arr];

    for (let i = 1;
         i < result.length;
         i++) {

        const key = result[i];

        let j = i - 1;

        while (
            j >= 0 &&
            result[j] > key
        ) {

            result[j + 1] =
                result[j];

            j--;
        }

        result[j + 1] = key;
    }

    return result;
}


/* ============================================================
   8. MERGE SORT
   ============================================================ */

function merge(left, right) {

    const result = [];

    let i = 0;
    let j = 0;

    while (
        i < left.length &&
        j < right.length
    ) {

        if (left[i] <= right[j]) {
            result.push(left[i]);
            i++;
        } else {
            result.push(right[j]);
            j++;
        }
    }

    while (i < left.length) {
        result.push(left[i]);
        i++;
    }

    while (j < right.length) {
        result.push(right[j]);
        j++;
    }

    return result;
}

function mergeSort(arr) {

    if (arr.length <= 1) {
        return arr;
    }

    const mid =
        Math.floor(arr.length / 2);

    const left =
        mergeSort(arr.slice(0, mid));

    const right =
        mergeSort(arr.slice(mid));

    return merge(left, right);
}


/* ============================================================
   9. QUICK SORT
   ============================================================ */

function quickSort(arr) {

    if (arr.length <= 1) {
        return arr;
    }

    const pivot =
        arr[arr.length - 1];

    const left = [];
    const right = [];

    for (
        let i = 0;
        i < arr.length - 1;
        i++
    ) {

        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    return [
        ...quickSort(left),
        pivot,
        ...quickSort(right)
    ];
}


/* ============================================================
   10. RECURSION
   ============================================================ */

function factorial(n) {

    if (n <= 1) {
        return 1;
    }

    return n * factorial(n - 1);
}

function fibonacci(n) {

    if (n <= 1) {
        return n;
    }

    return (
        fibonacci(n - 1) +
        fibonacci(n - 2)
    );
}


/* ============================================================
   11. SINGLY LINKED LIST
   ============================================================ */

class Node {

    constructor(data) {

        this.data = data;
        this.next = null;
    }
}

class LinkedList {

    constructor() {

        this.head = null;
    }

    insertAtBeginning(data) {

        const newNode =
            new Node(data);

        newNode.next =
            this.head;

        this.head = newNode;
    }

    insertAtEnd(data) {

        const newNode =
            new Node(data);

        if (this.head === null) {

            this.head = newNode;

            return;
        }

        let current =
            this.head;

        while (current.next !== null) {
            current = current.next;
        }

        current.next = newNode;
    }

    deleteFirst() {

        if (this.head !== null) {
            this.head =
                this.head.next;
        }
    }

    display() {

        const values = [];

        let current =
            this.head;

        while (current !== null) {

            values.push(
                current.data
            );

            current =
                current.next;
        }

        console.log(
            values.join(" -> ")
            + " -> NULL"
        );
    }
}


/* ============================================================
   12. DOUBLY LINKED LIST
   ============================================================ */

class DoublyNode {

    constructor(data) {

        this.data = data;

        this.previous = null;

        this.next = null;
    }
}

class DoublyLinkedList {

    constructor() {

        this.head = null;
    }

    insertAtEnd(data) {

        const newNode =
            new DoublyNode(data);

        if (this.head === null) {

            this.head = newNode;

            return;
        }

        let current =
            this.head;

        while (current.next !== null) {
            current = current.next;
        }

        current.next = newNode;

        newNode.previous =
            current;
    }

    display() {

        const values = [];

        let current =
            this.head;

        while (current !== null) {

            values.push(
                current.data
            );

            current =
                current.next;
        }

        console.log(
            values.join(" <-> ")
            + " <-> NULL"
        );
    }
}


/* ============================================================
   13. STACK
   ============================================================ */

class Stack {

    constructor() {

        this.items = [];
    }

    push(value) {

        this.items.push(value);
    }

    pop() {

        return this.items.pop();
    }

    top() {

        if (this.items.length === 0) {
            return null;
        }

        return this.items[
            this.items.length - 1
        ];
    }

    isEmpty() {

        return this.items.length === 0;
    }

    size() {

        return this.items.length;
    }
}


/* ============================================================
   14. QUEUE
   ============================================================ */

class Queue {

    constructor() {

        this.items = [];
        this.frontIndex = 0;
    }

    enqueue(value) {

        this.items.push(value);
    }

    dequeue() {

        if (this.isEmpty()) {
            return null;
        }

        const value =
            this.items[
                this.frontIndex
            ];

        this.frontIndex++;

        return value;
    }

    front() {

        if (this.isEmpty()) {
            return null;
        }

        return this.items[
            this.frontIndex
        ];
    }

    isEmpty() {

        return (
            this.frontIndex >=
            this.items.length
        );
    }
}


/* ============================================================
   15. HASHING
   ============================================================ */

function hashingExample() {

    const students =
        new Map();

    students.set(
        101,
        "Saloni"
    );

    students.set(
        102,
        "Student"
    );

    for (
        const [id, name]
        of students
    ) {

        console.log(
            id + " : " + name
        );
    }
}


/* ============================================================
   16. BINARY TREE
   ============================================================ */

class TreeNode {

    constructor(data) {

        this.data = data;

        this.left = null;

        this.right = null;
    }
}

function inorder(root) {

    if (root === null) {
        return;
    }

    inorder(root.left);

    console.log(root.data);

    inorder(root.right);
}

function preorder(root) {

    if (root === null) {
        return;
    }

    console.log(root.data);

    preorder(root.left);

    preorder(root.right);
}

function postorder(root) {

    if (root === null) {
        return;
    }

    postorder(root.left);

    postorder(root.right);

    console.log(root.data);
}


/* ============================================================
   17. BINARY SEARCH TREE
   ============================================================ */

function insertBST(root, value) {

    if (root === null) {
        return new TreeNode(value);
    }

    if (value < root.data) {

        root.left =
            insertBST(
                root.left,
                value
            );

    } else if (value > root.data) {

        root.right =
            insertBST(
                root.right,
                value
            );
    }

    return root;
}

function searchBST(root, key) {

    if (root === null) {
        return false;
    }

    if (root.data === key) {
        return true;
    }

    if (key < root.data) {

        return searchBST(
            root.left,
            key
        );
    }

    return searchBST(
        root.right,
        key
    );
}


/* ============================================================
   18. MIN HEAP
   ============================================================ */

class MinHeap {

    constructor() {

        this.heap = [];
    }

    parent(index) {

        return Math.floor(
            (index - 1) / 2
        );
    }

    leftChild(index) {

        return 2 * index + 1;
    }

    rightChild(index) {

        return 2 * index + 2;
    }

    insert(value) {

        this.heap.push(value);

        let index =
            this.heap.length - 1;

        while (
            index > 0 &&
            this.heap[
                this.parent(index)
            ] > this.heap[index]
        ) {

            const parentIndex =
                this.parent(index);

            [
                this.heap[parentIndex],
                this.heap[index]
            ] = [
                this.heap[index],
                this.heap[parentIndex]
            ];

            index = parentIndex;
        }
    }

    extractMin() {

        if (this.heap.length === 0) {
            return null;
        }

        if (this.heap.length === 1) {
            return this.heap.pop();
        }

        const minimum =
            this.heap[0];

        this.heap[0] =
            this.heap.pop();

        let index = 0;

        while (true) {

            let smallest = index;

            const left =
                this.leftChild(index);

            const right =
                this.rightChild(index);

            if (
                left < this.heap.length &&
                this.heap[left] <
                this.heap[smallest]
            ) {

                smallest = left;
            }

            if (
                right < this.heap.length &&
                this.heap[right] <
                this.heap[smallest]
            ) {

                smallest = right;
            }

            if (smallest === index) {
                break;
            }

            [
                this.heap[index],
                this.heap[smallest]
            ] = [
                this.heap[smallest],
                this.heap[index]
            ];

            index = smallest;
        }

        return minimum;
    }
}


/* ============================================================
   19. GRAPH - BFS
   ============================================================ */

function BFS(graph, start) {

    const visited =
        new Array(graph.length)
            .fill(false);

    const queue = [];

    let front = 0;

    visited[start] = true;

    queue.push(start);

    while (front < queue.length) {

        const current =
            queue[front++];

        console.log(current);

        for (
            const neighbour
            of graph[current]
        ) {

            if (!visited[neighbour]) {

                visited[neighbour] = true;

                queue.push(neighbour);
            }
        }
    }
}


/* ============================================================
   20. GRAPH - DFS
   ============================================================ */

function DFS(
    graph,
    current,
    visited
) {

    visited[current] = true;

    console.log(current);

    for (
        const neighbour
        of graph[current]
    ) {

        if (!visited[neighbour]) {

            DFS(
                graph,
                neighbour,
                visited
            );
        }
    }
}


/* ============================================================
   21. DIJKSTRA ALGORITHM
   ============================================================ */

function dijkstra(graph, source) {

    const n =
        graph.length;

    const distance =
        new Array(n)
            .fill(Infinity);

    const visited =
        new Array(n)
            .fill(false);

    distance[source] = 0;

    for (
        let count = 0;
        count < n;
        count++
    ) {

        let current = -1;

        for (
            let i = 0;
            i < n;
            i++
        ) {

            if (
                !visited[i] &&
                (current === -1 ||
                distance[i] <
                distance[current])
            ) {

                current = i;
            }
        }

        if (current === -1) {
            break;
        }

        visited[current] = true;

        for (
            const edge
            of graph[current]
        ) {

            const next =
                edge.node;

            const newDistance =
                distance[current]
                + edge.weight;

            if (
                newDistance <
                distance[next]
            ) {

                distance[next] =
                    newDistance;
            }
        }
    }

    return distance;
}


/* ============================================================
   22. GREEDY - ACTIVITY SELECTION
   ============================================================ */

function activitySelection(
    activities
) {

    activities.sort(
        (a, b) =>
            a.finish - b.finish
    );

    const selected = [];

    let lastFinish = -1;

    for (
        const activity
        of activities
    ) {

        if (
            activity.start >=
            lastFinish
        ) {

            selected.push(
                activity
            );

            lastFinish =
                activity.finish;
        }
    }

    return selected;
}


/* ============================================================
   23. BACKTRACKING - N QUEENS
   ============================================================ */

function isSafeQueen(
    board,
    row,
    col,
    n
) {

    for (
        let i = 0;
        i < row;
        i++
    ) {

        if (board[i][col] === 1) {
            return false;
        }
    }

    for (
        let i = row - 1,
        j = col - 1;
        i >= 0 && j >= 0;
        i--, j--
    ) {

        if (board[i][j] === 1) {
            return false;
        }
    }

    for (
        let i = row - 1,
        j = col + 1;
        i >= 0 && j < n;
        i--, j++
    ) {

        if (board[i][j] === 1) {
            return false;
        }
    }

    return true;
}

function solveNQueens(
    board,
    row,
    n
) {

    if (row === n) {
        return true;
    }

    for (
        let col = 0;
        col < n;
        col++
    ) {

        if (
            isSafeQueen(
                board,
                row,
                col,
                n
            )
        ) {

            board[row][col] = 1;

            if (
                solveNQueens(
                    board,
                    row + 1,
                    n
                )
            ) {

                return true;
            }

            board[row][col] = 0;
        }
    }

    return false;
}


/* ============================================================
   24. DYNAMIC PROGRAMMING - FIBONACCI
   ============================================================ */

function dpFibonacci(n) {

    if (n <= 1) {
        return n;
    }

    const dp =
        new Array(n + 1)
            .fill(0);

    dp[0] = 0;
    dp[1] = 1;

    for (
        let i = 2;
        i <= n;
        i++
    ) {

        dp[i] =
            dp[i - 1] +
            dp[i - 2];
    }

    return dp[n];
}


/* ============================================================
   25. 0/1 KNAPSACK
   ============================================================ */

function knapsack(
    capacity,
    weights,
    values
) {

    const n =
        weights.length;

    const dp =
        Array.from(
            { length: n + 1 },
            () =>
                new Array(
                    capacity + 1
                ).fill(0)
        );

    for (
        let i = 1;
        i <= n;
        i++
    ) {

        for (
            let weight = 1;
            weight <= capacity;
            weight++
        ) {

            if (
                weights[i - 1]
                <= weight
            ) {

                dp[i][weight] =
                    Math.max(

                        values[i - 1] +
                        dp[
                            i - 1
                        ][
                            weight -
                            weights[i - 1]
                        ],

                        dp[i - 1][weight]
                    );

            } else {

                dp[i][weight] =
                    dp[i - 1][weight];
            }
        }
    }

    return dp[n][capacity];
}


/* ============================================================
   26. LONGEST COMMON SUBSEQUENCE
   ============================================================ */

function LCS(X, Y) {

    const m = X.length;
    const n = Y.length;

    const dp =
        Array.from(
            { length: m + 1 },
            () =>
                new Array(
                    n + 1
                ).fill(0)
        );

    for (
        let i = 1;
        i <= m;
        i++
    ) {

        for (
            let j = 1;
            j <= n;
            j++
        ) {

            if (
                X[i - 1] ===
                Y[j - 1]
            ) {

                dp[i][j] =
                    dp[i - 1][j - 1]
                    + 1;

            } else {

                dp[i][j] =
                    Math.max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    );
            }
        }
    }

    return dp[m][n];
}


/* ============================================================
   27. TRIE
   ============================================================ */

class TrieNode {

    constructor() {

        this.children =
            new Array(26)
                .fill(null);

        this.isEnd = false;
    }
}

class Trie {

    constructor() {

        this.root =
            new TrieNode();
    }

    insert(word) {

        let current =
            this.root;

        for (
            const character
            of word
        ) {

            const index =
                character.charCodeAt(0)
                - 97;

            if (
                current.children[index]
                === null
            ) {

                current.children[index] =
                    new TrieNode();
            }

            current =
                current.children[index];
        }

        current.isEnd = true;
    }

    search(word) {

        let current =
            this.root;

        for (
            const character
            of word
        ) {

            const index =
                character.charCodeAt(0)
                - 97;

            if (
                current.children[index]
                === null
            ) {

                return false;
            }

            current =
                current.children[index];
        }

        return current.isEnd;
    }
}


/* ============================================================
   28. DISJOINT SET UNION
   ============================================================ */

class DSU {

    constructor(n) {

        this.parent =
            new Array(n);

        this.rank =
            new Array(n)
                .fill(0);

        for (
            let i = 0;
            i < n;
            i++
        ) {

            this.parent[i] = i;
        }
    }

    find(x) {

        if (
            this.parent[x] !== x
        ) {

            this.parent[x] =
                this.find(
                    this.parent[x]
                );
        }

        return this.parent[x];
    }

    union(a, b) {

        a = this.find(a);

        b = this.find(b);

        if (a === b) {
            return;
        }

        if (
            this.rank[a] <
            this.rank[b]
        ) {

            this.parent[a] = b;

        } else if (
            this.rank[a] >
            this.rank[b]
        ) {

            this.parent[b] = a;

        } else {

            this.parent[b] = a;

            this.rank[a]++;
        }
    }
}


/* ============================================================
   29. BIT MANIPULATION
   ============================================================ */

function isPowerOfTwo(n) {

    if (n <= 0) {
        return false;
    }

    return (
        (n & (n - 1)) === 0
    );
}

function countSetBits(n) {

    let count = 0;

    while (n !== 0) {

        n =
            n & (n - 1);

        count++;
    }

    return count;
}


/* ============================================================
   30. MATHEMATICAL ALGORITHMS
   ============================================================ */

function gcd(a, b) {

    while (b !== 0) {

        const temp = b;

        b = a % b;

        a = temp;
    }

    return Math.abs(a);
}

function lcm(a, b) {

    return Math.abs(
        a * b
    ) / gcd(a, b);
}

function isPrime(n) {

    if (n < 2) {
        return false;
    }

    for (
        let i = 2;
        i * i <= n;
        i++
    ) {

        if (n % i === 0) {
            return false;
        }
    }

    return true;
}

function fastPower(
    base,
    exponent
) {

    let result = 1;

    while (exponent > 0) {

        if (
            exponent % 2 === 1
        ) {

            result *= base;
        }

        base *= base;

        exponent =
            Math.floor(
                exponent / 2
            );
    }

    return result;
}


/* ============================================================
   MAIN DEMONSTRATION
   ============================================================ */

console.log(
    "========================================"
);

console.log(
    " DATA STRUCTURES & ALGORITHMS - JAVASCRIPT"
);

console.log(
    "========================================"
);

console.log(
    "Author    : Saloni Tiwari"
);

console.log(
    "Programme : IIT Madras BS Degree - Diploma Level"
);

console.log();


/* Arrays */

let arr =
    [64, 25, 12, 22, 11];

console.log(
    "Original Array:"
);

printArray(arr);

const sortedArray =
    bubbleSort(arr);

console.log(
    "Sorted Array:"
);

printArray(sortedArray);

console.log(
    "Maximum:",
    maximumElement(arr)
);

console.log(
    "Minimum:",
    minimumElement(arr)
);

console.log(
    "Binary Search for 22:",
    binarySearch(sortedArray, 22)
);


/* Recursion */

console.log(
    "Factorial of 5:",
    factorial(5)
);

console.log(
    "Fibonacci of 10:",
    fibonacci(10)
);


/* Linked List */

const linkedList =
    new LinkedList();

linkedList.insertAtEnd(10);
linkedList.insertAtEnd(20);
linkedList.insertAtBeginning(5);

console.log(
    "Linked List:"
);

linkedList.display();


/* Stack */

const stack =
    new Stack();

stack.push(10);
stack.push(20);
stack.push(30);

console.log(
    "Stack Top:",
    stack.top()
);


/* Queue */

const queue =
    new Queue();

queue.enqueue(10);
queue.enqueue(20);

console.log(
    "Queue Front:",
    queue.front()
);


/* Binary Search Tree */

let root = null;

root =
    insertBST(root, 50);

root =
    insertBST(root, 30);

root =
    insertBST(root, 70);

root =
    insertBST(root, 20);

root =
    insertBST(root, 40);

root =
    insertBST(root, 60);

root =
    insertBST(root, 80);

console.log(
    "BST Inorder:"
);

inorder(root);


/* Graph */

const graph = [

    [1, 2],

    [0, 3],

    [0, 3],

    [1, 2]
];

console.log(
    "Graph BFS:"
);

BFS(graph, 0);

console.log(
    "Graph DFS:"
);

DFS(
    graph,
    0,
    new Array(
        graph.length
    ).fill(false)
);


/* Dynamic Programming */

console.log(
    "DP Fibonacci(10):",
    dpFibonacci(10)
);


/* Mathematics */

console.log(
    "GCD(48, 18):",
    gcd(48, 18)
);

console.log(
    "LCM(12, 18):",
    lcm(12, 18)
);

console.log(
    "Is 29 Prime?",
    isPrime(29)
);


/* Bit Manipulation */

console.log(
    "Set Bits in 15:",
    countSetBits(15)
);

console.log(
    "========================================"
);

console.log(
    "              COMPLETED"
);

console.log(
    "========================================"
);