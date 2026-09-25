 /*
 ============================================================
              DATA STRUCTURES & ALGORITHMS
                       C++
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
 12. Circular Queue
 13. Hashing
 14. Binary Tree
 15. Binary Search Tree
 16. Heap
 17. Graph
 18. BFS
 19. DFS
 20. Dijkstra Algorithm
 21. Prim's Algorithm
 22. Kruskal's Algorithm
 23. Greedy Algorithms
 24. Divide and Conquer
 25. Backtracking
 26. Dynamic Programming
 27. Trie
 28. Disjoint Set Union
 29. Bit Manipulation
 30. Mathematical Algorithms

 ============================================================
 Author: Saloni Tiwari
 IIT Madras BS Degree — Diploma Level
 ============================================================
 */

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <climits>
#include <cmath>

using namespace std;

/* ============================================================
   1. ARRAYS
   ============================================================ */

void printArray(const vector<int>& arr) {
    for (int value : arr)
        cout << value << " ";
    cout << endl;
}

void reverseArray(vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

int maximumElement(const vector<int>& arr) {
    int maximum = arr[0];

    for (int value : arr)
        maximum = max(maximum, value);

    return maximum;
}

int minimumElement(const vector<int>& arr) {
    int minimum = arr[0];

    for (int value : arr)
        minimum = min(minimum, value);

    return minimum;
}

/* ============================================================
   2. STRINGS
   ============================================================ */

bool isPalindrome(const string& str) {
    int left = 0;
    int right = str.length() - 1;

    while (left < right) {
        if (str[left] != str[right])
            return false;

        left++;
        right--;
    }

    return true;
}

string reverseString(string str) {
    reverse(str.begin(), str.end());
    return str;
}

/* ============================================================
   3. LINEAR SEARCH
   ============================================================ */

int linearSearch(const vector<int>& arr, int key) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == key)
            return i;
    }

    return -1;
}

/* ============================================================
   4. BINARY SEARCH
   ============================================================ */

int binarySearch(const vector<int>& arr, int key) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == key)
            return mid;

        if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1;
}

/* ============================================================
   5. BUBBLE SORT
   ============================================================ */

void bubbleSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;

        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        if (!swapped)
            break;
    }
}

/* ============================================================
   6. SELECTION SORT
   ============================================================ */

void selectionSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; i++) {
        int minimumIndex = i;

        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minimumIndex])
                minimumIndex = j;
        }

        swap(arr[i], arr[minimumIndex]);
    }
}

/* ============================================================
   7. INSERTION SORT
   ============================================================ */

void insertionSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

/* ============================================================
   8. MERGE SORT
   ============================================================ */

void mergeArray(vector<int>& arr, int left, int mid, int right) {

    vector<int> temp;

    int i = left;
    int j = mid + 1;

    while (i <= mid && j <= right) {

        if (arr[i] <= arr[j])
            temp.push_back(arr[i++]);
        else
            temp.push_back(arr[j++]);
    }

    while (i <= mid)
        temp.push_back(arr[i++]);

    while (j <= right)
        temp.push_back(arr[j++]);

    for (int k = 0; k < temp.size(); k++)
        arr[left + k] = temp[k];
}

void mergeSort(vector<int>& arr, int left, int right) {

    if (left >= right)
        return;

    int mid = left + (right - left) / 2;

    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);

    mergeArray(arr, left, mid, right);
}

/* ============================================================
   9. QUICK SORT
   ============================================================ */

int partitionArray(vector<int>& arr, int low, int high) {

    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {

        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);

    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {

    if (low < high) {

        int pivotIndex =
            partitionArray(arr, low, high);

        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

/* ============================================================
   10. RECURSION
   ============================================================ */

long long factorial(int n) {

    if (n <= 1)
        return 1;

    return n * factorial(n - 1);
}

long long fibonacci(int n) {

    if (n <= 1)
        return n;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

/* ============================================================
   11. LINKED LIST
   ============================================================ */

struct Node {

    int data;
    Node* next;

    Node(int value) {
        data = value;
        next = nullptr;
    }
};

void insertAtBeginning(Node*& head, int value) {

    Node* newNode = new Node(value);

    newNode->next = head;
    head = newNode;
}

void insertAtEnd(Node*& head, int value) {

    Node* newNode = new Node(value);

    if (head == nullptr) {
        head = newNode;
        return;
    }

    Node* current = head;

    while (current->next != nullptr)
        current = current->next;

    current->next = newNode;
}

void deleteFirst(Node*& head) {

    if (head == nullptr)
        return;

    Node* temp = head;

    head = head->next;

    delete temp;
}

void printLinkedList(Node* head) {

    while (head != nullptr) {

        cout << head->data << " -> ";

        head = head->next;
    }

    cout << "NULL" << endl;
}

/* ============================================================
   12. DOUBLY LINKED LIST
   ============================================================ */

struct DoublyNode {

    int data;
    DoublyNode* previous;
    DoublyNode* next;

    DoublyNode(int value) {
        data = value;
        previous = nullptr;
        next = nullptr;
    }
};

void insertDoublyEnd(DoublyNode*& head, int value) {

    DoublyNode* newNode =
        new DoublyNode(value);

    if (head == nullptr) {
        head = newNode;
        return;
    }

    DoublyNode* current = head;

    while (current->next != nullptr)
        current = current->next;

    current->next = newNode;
    newNode->previous = current;
}

void printDoublyList(DoublyNode* head) {

    while (head != nullptr) {

        cout << head->data << " <-> ";

        head = head->next;
    }

    cout << "NULL" << endl;
}

/* ============================================================
   13. STACK
   ============================================================ */

class StackDSA {

private:
    vector<int> data;

public:

    void push(int value) {
        data.push_back(value);
    }

    void pop() {

        if (!data.empty())
            data.pop_back();
    }

    int top() {

        if (data.empty())
            return -1;

        return data.back();
    }

    bool empty() {
        return data.empty();
    }

    int size() {
        return data.size();
    }
};

/* ============================================================
   14. QUEUE
   ============================================================ */

class QueueDSA {

private:
    queue<int> q;

public:

    void enqueue(int value) {
        q.push(value);
    }

    void dequeue() {

        if (!q.empty())
            q.pop();
    }

    int front() {

        if (q.empty())
            return -1;

        return q.front();
    }

    bool empty() {
        return q.empty();
    }
};

/* ============================================================
   15. HASHING
   ============================================================ */

void hashingExample() {

    unordered_map<int, string> student;

    student[101] = "Saloni";
    student[102] = "Student";

    for (auto item : student) {

        cout << item.first
             << " : "
             << item.second
             << endl;
    }
}

/* ============================================================
   16. BINARY TREE
   ============================================================ */

struct TreeNode {

    int data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int value) {

        data = value;
        left = nullptr;
        right = nullptr;
    }
};

void inorder(TreeNode* root) {

    if (root == nullptr)
        return;

    inorder(root->left);

    cout << root->data << " ";

    inorder(root->right);
}

void preorder(TreeNode* root) {

    if (root == nullptr)
        return;

    cout << root->data << " ";

    preorder(root->left);
    preorder(root->right);
}

void postorder(TreeNode* root) {

    if (root == nullptr)
        return;

    postorder(root->left);
    postorder(root->right);

    cout << root->data << " ";
}

/* ============================================================
   17. BINARY SEARCH TREE
   ============================================================ */

TreeNode* insertBST(TreeNode* root, int value) {

    if (root == nullptr)
        return new TreeNode(value);

    if (value < root->data)
        root->left =
            insertBST(root->left, value);

    else if (value > root->data)
        root->right =
            insertBST(root->right, value);

    return root;
}

bool searchBST(TreeNode* root, int key) {

    if (root == nullptr)
        return false;

    if (root->data == key)
        return true;

    if (key < root->data)
        return searchBST(root->left, key);

    return searchBST(root->right, key);
}

/* ============================================================
   18. HEAP
   ============================================================ */

void heapify(vector<int>& arr,
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

        swap(arr[index], arr[largest]);

        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {

    int n = arr.size();

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {

        swap(arr[0], arr[i]);

        heapify(arr, i, 0);
    }
}

/* ============================================================
   19. GRAPH - BFS
   ============================================================ */

void BFS(const vector<vector<int>>& graph,
         int start) {

    int n = graph.size();

    vector<bool> visited(n, false);

    queue<int> q;

    visited[start] = true;

    q.push(start);

    while (!q.empty()) {

        int current = q.front();

        q.pop();

        cout << current << " ";

        for (int neighbour : graph[current]) {

            if (!visited[neighbour]) {

                visited[neighbour] = true;

                q.push(neighbour);
            }
        }
    }

    cout << endl;
}

/* ============================================================
   20. GRAPH - DFS
   ============================================================ */

void DFSUtil(const vector<vector<int>>& graph,
             int current,
             vector<bool>& visited) {

    visited[current] = true;

    cout << current << " ";

    for (int neighbour : graph[current]) {

        if (!visited[neighbour])
            DFSUtil(graph,
                    neighbour,
                    visited);
    }
}

void DFS(const vector<vector<int>>& graph,
         int start) {

    vector<bool> visited(graph.size(), false);

    DFSUtil(graph, start, visited);

    cout << endl;
}

/* ============================================================
   21. DIJKSTRA ALGORITHM
   ============================================================ */

void dijkstra(const vector<vector<pair<int, int>>>& graph,
              int source) {

    int n = graph.size();

    vector<int> distance(n, INT_MAX);

    priority_queue<
        pair<int, int>,
        vector<pair<int, int>>,
        greater<pair<int, int>>
    > pq;

    distance[source] = 0;

    pq.push({0, source});

    while (!pq.empty()) {

        int currentDistance =
            pq.top().first;

        int current =
            pq.top().second;

        pq.pop();

        if (currentDistance >
            distance[current])
            continue;

        for (auto edge : graph[current]) {

            int next = edge.first;
            int weight = edge.second;

            if (distance[current] + weight <
                distance[next]) {

                distance[next] =
                    distance[current] + weight;

                pq.push({
                    distance[next],
                    next
                });
            }
        }
    }

    for (int i = 0; i < n; i++) {

        cout << "Distance to "
             << i
             << " = ";

        if (distance[i] == INT_MAX)
            cout << "INF";
        else
            cout << distance[i];

        cout << endl;
    }
}

/* ============================================================
   22. GREEDY - ACTIVITY SELECTION
   ============================================================ */

struct Activity {

    int start;
    int finish;
};

bool compareActivity(Activity a,
                     Activity b) {

    return a.finish < b.finish;
}

void activitySelection(
    vector<Activity> activities) {

    sort(activities.begin(),
         activities.end(),
         compareActivity);

    int lastFinish = -1;

    for (Activity activity : activities) {

        if (activity.start >= lastFinish) {

            cout << "("
                 << activity.start
                 << ", "
                 << activity.finish
                 << ") ";

            lastFinish = activity.finish;
        }
    }

    cout << endl;
}

/* ============================================================
   23. BACKTRACKING - N QUEENS
   ============================================================ */

bool isSafeQueen(
    vector<vector<int>>& board,
    int row,
    int col,
    int n) {

    for (int i = 0; i < row; i++) {

        if (board[i][col])
            return false;
    }

    for (int i = row - 1, j = col - 1;
         i >= 0 && j >= 0;
         i--, j--) {

        if (board[i][j])
            return false;
    }

    for (int i = row - 1, j = col + 1;
         i >= 0 && j < n;
         i--, j++) {

        if (board[i][j])
            return false;
    }

    return true;
}

bool solveNQueens(
    vector<vector<int>>& board,
    int row,
    int n) {

    if (row == n)
        return true;

    for (int col = 0; col < n; col++) {

        if (isSafeQueen(board,
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

/* ============================================================
   24. DYNAMIC PROGRAMMING - FIBONACCI
   ============================================================ */

long long dpFibonacci(int n) {

    if (n <= 1)
        return n;

    vector<long long> dp(n + 1);

    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++)
        dp[i] =
            dp[i - 1] +
            dp[i - 2];

    return dp[n];
}

/* ============================================================
   25. 0/1 KNAPSACK
   ============================================================ */

int knapsack(int capacity,
             vector<int> weights,
             vector<int> values) {

    int n = weights.size();

    vector<vector<int>> dp(
        n + 1,
        vector<int>(capacity + 1, 0)
    );

    for (int i = 1; i <= n; i++) {

        for (int weight = 1;
             weight <= capacity;
             weight++) {

            if (weights[i - 1] <= weight) {

                dp[i][weight] =
                    max(
                        values[i - 1] +
                        dp[i - 1]
                        [weight - weights[i - 1]],

                        dp[i - 1][weight]
                    );
            }
            else {

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

int LCS(string X, string Y) {

    int m = X.length();
    int n = Y.length();

    vector<vector<int>> dp(
        m + 1,
        vector<int>(n + 1, 0)
    );

    for (int i = 1; i <= m; i++) {

        for (int j = 1; j <= n; j++) {

            if (X[i - 1] == Y[j - 1]) {

                dp[i][j] =
                    dp[i - 1][j - 1] + 1;
            }
            else {

                dp[i][j] =
                    max(
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

public:

    TrieNode* children[26];
    bool isEnd;

    TrieNode() {

        isEnd = false;

        for (int i = 0; i < 26; i++)
            children[i] = nullptr;
    }
};

class Trie {

private:

    TrieNode* root;

public:

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {

        TrieNode* current = root;

        for (char character : word) {

            int index =
                character - 'a';

            if (current->children[index]
                == nullptr) {

                current->children[index] =
                    new TrieNode();
            }

            current =
                current->children[index];
        }

        current->isEnd = true;
    }

    bool search(string word) {

        TrieNode* current = root;

        for (char character : word) {

            int index =
                character - 'a';

            if (current->children[index]
                == nullptr)
                return false;

            current =
                current->children[index];
        }

        return current->isEnd;
    }
};

/* ============================================================
   28. DISJOINT SET UNION
   ============================================================ */

class DSU {

private:

    vector<int> parent;
    vector<int> rankValue;

public:

    DSU(int n) {

        parent.resize(n);
        rankValue.resize(n, 0);

        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x) {

        if (parent[x] != x)
            parent[x] =
                find(parent[x]);

        return parent[x];
    }

    void unite(int a, int b) {

        a = find(a);
        b = find(b);

        if (a == b)
            return;

        if (rankValue[a] <
            rankValue[b]) {

            parent[a] = b;
        }
        else if (rankValue[a] >
                 rankValue[b]) {

            parent[b] = a;
        }
        else {

            parent[b] = a;
            rankValue[a]++;
        }
    }
};

/* ============================================================
   29. BIT MANIPULATION
   ============================================================ */

bool isPowerOfTwo(int n) {

    if (n <= 0)
        return false;

    return (n & (n - 1)) == 0;
}

int countSetBits(int n) {

    int count = 0;

    while (n) {

        n = n & (n - 1);

        count++;
    }

    return count;
}

/* ============================================================
   30. MATHEMATICAL ALGORITHMS
   ============================================================ */

int gcd(int a, int b) {

    while (b != 0) {

        int temp = b;

        b = a % b;

        a = temp;
    }

    return a;
}

int lcm(int a, int b) {

    return abs(a * b) /
           gcd(a, b);
}

bool isPrime(int n) {

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

long long fastPower(
    long long base,
    long long exponent) {

    long long result = 1;

    while (exponent > 0) {

        if (exponent & 1)
            result *= base;

        base *= base;

        exponent >>= 1;
    }

    return result;
}

/* ============================================================
   MAIN FUNCTION
   ============================================================ */

int main() {

    cout << "========================================\n";
    cout << "   DATA STRUCTURES & ALGORITHMS - C++\n";
    cout << "========================================\n";

    cout << "Author    : Saloni Tiwari\n";
    cout << "Programme : IIT Madras BS Degree - Diploma Level\n\n";

    vector<int> arr =
        {64, 25, 12, 22, 11};

    cout << "Original Array: ";
    printArray(arr);

    bubbleSort(arr);

    cout << "Sorted Array: ";
    printArray(arr);

    cout << "Maximum: "
         << maximumElement(arr)
         << endl;

    cout << "Minimum: "
         << minimumElement(arr)
         << endl;

    cout << "Binary Search for 22: "
         << binarySearch(arr, 22)
         << endl;

    cout << "Factorial of 5: "
         << factorial(5)
         << endl;

    cout << "Fibonacci of 10: "
         << fibonacci(10)
         << endl;

    Node* head = nullptr;

    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtBeginning(head, 5);

    cout << "Linked List: ";
    printLinkedList(head);

    StackDSA stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);

    cout << "Stack Top: "
         << stack.top()
         << endl;

    QueueDSA queueDSA;

    queueDSA.enqueue(10);
    queueDSA.enqueue(20);

    cout << "Queue Front: "
         << queueDSA.front()
         << endl;

    TreeNode* root = nullptr;

    root = insertBST(root, 50);
    root = insertBST(root, 30);
    root = insertBST(root, 70);
    root = insertBST(root, 20);
    root = insertBST(root, 40);
    root = insertBST(root, 60);
    root = insertBST(root, 80);

    cout << "BST Inorder: ";
    inorder(root);
    cout << endl;

    vector<vector<int>> graph = {
        {1, 2},
        {0, 3},
        {0, 3},
        {1, 2}
    };

    cout << "BFS: ";
    BFS(graph, 0);

    cout << "DFS: ";
    DFS(graph, 0);

    cout << "DP Fibonacci(10): "
         << dpFibonacci(10)
         << endl;

    cout << "GCD(48, 18): "
         << gcd(48, 18)
         << endl;

    cout << "LCM(12, 18): "
         << lcm(12, 18)
         << endl;

    cout << "Is 29 Prime? "
         << (isPrime(29) ? "Yes" : "No")
         << endl;

    cout << "Set Bits in 15: "
         << countSetBits(15)
         << endl;

    cout << "\n========================================\n";
    cout << "              COMPLETED\n";
    cout << "========================================\n";

    return 0;
}