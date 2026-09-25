/*
============================================================
             DATA STRUCTURES & ALGORITHMS
                    JAVASCRIPT
============================================================

Author      : Saloni Tiwari
Programme   : IIT Madras BS Degree — Diploma Level

File        : script.js
Purpose     : Interactive DSA Demonstrations

============================================================
*/


/* ============================================================
   1. ARRAY DEMONSTRATION
   ============================================================ */

let originalArray = [64, 25, 12, 22, 11];

let currentArray = [...originalArray];


function displayArray() {

    const container =
        document.getElementById("arrayDisplay");

    if (!container) return;

    container.innerHTML = "";

    currentArray.forEach(value => {

        const item =
            document.createElement("div");

        item.className = "array-item";

        item.textContent = value;

        container.appendChild(item);
    });
}


function reverseArray() {

    currentArray.reverse();

    displayArray();

    const output =
        document.getElementById("arrayOutput");

    if (output) {

        output.textContent =
            "Array reversed successfully.";
    }
}


function sortArray() {

    currentArray.sort(
        (a, b) => a - b
    );

    displayArray();

    const output =
        document.getElementById("arrayOutput");

    if (output) {

        output.textContent =
            "Array sorted successfully.";
    }
}


function resetArray() {

    currentArray =
        [...originalArray];

    displayArray();

    const output =
        document.getElementById("arrayOutput");

    if (output) {

        output.textContent =
            "Array reset successfully.";
    }
}


/* ============================================================
   2. LINEAR SEARCH
   ============================================================ */

function linearSearch() {

    const input =
        document.getElementById("searchValue");

    const output =
        document.getElementById("searchOutput");

    if (!input || !output) return;

    const value =
        Number(input.value);

    if (input.value === "") {

        output.textContent =
            "Please enter a number.";

        return;
    }

    let foundIndex = -1;

    for (
        let i = 0;
        i < currentArray.length;
        i++
    ) {

        if (currentArray[i] === value) {

            foundIndex = i;

            break;
        }
    }

    if (foundIndex === -1) {

        output.textContent =
            "Element not found.";

    } else {

        output.textContent =
            "Element found at index "
            + foundIndex + ".";
    }
}


/* ============================================================
   3. BINARY SEARCH
   ============================================================ */

function binarySearch() {

    const input =
        document.getElementById("searchValue");

    const output =
        document.getElementById("searchOutput");

    if (!input || !output) return;

    if (input.value === "") {

        output.textContent =
            "Please enter a number.";

        return;
    }

    const value =
        Number(input.value);

    const sortedArray =
        [...currentArray].sort(
            (a, b) => a - b
        );

    let left = 0;

    let right =
        sortedArray.length - 1;

    let foundIndex = -1;


    while (left <= right) {

        const mid =
            Math.floor(
                (left + right) / 2
            );

        if (sortedArray[mid] === value) {

            foundIndex = mid;

            break;

        } else if (
            sortedArray[mid] < value
        ) {

            left = mid + 1;

        } else {

            right = mid - 1;
        }
    }


    if (foundIndex === -1) {

        output.textContent =
            "Element not found.";

    } else {

        output.textContent =
            "Element found at sorted index "
            + foundIndex
            + ".";
    }
}


/* ============================================================
   4. LINKED LIST
   ============================================================ */

let linkedList =
    [10, 20, 30];


function displayLinkedList() {

    const output =
        document.getElementById(
            "linkedListOutput"
        );

    if (!output) return;

    if (linkedList.length === 0) {

        output.textContent =
            "NULL";

        return;
    }

    output.textContent =
        linkedList.join(" -> ")
        + " -> NULL";
}


function addNode() {

    const newValue =
        linkedList.length === 0
        ? 10
        : linkedList[
            linkedList.length - 1
        ] + 10;

    linkedList.push(newValue);

    displayLinkedList();
}


function removeNode() {

    if (linkedList.length > 0) {

        linkedList.pop();
    }

    displayLinkedList();
}


/* ============================================================
   5. STACK
   ============================================================ */

let stack =
    [10, 20, 30];


function displayStack() {

    const output =
        document.getElementById(
            "stackOutput"
        );

    if (!output) return;

    if (stack.length === 0) {

        output.textContent =
            "Stack is empty.";

        return;
    }

    output.textContent =
        "Stack: "
        + stack.join(" -> ")
        + "\nTop: "
        + stack[stack.length - 1];
}


function pushStack() {

    const input =
        document.getElementById(
            "stackValue"
        );

    if (!input) return;

    if (input.value === "") {

        return;
    }

    const value =
        Number(input.value);

    stack.push(value);

    input.value = "";

    displayStack();
}


function popStack() {

    if (stack.length > 0) {

        stack.pop();
    }

    displayStack();
}


/* ============================================================
   6. QUEUE
   ============================================================ */

let queue =
    [10, 20, 30];


function displayQueue() {

    const output =
        document.getElementById(
            "queueOutput"
        );

    if (!output) return;

    if (queue.length === 0) {

        output.textContent =
            "Queue is empty.";

        return;
    }

    output.textContent =
        "Queue: "
        + queue.join(" -> ");
}


function enqueue() {

    const input =
        document.getElementById(
            "queueValue"
        );

    if (!input) return;

    if (input.value === "") {

        return;
    }

    const value =
        Number(input.value);

    queue.push(value);

    input.value = "";

    displayQueue();
}


function dequeue() {

    if (queue.length > 0) {

        queue.shift();
    }

    displayQueue();
}


/* ============================================================
   7. FACTORIAL
   ============================================================ */

function calculateFactorial() {

    const input =
        document.getElementById(
            "factorialValue"
        );

    const output =
        document.getElementById(
            "factorialOutput"
        );

    if (!input || !output) return;

    if (input.value === "") {

        output.textContent =
            "Please enter a number.";

        return;
    }

    const value =
        Number(input.value);


    if (
        value < 0 ||
        !Number.isInteger(value)
    ) {

        output.textContent =
            "Please enter a valid non-negative integer.";

        return;
    }


    let result = 1;


    for (
        let i = 2;
        i <= value;
        i++
    ) {

        result *= i;
    }


    output.textContent =
        value
        + "! = "
        + result;
}


/* ============================================================
   8. FIBONACCI
   ============================================================ */

function fibonacci(n) {

    if (n <= 1) {

        return n;
    }

    let a = 0;

    let b = 1;


    for (
        let i = 2;
        i <= n;
        i++
    ) {

        const next =
            a + b;

        a = b;

        b = next;
    }

    return b;
}


/* ============================================================
   9. BUBBLE SORT
   ============================================================ */

function bubbleSort(arr) {

    const result =
        [...arr];

    for (
        let i = 0;
        i < result.length - 1;
        i++
    ) {

        let swapped = false;


        for (
            let j = 0;
            j < result.length - i - 1;
            j++
        ) {

            if (
                result[j] >
                result[j + 1]
            ) {

                [
                    result[j],
                    result[j + 1]
                ] = [
                    result[j + 1],
                    result[j]
                ];

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
   10. SELECTION SORT
   ============================================================ */

function selectionSort(arr) {

    const result =
        [...arr];


    for (
        let i = 0;
        i < result.length - 1;
        i++
    ) {

        let minimumIndex = i;


        for (
            let j = i + 1;
            j < result.length;
            j++
        ) {

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
   11. INSERTION SORT
   ============================================================ */

function insertionSort(arr) {

    const result =
        [...arr];


    for (
        let i = 1;
        i < result.length;
        i++
    ) {

        const key =
            result[i];

        let j =
            i - 1;


        while (
            j >= 0 &&
            result[j] > key
        ) {

            result[j + 1] =
                result[j];

            j--;
        }


        result[j + 1] =
            key;
    }


    return result;
}


/* ============================================================
   12. MERGE SORT
   ============================================================ */

function mergeArrays(left, right) {

    const result = [];

    let i = 0;

    let j = 0;


    while (
        i < left.length &&
        j < right.length
    ) {

        if (
            left[i] <= right[j]
        ) {

            result.push(
                left[i]
            );

            i++;

        } else {

            result.push(
                right[j]
            );

            j++;
        }
    }


    while (
        i < left.length
    ) {

        result.push(
            left[i]
        );

        i++;
    }


    while (
        j < right.length
    ) {

        result.push(
            right[j]
        );

        j++;
    }


    return result;
}


function mergeSort(arr) {

    if (arr.length <= 1) {

        return arr;
    }


    const mid =
        Math.floor(
            arr.length / 2
        );


    const left =
        mergeSort(
            arr.slice(0, mid)
        );


    const right =
        mergeSort(
            arr.slice(mid)
        );


    return mergeArrays(
        left,
        right
    );
}


/* ============================================================
   13. QUICK SORT
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

        if (
            arr[i] < pivot
        ) {

            left.push(
                arr[i]
            );

        } else {

            right.push(
                arr[i]
            );
        }
    }


    return [
        ...quickSort(left),
        pivot,
        ...quickSort(right)
    ];
}


/* ============================================================
   14. BINARY TREE
   ============================================================ */

class TreeNode {

    constructor(data) {

        this.data = data;

        this.left = null;

        this.right = null;
    }
}


function inorder(root, result = []) {

    if (root === null) {

        return result;
    }


    inorder(
        root.left,
        result
    );


    result.push(
        root.data
    );


    inorder(
        root.right,
        result
    );


    return result;
}


function preorder(root, result = []) {

    if (root === null) {

        return result;
    }


    result.push(
        root.data
    );


    preorder(
        root.left,
        result
    );


    preorder(
        root.right,
        result
    );


    return result;
}


function postorder(root, result = []) {

    if (root === null) {

        return result;
    }


    postorder(
        root.left,
        result
    );


    postorder(
        root.right,
        result
    );


    result.push(
        root.data
    );


    return result;
}


/* ============================================================
   15. BINARY SEARCH TREE
   ============================================================ */

function insertBST(root, value) {

    if (root === null) {

        return new TreeNode(
            value
        );
    }


    if (
        value < root.data
    ) {

        root.left =
            insertBST(
                root.left,
                value
            );

    } else if (
        value > root.data
    ) {

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


    if (
        root.data === key
    ) {

        return true;
    }


    if (
        key < root.data
    ) {

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
   16. GRAPH - BFS
   ============================================================ */

function BFS(graph, start) {

    const visited =
        new Array(
            graph.length
        ).fill(false);


    const queue = [];

    let front = 0;


    visited[start] = true;

    queue.push(start);


    const result = [];


    while (
        front < queue.length
    ) {

        const current =
            queue[front++];


        result.push(
            current
        );


        for (
            const neighbour
            of graph[current]
        ) {

            if (
                !visited[neighbour]
            ) {

                visited[neighbour] =
                    true;

                queue.push(
                    neighbour
                );
            }
        }
    }


    return result;
}


/* ============================================================
   17. GRAPH - DFS
   ============================================================ */

function DFS(
    graph,
    current,
    visited = new Set(),
    result = []
) {

    visited.add(
        current
    );


    result.push(
        current
    );


    for (
        const neighbour
        of graph[current]
    ) {

        if (
            !visited.has(
                neighbour
            )
        ) {

            DFS(
                graph,
                neighbour,
                visited,
                result
            );
        }
    }


    return result;
}


/* ============================================================
   18. DIJKSTRA ALGORITHM
   ============================================================ */

function dijkstra(
    graph,
    source
) {

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
                (
                    current === -1 ||
                    distance[i] <
                    distance[current]
                )
            ) {

                current = i;
            }
        }


        if (current === -1) {

            break;
        }


        visited[current] =
            true;


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
   19. GREEDY - ACTIVITY SELECTION
   ============================================================ */

function activitySelection(
    activities
) {

    const sorted =
        [...activities].sort(
            (a, b) =>
                a.finish - b.finish
        );


    const selected = [];

    let lastFinish = -Infinity;


    for (
        const activity
        of sorted
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
   20. N-QUEENS
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

        if (
            board[i][col] === 1
        ) {

            return false;
        }
    }


    for (
        let i = row - 1,
        j = col - 1;
        i >= 0 && j >= 0;
        i--, j--
    ) {

        if (
            board[i][j] === 1
        ) {

            return false;
        }
    }


    for (
        let i = row - 1,
        j = col + 1;
        i >= 0 && j < n;
        i--, j++
    ) {

        if (
            board[i][j] === 1
        ) {

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

            board[row][col] =
                1;


            if (
                solveNQueens(
                    board,
                    row + 1,
                    n
                )
            ) {

                return true;
            }


            board[row][col] =
                0;
        }
    }


    return false;
}


/* ============================================================
   21. DYNAMIC PROGRAMMING - FIBONACCI
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
            dp[i - 1]
            + dp[i - 2];
    }


    return dp[n];
}


/* ============================================================
   22. 0/1 KNAPSACK
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
            {
                length:
                    n + 1
            },
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

                        values[i - 1]
                        +
                        dp[
                            i - 1
                        ][
                            weight -
                            weights[i - 1]
                        ],

                        dp[
                            i - 1
                        ][weight]
                    );

            } else {

                dp[i][weight] =
                    dp[
                        i - 1
                    ][weight];
            }
        }
    }


    return dp[n][capacity];
}


/* ============================================================
   23. LONGEST COMMON SUBSEQUENCE
   ============================================================ */

function LCS(X, Y) {

    const m =
        X.length;

    const n =
        Y.length;


    const dp =
        Array.from(
            {
                length:
                    m + 1
            },
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
   24. TRIE
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


        current.isEnd =
            true;
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
   25. DISJOINT SET UNION
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

            this.parent[i] =
                i;
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

            this.parent[a] =
                b;

        } else if (
            this.rank[a] >
            this.rank[b]
        ) {

            this.parent[b] =
                a;

        } else {

            this.parent[b] =
                a;

            this.rank[a]++;
        }
    }
}


/* ============================================================
   26. BIT MANIPULATION
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
   27. MATHEMATICAL ALGORITHMS
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

        if (
            n % i === 0
        ) {

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
   INITIALIZE PAGE
   ============================================================ */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        displayArray();

        displayLinkedList();

        displayStack();

        displayQueue();

    }
);