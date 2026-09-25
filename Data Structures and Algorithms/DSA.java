/*
============================================================
             DATA STRUCTURES & ALGORITHMS
                         JAVA
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

import java.util.*;

/* ============================================================
   MAIN CLASS
   ============================================================ */

public class DSA {

    /* ========================================================
       1. ARRAYS
       ======================================================== */

    static void printArray(int[] arr) {

        for (int value : arr)
            System.out.print(value + " ");

        System.out.println();
    }

    static void reverseArray(int[] arr) {

        int left = 0;
        int right = arr.length - 1;

        while (left < right) {

            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }

    static int maximumElement(int[] arr) {

        int maximum = arr[0];

        for (int value : arr)
            maximum = Math.max(maximum, value);

        return maximum;
    }

    static int minimumElement(int[] arr) {

        int minimum = arr[0];

        for (int value : arr)
            minimum = Math.min(minimum, value);

        return minimum;
    }

    /* ========================================================
       2. STRINGS
       ======================================================== */

    static boolean isPalindrome(String str) {

        int left = 0;
        int right = str.length() - 1;

        while (left < right) {

            if (str.charAt(left) != str.charAt(right))
                return false;

            left++;
            right--;
        }

        return true;
    }

    static String reverseString(String str) {

        return new StringBuilder(str)
                .reverse()
                .toString();
    }

    /* ========================================================
       3. LINEAR SEARCH
       ======================================================== */

    static int linearSearch(int[] arr, int key) {

        for (int i = 0; i < arr.length; i++) {

            if (arr[i] == key)
                return i;
        }

        return -1;
    }

    /* ========================================================
       4. BINARY SEARCH
       ======================================================== */

    static int binarySearch(int[] arr, int key) {

        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {

            int mid =
                    left + (right - left) / 2;

            if (arr[mid] == key)
                return mid;

            if (arr[mid] < key)
                left = mid + 1;

            else
                right = mid - 1;
        }

        return -1;
    }

    /* ========================================================
       5. BUBBLE SORT
       ======================================================== */

    static void bubbleSort(int[] arr) {

        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {

            boolean swapped = false;

            for (int j = 0; j < n - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {

                    int temp = arr[j];

                    arr[j] = arr[j + 1];

                    arr[j + 1] = temp;

                    swapped = true;
                }
            }

            if (!swapped)
                break;
        }
    }

    /* ========================================================
       6. SELECTION SORT
       ======================================================== */

    static void selectionSort(int[] arr) {

        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {

            int minimumIndex = i;

            for (int j = i + 1; j < n; j++) {

                if (arr[j] < arr[minimumIndex])
                    minimumIndex = j;
            }

            int temp = arr[i];

            arr[i] = arr[minimumIndex];

            arr[minimumIndex] = temp;
        }
    }

    /* ========================================================
       7. INSERTION SORT
       ======================================================== */

    static void insertionSort(int[] arr) {

        for (int i = 1; i < arr.length; i++) {

            int key = arr[i];

            int j = i - 1;

            while (j >= 0 && arr[j] > key) {

                arr[j + 1] = arr[j];

                j--;
            }

            arr[j + 1] = key;
        }
    }

    /* ========================================================
       8. MERGE SORT
       ======================================================== */

    static void merge(
            int[] arr,
            int left,
            int mid,
            int right) {

        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];

        for (int j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        int i = 0;
        int j = 0;
        int k = left;

        while (i < n1 && j < n2) {

            if (L[i] <= R[j])
                arr[k++] = L[i++];

            else
                arr[k++] = R[j++];
        }

        while (i < n1)
            arr[k++] = L[i++];

        while (j < n2)
            arr[k++] = R[j++];
    }

    static void mergeSort(
            int[] arr,
            int left,
            int right) {

        if (left >= right)
            return;

        int mid =
                left + (right - left) / 2;

        mergeSort(arr, left, mid);

        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }

    /* ========================================================
       9. QUICK SORT
       ======================================================== */

    static int partition(
            int[] arr,
            int low,
            int high) {

        int pivot = arr[high];

        int i = low - 1;

        for (int j = low; j < high; j++) {

            if (arr[j] < pivot) {

                i++;

                int temp = arr[i];

                arr[i] = arr[j];

                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];

        arr[i + 1] = arr[high];

        arr[high] = temp;

        return i + 1;
    }

    static void quickSort(
            int[] arr,
            int low,
            int high) {

        if (low < high) {

            int pivotIndex =
                    partition(arr, low, high);

            quickSort(
                    arr,
                    low,
                    pivotIndex - 1);

            quickSort(
                    arr,
                    pivotIndex + 1,
                    high);
        }
    }

    /* ========================================================
       10. RECURSION
       ======================================================== */

    static long factorial(int n) {

        if (n <= 1)
            return 1;

        return n * factorial(n - 1);
    }

    static long fibonacci(int n) {

        if (n <= 1)
            return n;

        return fibonacci(n - 1)
                + fibonacci(n - 2);
    }

    /* ========================================================
       11. SINGLY LINKED LIST
       ======================================================== */

    static class Node {

        int data;

        Node next;

        Node(int data) {

            this.data = data;

            this.next = null;
        }
    }

    static void insertAtBeginning(
            Node[] head,
            int value) {

        Node newNode =
                new Node(value);

        newNode.next = head[0];

        head[0] = newNode;
    }

    static void insertAtEnd(
            Node[] head,
            int value) {

        Node newNode =
                new Node(value);

        if (head[0] == null) {

            head[0] = newNode;

            return;
        }

        Node current = head[0];

        while (current.next != null)
            current = current.next;

        current.next = newNode;
    }

    static void deleteFirst(Node[] head) {

        if (head[0] != null)
            head[0] = head[0].next;
    }

    static void printLinkedList(Node head) {

        while (head != null) {

            System.out.print(
                    head.data + " -> ");

            head = head.next;
        }

        System.out.println("NULL");
    }

    /* ========================================================
       12. DOUBLY LINKED LIST
       ======================================================== */

    static class DoublyNode {

        int data;

        DoublyNode previous;

        DoublyNode next;

        DoublyNode(int data) {

            this.data = data;

            previous = null;

            next = null;
        }
    }

    static void insertDoublyEnd(
            DoublyNode[] head,
            int value) {

        DoublyNode newNode =
                new DoublyNode(value);

        if (head[0] == null) {

            head[0] = newNode;

            return;
        }

        DoublyNode current = head[0];

        while (current.next != null)
            current = current.next;

        current.next = newNode;

        newNode.previous = current;
    }

    static void printDoublyList(
            DoublyNode head) {

        while (head != null) {

            System.out.print(
                    head.data + " <-> ");

            head = head.next;
        }

        System.out.println("NULL");
    }

    /* ========================================================
       13. STACK
       ======================================================== */

    static class StackDSA {

        private Stack<Integer> stack =
                new Stack<>();

        void push(int value) {

            stack.push(value);
        }

        void pop() {

            if (!stack.empty())
                stack.pop();
        }

        int top() {

            if (stack.empty())
                return -1;

            return stack.peek();
        }

        boolean isEmpty() {

            return stack.empty();
        }

        int size() {

            return stack.size();
        }
    }

    /* ========================================================
       14. QUEUE
       ======================================================== */

    static class QueueDSA {

        private Queue<Integer> queue =
                new LinkedList<>();

        void enqueue(int value) {

            queue.offer(value);
        }

        void dequeue() {

            if (!queue.isEmpty())
                queue.poll();
        }

        int front() {

            if (queue.isEmpty())
                return -1;

            return queue.peek();
        }

        boolean isEmpty() {

            return queue.isEmpty();
        }
    }

    /* ========================================================
       15. HASHING
       ======================================================== */

    static void hashingExample() {

        HashMap<Integer, String> students =
                new HashMap<>();

        students.put(101, "Saloni");

        students.put(102, "Student");

        for (Map.Entry<Integer, String> entry
                : students.entrySet()) {

            System.out.println(
                    entry.getKey()
                    + " : "
                    + entry.getValue());
        }
    }

    /* ========================================================
       16. BINARY TREE
       ======================================================== */

    static class TreeNode {

        int data;

        TreeNode left;

        TreeNode right;

        TreeNode(int data) {

            this.data = data;

            left = null;

            right = null;
        }
    }

    static void inorder(TreeNode root) {

        if (root == null)
            return;

        inorder(root.left);

        System.out.print(
                root.data + " ");

        inorder(root.right);
    }

    static void preorder(TreeNode root) {

        if (root == null)
            return;

        System.out.print(
                root.data + " ");

        preorder(root.left);

        preorder(root.right);
    }

    static void postorder(TreeNode root) {

        if (root == null)
            return;

        postorder(root.left);

        postorder(root.right);

        System.out.print(
                root.data + " ");
    }

    /* ========================================================
       17. BINARY SEARCH TREE
       ======================================================== */

    static TreeNode insertBST(
            TreeNode root,
            int value) {

        if (root == null)
            return new TreeNode(value);

        if (value < root.data)

            root.left =
                    insertBST(
                            root.left,
                            value);

        else if (value > root.data)

            root.right =
                    insertBST(
                            root.right,
                            value);

        return root;
    }

    static boolean searchBST(
            TreeNode root,
            int key) {

        if (root == null)
            return false;

        if (root.data == key)
            return true;

        if (key < root.data)

            return searchBST(
                    root.left,
                    key);

        return searchBST(
                root.right,
                key);
    }

    /* ========================================================
       18. HEAP SORT
       ======================================================== */

    static void heapify(
            int[] arr,
            int n,
            int index) {

        int largest = index;

        int left = 2 * index + 1;

        int right = 2 * index + 2;

        if (left < n &&
                arr[left] > arr[largest])

            largest = left;

        if (right < n &&
                arr[right] > arr[largest])

            largest = right;

        if (largest != index) {

            int temp = arr[index];

            arr[index] = arr[largest];

            arr[largest] = temp;

            heapify(
                    arr,
                    n,
                    largest);
        }
    }

    static void heapSort(int[] arr) {

        int n = arr.length;

        for (int i = n / 2 - 1;
             i >= 0;
             i--)

            heapify(arr, n, i);

        for (int i = n - 1;
             i > 0;
             i--) {

            int temp = arr[0];

            arr[0] = arr[i];

            arr[i] = temp;

            heapify(arr, i, 0);
        }
    }

    /* ========================================================
       19. GRAPH - BFS
       ======================================================== */

    static void BFS(
            ArrayList<ArrayList<Integer>> graph,
            int start) {

        boolean[] visited =
                new boolean[graph.size()];

        Queue<Integer> queue =
                new LinkedList<>();

        visited[start] = true;

        queue.offer(start);

        while (!queue.isEmpty()) {

            int current =
                    queue.poll();

            System.out.print(
                    current + " ");

            for (int neighbour :
                    graph.get(current)) {

                if (!visited[neighbour]) {

                    visited[neighbour] = true;

                    queue.offer(neighbour);
                }
            }
        }

        System.out.println();
    }

    /* ========================================================
       20. GRAPH - DFS
       ======================================================== */

    static void DFS(
            ArrayList<ArrayList<Integer>> graph,
            int current,
            boolean[] visited) {

        visited[current] = true;

        System.out.print(
                current + " ");

        for (int neighbour :
                graph.get(current)) {

            if (!visited[neighbour])

                DFS(
                        graph,
                        neighbour,
                        visited);
        }
    }

    /* ========================================================
       21. DIJKSTRA ALGORITHM
       ======================================================== */

    static class Edge {

        int node;

        int weight;

        Edge(int node, int weight) {

            this.node = node;

            this.weight = weight;
        }
    }

    static void dijkstra(
            ArrayList<ArrayList<Edge>> graph,
            int source) {

        int n = graph.size();

        int[] distance =
                new int[n];

        Arrays.fill(
                distance,
                Integer.MAX_VALUE);

        PriorityQueue<int[]> pq =
                new PriorityQueue<>(
                        Comparator.comparingInt(
                                a -> a[0]));

        distance[source] = 0;

        pq.offer(
                new int[]{0, source});

        while (!pq.isEmpty()) {

            int[] current =
                    pq.poll();

            int currentDistance =
                    current[0];

            int node =
                    current[1];

            if (currentDistance >
                    distance[node])
                continue;

            for (Edge edge :
                    graph.get(node)) {

                int next =
                        edge.node;

                int newDistance =
                        currentDistance
                        + edge.weight;

                if (newDistance <
                        distance[next]) {

                    distance[next] =
                            newDistance;

                    pq.offer(
                            new int[]{
                                    newDistance,
                                    next
                            });
                }
            }
        }

        for (int i = 0; i < n; i++) {

            System.out.println(
                    "Distance to "
                    + i
                    + " = "
                    + (distance[i] ==
                       Integer.MAX_VALUE
                       ? "INF"
                       : distance[i]));
        }
    }

    /* ========================================================
       22. GREEDY - ACTIVITY SELECTION
       ======================================================== */

    static class Activity {

        int start;

        int finish;

        Activity(int start,
                 int finish) {

            this.start = start;

            this.finish = finish;
        }
    }

    static void activitySelection(
            ArrayList<Activity> activities) {

        activities.sort(
                Comparator.comparingInt(
                        a -> a.finish));

        int lastFinish = -1;

        for (Activity activity :
                activities) {

            if (activity.start >=
                    lastFinish) {

                System.out.println(
                        "("
                        + activity.start
                        + ", "
                        + activity.finish
                        + ")");

                lastFinish =
                        activity.finish;
            }
        }
    }

    /* ========================================================
       23. BACKTRACKING - N QUEENS
       ======================================================== */

    static boolean isSafeQueen(
            int[][] board,
            int row,
            int col,
            int n) {

        for (int i = 0; i < row; i++) {

            if (board[i][col] == 1)
                return false;
        }

        for (int i = row - 1,
             j = col - 1;
             i >= 0 && j >= 0;
             i--, j--) {

            if (board[i][j] == 1)
                return false;
        }

        for (int i = row - 1,
             j = col + 1;
             i >= 0 && j < n;
             i--, j++) {

            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    static boolean solveNQueens(
            int[][] board,
            int row,
            int n) {

        if (row == n)
            return true;

        for (int col = 0;
             col < n;
             col++) {

            if (isSafeQueen(
                    board,
                    row,
                    col,
                    n)) {

                board[row][col] = 1;

                if (solveNQueens(
                        board,
                        row + 1,
                        n))

                    return true;

                board[row][col] = 0;
            }
        }

        return false;
    }

    /* ========================================================
       24. DYNAMIC PROGRAMMING - FIBONACCI
       ======================================================== */

    static long dpFibonacci(int n) {

        if (n <= 1)
            return n;

        long[] dp =
                new long[n + 1];

        dp[0] = 0;

        dp[1] = 1;

        for (int i = 2;
             i <= n;
             i++) {

            dp[i] =
                    dp[i - 1]
                    + dp[i - 2];
        }

        return dp[n];
    }

    /* ========================================================
       25. 0/1 KNAPSACK
       ======================================================== */

    static int knapsack(
            int capacity,
            int[] weights,
            int[] values) {

        int n = weights.length;

        int[][] dp =
                new int[n + 1]
                        [capacity + 1];

        for (int i = 1;
             i <= n;
             i++) {

            for (int weight = 1;
                 weight <= capacity;
                 weight++) {

                if (weights[i - 1]
                        <= weight) {

                    dp[i][weight] =
                            Math.max(
                                    values[i - 1]
                                    + dp[i - 1]
                                    [weight
                                    - weights[i - 1]],

                                    dp[i - 1]
                                    [weight]);
                }
                else {

                    dp[i][weight] =
                            dp[i - 1]
                            [weight];
                }
            }
        }

        return dp[n][capacity];
    }

    /* ========================================================
       26. LONGEST COMMON SUBSEQUENCE
       ======================================================== */

    static int LCS(
            String X,
            String Y) {

        int m = X.length();

        int n = Y.length();

        int[][] dp =
                new int[m + 1]
                        [n + 1];

        for (int i = 1;
             i <= m;
             i++) {

            for (int j = 1;
                 j <= n;
                 j++) {

                if (X.charAt(i - 1)
                        == Y.charAt(j - 1)) {

                    dp[i][j] =
                            dp[i - 1][j - 1]
                            + 1;
                }
                else {

                    dp[i][j] =
                            Math.max(
                                    dp[i - 1][j],
                                    dp[i][j - 1]);
                }
            }
        }

        return dp[m][n];
    }

    /* ========================================================
       27. TRIE
       ======================================================== */

    static class TrieNode {

        TrieNode[] children =
                new TrieNode[26];

        boolean isEnd = false;
    }

    static class Trie {

        TrieNode root =
                new TrieNode();

        void insert(String word) {

            TrieNode current = root;

            for (char character :
                    word.toCharArray()) {

                int index =
                        character - 'a';

                if (current.children[index]
                        == null) {

                    current.children[index] =
                            new TrieNode();
                }

                current =
                        current.children[index];
            }

            current.isEnd = true;
        }

        boolean search(String word) {

            TrieNode current = root;

            for (char character :
                    word.toCharArray()) {

                int index =
                        character - 'a';

                if (current.children[index]
                        == null)

                    return false;

                current =
                        current.children[index];
            }

            return current.isEnd;
        }
    }

    /* ========================================================
       28. DISJOINT SET UNION
       ======================================================== */

    static class DSU {

        int[] parent;

        int[] rank;

        DSU(int n) {

            parent = new int[n];

            rank = new int[n];

            for (int i = 0; i < n; i++)
                parent[i] = i;
        }

        int find(int x) {

            if (parent[x] != x)

                parent[x] =
                        find(parent[x]);

            return parent[x];
        }

        void union(int a, int b) {

            a = find(a);

            b = find(b);

            if (a == b)
                return;

            if (rank[a] < rank[b])

                parent[a] = b;

            else if (rank[a] > rank[b])

                parent[b] = a;

            else {

                parent[b] = a;

                rank[a]++;
            }
        }
    }

    /* ========================================================
       29. BIT MANIPULATION
       ======================================================== */

    static boolean isPowerOfTwo(int n) {

        if (n <= 0)
            return false;

        return (n & (n - 1)) == 0;
    }

    static int countSetBits(int n) {

        int count = 0;

        while (n != 0) {

            n = n & (n - 1);

            count++;
        }

        return count;
    }

    /* ========================================================
       30. MATHEMATICAL ALGORITHMS
       ======================================================== */

    static int gcd(int a, int b) {

        while (b != 0) {

            int temp = b;

            b = a % b;

            a = temp;
        }

        return a;
    }

    static int lcm(int a, int b) {

        return Math.abs(a * b)
                / gcd(a, b);
    }

    static boolean isPrime(int n) {

        if (n < 2)
            return false;

        for (int i = 2;
             i * i <= n;
             i++) {

            if (n % i == 0)
                return false;
        }

        return true;
    }

    static long fastPower(
            long base,
            long exponent) {

        long result = 1;

        while (exponent > 0) {

            if ((exponent & 1) == 1)
                result *= base;

            base *= base;

            exponent >>= 1;
        }

        return result;
    }

    /* ========================================================
       MAIN METHOD
       ======================================================== */

    public static void main(String[] args) {

        System.out.println(
                "========================================");

        System.out.println(
                " DATA STRUCTURES & ALGORITHMS - JAVA");

        System.out.println(
                "========================================");

        System.out.println(
                "Author    : Saloni Tiwari");

        System.out.println(
                "Programme : IIT Madras BS Degree - Diploma Level");

        System.out.println();

        /* Arrays */

        int[] arr =
                {64, 25, 12, 22, 11};

        System.out.print(
                "Original Array: ");

        printArray(arr);

        bubbleSort(arr);

        System.out.print(
                "Sorted Array: ");

        printArray(arr);

        System.out.println(
                "Maximum: "
                + maximumElement(arr));

        System.out.println(
                "Minimum: "
                + minimumElement(arr));

        System.out.println(
                "Binary Search for 22: "
                + binarySearch(arr, 22));

        /* Recursion */

        System.out.println(
                "Factorial of 5: "
                + factorial(5));

        System.out.println(
                "Fibonacci of 10: "
                + fibonacci(10));

        /* Linked List */

        Node[] head =
                new Node[1];

        insertAtEnd(head, 10);

        insertAtEnd(head, 20);

        insertAtBeginning(head, 5);

        System.out.print(
                "Linked List: ");

        printLinkedList(head[0]);

        /* Stack */

        StackDSA stack =
                new StackDSA();

        stack.push(10);

        stack.push(20);

        stack.push(30);

        System.out.println(
                "Stack Top: "
                + stack.top());

        /* Queue */

        QueueDSA queue =
                new QueueDSA();

        queue.enqueue(10);

        queue.enqueue(20);

        System.out.println(
                "Queue Front: "
                + queue.front());

        /* Binary Search Tree */

        TreeNode root = null;

        root = insertBST(root, 50);

        root = insertBST(root, 30);

        root = insertBST(root, 70);

        root = insertBST(root, 20);

        root = insertBST(root, 40);

        root = insertBST(root, 60);

        root = insertBST(root, 80);

        System.out.print(
                "BST Inorder: ");

        inorder(root);

        System.out.println();

        /* Graph */

        ArrayList<ArrayList<Integer>>
                graph = new ArrayList<>();

        for (int i = 0; i < 4; i++)
            graph.add(
                    new ArrayList<>());

        graph.get(0).add(1);
        graph.get(0).add(2);

        graph.get(1).add(0);
        graph.get(1).add(3);

        graph.get(2).add(0);
        graph.get(2).add(3);

        graph.get(3).add(1);
        graph.get(3).add(2);

        System.out.print(
                "BFS: ");

        BFS(graph, 0);

        System.out.print(
                "DFS: ");

        DFS(
                graph,
                0,
                new boolean[graph.size()]);

        System.out.println();

        /* Dynamic Programming */

        System.out.println(
                "DP Fibonacci(10): "
                + dpFibonacci(10));

        /* Mathematics */

        System.out.println(
                "GCD(48, 18): "
                + gcd(48, 18));

        System.out.println(
                "LCM(12, 18): "
                + lcm(12, 18));

        System.out.println(
                "Is 29 Prime? "
                + (isPrime(29)
                ? "Yes"
                : "No"));

        /* Bit Manipulation */

        System.out.println(
                "Set Bits in 15: "
                + countSetBits(15));

        System.out.println(
                "========================================");

        System.out.println(
                "              COMPLETED");

        System.out.println(
                "========================================");
    }
}