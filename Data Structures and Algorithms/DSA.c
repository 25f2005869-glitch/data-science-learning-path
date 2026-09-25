/*
===========================================================
                 DATA STRUCTURES & ALGORITHMS IN C
===========================================================
Single File: DSA.c

Topics:
1. Arrays
2. Strings
3. Searching
4. Sorting
5. Recursion
6. Linked List
7. Doubly Linked List
8. Circular Linked List
9. Stack
10. Queue
11. Circular Queue
12. Hash Table
13. Binary Tree
14. Binary Search Tree
15. Heap
16. Graph
17. BFS
18. DFS
19. Dijkstra
20. Prim's Algorithm
21. Kruskal's Algorithm
22. Greedy Algorithms
23. Backtracking
24. Dynamic Programming
25. Trie
26. Disjoint Set Union
27. Bit Manipulation
28. Mathematical Algorithms
===========================================================
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

/* =========================================================
   1. ARRAYS
   ========================================================= */

void printArray(int a[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");
}

void reverseArray(int a[], int n) {
    int i = 0, j = n - 1;

    while (i < j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
        i++;
        j--;
    }
}

int maxArray(int a[], int n) {
    int max = a[0];

    for (int i = 1; i < n; i++)
        if (a[i] > max)
            max = a[i];

    return max;
}

int minArray(int a[], int n) {
    int min = a[0];

    for (int i = 1; i < n; i++)
        if (a[i] < min)
            min = a[i];

    return min;
}

/* =========================================================
   2. STRINGS
   ========================================================= */

int stringLength(char str[]) {
    int i = 0;

    while (str[i] != '\0')
        i++;

    return i;
}

void reverseString(char str[]) {
    int i = 0;
    int j = strlen(str) - 1;

    while (i < j) {
        char temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++;
        j--;
    }
}

int isPalindromeString(char str[]) {
    int i = 0;
    int j = strlen(str) - 1;

    while (i < j) {
        if (str[i] != str[j])
            return 0;

        i++;
        j--;
    }

    return 1;
}

/* =========================================================
   3. LINEAR SEARCH
   ========================================================= */

int linearSearch(int a[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (a[i] == key)
            return i;
    }

    return -1;
}

/* =========================================================
   4. BINARY SEARCH
   ========================================================= */

int binarySearch(int a[], int n, int key) {
    int left = 0;
    int right = n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (a[mid] == key)
            return mid;

        if (a[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1;
}

/* =========================================================
   5. BUBBLE SORT
   ========================================================= */

void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;

        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;

                swapped = 1;
            }
        }

        if (!swapped)
            break;
    }
}

/* =========================================================
   6. SELECTION SORT
   ========================================================= */

void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;

        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[minIndex])
                minIndex = j;
        }

        int temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
}

/* =========================================================
   7. INSERTION SORT
   ========================================================= */

void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }
}

/* =========================================================
   8. MERGE SORT
   ========================================================= */

void merge(int a[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++)
        L[i] = a[left + i];

    for (int j = 0; j < n2; j++)
        R[j] = a[mid + 1 + j];

    int i = 0;
    int j = 0;
    int k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            a[k++] = L[i++];
        else
            a[k++] = R[j++];
    }

    while (i < n1)
        a[k++] = L[i++];

    while (j < n2)
        a[k++] = R[j++];

    free(L);
    free(R);
}

void mergeSort(int a[], int left, int right) {
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;

    mergeSort(a, left, mid);
    mergeSort(a, mid + 1, right);

    merge(a, left, mid, right);
}

/* =========================================================
   9. QUICK SORT
   ========================================================= */

int partition(int a[], int low, int high) {
    int pivot = a[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (a[j] < pivot) {
            i++;

            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }

    int temp = a[i + 1];
    a[i + 1] = a[high];
    a[high] = temp;

    return i + 1;
}

void quickSort(int a[], int low, int high) {
    if (low < high) {
        int p = partition(a, low, high);

        quickSort(a, low, p - 1);
        quickSort(a, p + 1, high);
    }
}

/* =========================================================
   10. RECURSION
   ========================================================= */

int factorial(int n) {
    if (n <= 1)
        return 1;

    return n * factorial(n - 1);
}

int fibonacci(int n) {
    if (n <= 1)
        return n;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int recursiveBinarySearch(int a[], int left, int right, int key) {
    if (left > right)
        return -1;

    int mid = left + (right - left) / 2;

    if (a[mid] == key)
        return mid;

    if (key < a[mid])
        return recursiveBinarySearch(a, left, mid - 1, key);

    return recursiveBinarySearch(a, mid + 1, right, key);
}

/* =========================================================
   11. SINGLY LINKED LIST
   ========================================================= */

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *createNode(int data) {
    Node *newNode = malloc(sizeof(Node));

    if (newNode == NULL)
        return NULL;

    newNode->data = data;
    newNode->next = NULL;

    return newNode;
}

void insertBeginning(Node **head, int data) {
    Node *newNode = createNode(data);

    newNode->next = *head;
    *head = newNode;
}

void insertEnd(Node **head, int data) {
    Node *newNode = createNode(data);

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    Node *temp = *head;

    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
}

void deleteBeginning(Node **head) {
    if (*head == NULL)
        return;

    Node *temp = *head;
    *head = (*head)->next;

    free(temp);
}

void deleteEnd(Node **head) {
    if (*head == NULL)
        return;

    if ((*head)->next == NULL) {
        free(*head);
        *head = NULL;
        return;
    }

    Node *temp = *head;

    while (temp->next->next != NULL)
        temp = temp->next;

    free(temp->next);
    temp->next = NULL;
}

void printLinkedList(Node *head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }

    printf("NULL\n");
}

/* =========================================================
   12. DOUBLY LINKED LIST
   ========================================================= */

typedef struct DNode {
    int data;
    struct DNode *prev;
    struct DNode *next;
} DNode;

DNode *createDNode(int data) {
    DNode *node = malloc(sizeof(DNode));

    node->data = data;
    node->prev = NULL;
    node->next = NULL;

    return node;
}

void insertDoublyEnd(DNode **head, int data) {
    DNode *newNode = createDNode(data);

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    DNode *temp = *head;

    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
    newNode->prev = temp;
}

void printDoublyList(DNode *head) {
    while (head != NULL) {
        printf("%d <-> ", head->data);
        head = head->next;
    }

    printf("NULL\n");
}

/* =========================================================
   13. STACK USING ARRAY
   ========================================================= */

#define STACK_SIZE 100

typedef struct {
    int data[STACK_SIZE];
    int top;
} Stack;

void initStack(Stack *s) {
    s->top = -1;
}

int isStackEmpty(Stack *s) {
    return s->top == -1;
}

int isStackFull(Stack *s) {
    return s->top == STACK_SIZE - 1;
}

void push(Stack *s, int value) {
    if (isStackFull(s)) {
        printf("Stack Overflow\n");
        return;
    }

    s->data[++s->top] = value;
}

int pop(Stack *s) {
    if (isStackEmpty(s)) {
        printf("Stack Underflow\n");
        return -1;
    }

    return s->data[s->top--];
}

int peek(Stack *s) {
    if (isStackEmpty(s))
        return -1;

    return s->data[s->top];
}

/* =========================================================
   14. QUEUE
   ========================================================= */

#define QUEUE_SIZE 100

typedef struct {
    int data[QUEUE_SIZE];
    int front;
    int rear;
} Queue;

void initQueue(Queue *q) {
    q->front = 0;
    q->rear = -1;
}

int isQueueEmpty(Queue *q) {
    return q->front > q->rear;
}

void enqueue(Queue *q, int value) {
    if (q->rear == QUEUE_SIZE - 1) {
        printf("Queue Overflow\n");
        return;
    }

    q->data[++q->rear] = value;
}

int dequeue(Queue *q) {
    if (isQueueEmpty(q)) {
        printf("Queue Underflow\n");
        return -1;
    }

    return q->data[q->front++];
}

/* =========================================================
   15. CIRCULAR QUEUE
   ========================================================= */

#define CQUEUE_SIZE 10

typedef struct {
    int data[CQUEUE_SIZE];
    int front;
    int rear;
    int count;
} CircularQueue;

void initCircularQueue(CircularQueue *q) {
    q->front = 0;
    q->rear = -1;
    q->count = 0;
}

void circularEnqueue(CircularQueue *q, int value) {
    if (q->count == CQUEUE_SIZE) {
        printf("Circular Queue Full\n");
        return;
    }

    q->rear = (q->rear + 1) % CQUEUE_SIZE;
    q->data[q->rear] = value;
    q->count++;
}

int circularDequeue(CircularQueue *q) {
    if (q->count == 0)
        return -1;

    int value = q->data[q->front];

    q->front = (q->front + 1) % CQUEUE_SIZE;
    q->count--;

    return value;
}

/* =========================================================
   16. BINARY TREE
   ========================================================= */

typedef struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

TreeNode *createTreeNode(int data) {
    TreeNode *node = malloc(sizeof(TreeNode));

    node->data = data;
    node->left = NULL;
    node->right = NULL;

    return node;
}

void inorder(TreeNode *root) {
    if (root == NULL)
        return;

    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

void preorder(TreeNode *root) {
    if (root == NULL)
        return;

    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

void postorder(TreeNode *root) {
    if (root == NULL)
        return;

    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

/* =========================================================
   17. BINARY SEARCH TREE
   ========================================================= */

TreeNode *bstInsert(TreeNode *root, int data) {
    if (root == NULL)
        return createTreeNode(data);

    if (data < root->data)
        root->left = bstInsert(root->left, data);
    else if (data > root->data)
        root->right = bstInsert(root->right, data);

    return root;
}

TreeNode *bstSearch(TreeNode *root, int key) {
    if (root == NULL || root->data == key)
        return root;

    if (key < root->data)
        return bstSearch(root->left, key);

    return bstSearch(root->right, key);
}

TreeNode *findMin(TreeNode *root) {
    while (root != NULL && root->left != NULL)
        root = root->left;

    return root;
}

TreeNode *bstDelete(TreeNode *root, int key) {
    if (root == NULL)
        return NULL;

    if (key < root->data) {
        root->left = bstDelete(root->left, key);
    }
    else if (key > root->data) {
        root->right = bstDelete(root->right, key);
    }
    else {
        if (root->left == NULL) {
            TreeNode *temp = root->right;
            free(root);
            return temp;
        }

        if (root->right == NULL) {
            TreeNode *temp = root->left;
            free(root);
            return temp;
        }

        TreeNode *temp = findMin(root->right);

        root->data = temp->data;
        root->right = bstDelete(root->right, temp->data);
    }

    return root;
}

/* =========================================================
   18. HEAP
   ========================================================= */

void heapify(int a[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] > a[largest])
        largest = left;

    if (right < n && a[right] > a[largest])
        largest = right;

    if (largest != i) {
        int temp = a[i];
        a[i] = a[largest];
        a[largest] = temp;

        heapify(a, n, largest);
    }
}

void heapSort(int a[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(a, n, i);

    for (int i = n - 1; i > 0; i--) {
        int temp = a[0];
        a[0] = a[i];
        a[i] = temp;

        heapify(a, i, 0);
    }
}

/* =========================================================
   19. GRAPH - ADJACENCY MATRIX
   ========================================================= */

#define MAX_VERTICES 20

void addEdgeMatrix(int graph[MAX_VERTICES][MAX_VERTICES],
                   int u, int v) {
    graph[u][v] = 1;
    graph[v][u] = 1;
}

void bfs(int graph[MAX_VERTICES][MAX_VERTICES],
         int vertices,
         int start) {

    int visited[MAX_VERTICES] = {0};
    int queue[MAX_VERTICES];

    int front = 0;
    int rear = 0;

    queue[rear++] = start;
    visited[start] = 1;

    while (front < rear) {
        int current = queue[front++];

        printf("%d ", current);

        for (int i = 0; i < vertices; i++) {
            if (graph[current][i] && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }

    printf("\n");
}

void dfsUtil(int graph[MAX_VERTICES][MAX_VERTICES],
             int vertices,
             int current,
             int visited[]) {

    visited[current] = 1;

    printf("%d ", current);

    for (int i = 0; i < vertices; i++) {
        if (graph[current][i] && !visited[i])
            dfsUtil(graph, vertices, i, visited);
    }
}

void dfs(int graph[MAX_VERTICES][MAX_VERTICES],
         int vertices,
         int start) {

    int visited[MAX_VERTICES] = {0};

    dfsUtil(graph, vertices, start, visited);

    printf("\n");
}

/* =========================================================
   20. DIJKSTRA ALGORITHM
   ========================================================= */

#define INF 1000000000

int minDistance(int dist[], int visited[], int n) {
    int min = INF;
    int index = -1;

    for (int i = 0; i < n; i++) {
        if (!visited[i] && dist[i] < min) {
            min = dist[i];
            index = i;
        }
    }

    return index;
}

void dijkstra(int graph[MAX_VERTICES][MAX_VERTICES],
              int n,
              int source) {

    int dist[MAX_VERTICES];
    int visited[MAX_VERTICES] = {0};

    for (int i = 0; i < n; i++)
        dist[i] = INF;

    dist[source] = 0;

    for (int count = 0; count < n - 1; count++) {

        int u = minDistance(dist, visited, n);

        if (u == -1)
            break;

        visited[u] = 1;

        for (int v = 0; v < n; v++) {
            if (!visited[v] &&
                graph[u][v] > 0 &&
                dist[u] != INF &&
                dist[u] + graph[u][v] < dist[v]) {

                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (dist[i] == INF)
            printf("%d -> INF\n", i);
        else
            printf("%d -> %d\n", i, dist[i]);
    }
}

/* =========================================================
   21. DISJOINT SET UNION
   ========================================================= */

int parent[100];
int rankValue[100];

void makeSet(int n) {
    for (int i = 0; i < n; i++) {
        parent[i] = i;
        rankValue[i] = 0;
    }
}

int findSet(int x) {
    if (parent[x] != x)
        parent[x] = findSet(parent[x]);

    return parent[x];
}

void unionSet(int a, int b) {
    int rootA = findSet(a);
    int rootB = findSet(b);

    if (rootA == rootB)
        return;

    if (rankValue[rootA] < rankValue[rootB]) {
        parent[rootA] = rootB;
    }
    else if (rankValue[rootA] > rankValue[rootB]) {
        parent[rootB] = rootA;
    }
    else {
        parent[rootB] = rootA;
        rankValue[rootA]++;
    }
}

/* =========================================================
   22. KRUSKAL'S ALGORITHM
   ========================================================= */

typedef struct Edge {
    int u;
    int v;
    int weight;
} Edge;

int compareEdges(const void *a, const void *b) {
    Edge *e1 = (Edge *)a;
    Edge *e2 = (Edge *)b;

    return e1->weight - e2->weight;
}

void kruskal(Edge edges[], int edgeCount, int vertices) {

    makeSet(vertices);

    qsort(edges,
          edgeCount,
          sizeof(Edge),
          compareEdges);

    int total = 0;
    int selected = 0;

    for (int i = 0;
         i < edgeCount && selected < vertices - 1;
         i++) {

        int u = edges[i].u;
        int v = edges[i].v;

        if (findSet(u) != findSet(v)) {

            printf("%d - %d : %d\n",
                   u,
                   v,
                   edges[i].weight);

            total += edges[i].weight;
            selected++;

            unionSet(u, v);
        }
    }

    printf("MST Weight = %d\n", total);
}

/* =========================================================
   23. PRIM'S ALGORITHM
   ========================================================= */

int minKey(int key[], int mstSet[], int n) {

    int min = INF;
    int index = -1;

    for (int i = 0; i < n; i++) {
        if (!mstSet[i] && key[i] < min) {
            min = key[i];
            index = i;
        }
    }

    return index;
}

void prim(int graph[MAX_VERTICES][MAX_VERTICES], int n) {

    int parentVertex[MAX_VERTICES];
    int key[MAX_VERTICES];
    int mstSet[MAX_VERTICES] = {0};

    for (int i = 0; i < n; i++) {
        key[i] = INF;
        parentVertex[i] = -1;
    }

    key[0] = 0;

    for (int count = 0; count < n - 1; count++) {

        int u = minKey(key, mstSet, n);

        if (u == -1)
            break;

        mstSet[u] = 1;

        for (int v = 0; v < n; v++) {

            if (graph[u][v] &&
                !mstSet[v] &&
                graph[u][v] < key[v]) {

                parentVertex[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    int total = 0;

    for (int i = 1; i < n; i++) {
        printf("%d - %d : %d\n",
               parentVertex[i],
               i,
               key[i]);

        total += key[i];
    }

    printf("MST Weight = %d\n", total);
}

/* =========================================================
   24. GREEDY - ACTIVITY SELECTION
   ========================================================= */

typedef struct {
    int start;
    int finish;
} Activity;

int compareActivity(const void *a, const void *b) {

    Activity *x = (Activity *)a;
    Activity *y = (Activity *)b;

    return x->finish - y->finish;
}

void activitySelection(Activity activities[], int n) {

    qsort(activities,
          n,
          sizeof(Activity),
          compareActivity);

    printf("Selected Activities:\n");

    int lastFinish = -1;

    for (int i = 0; i < n; i++) {

        if (activities[i].start >= lastFinish) {

            printf("(%d, %d)\n",
                   activities[i].start,
                   activities[i].finish);

            lastFinish = activities[i].finish;
        }
    }
}

/* =========================================================
   25. BACKTRACKING - N QUEENS
   ========================================================= */

#define NQUEENS 10

int board[NQUEENS][NQUEENS];

int isSafeQueen(int row, int col, int n) {

    for (int i = 0; i < row; i++)
        if (board[i][col])
            return 0;

    for (int i = row - 1, j = col - 1;
         i >= 0 && j >= 0;
         i--, j--) {

        if (board[i][j])
            return 0;
    }

    for (int i = row - 1, j = col + 1;
         i >= 0 && j < n;
         i--, j++) {

        if (board[i][j])
            return 0;
    }

    return 1;
}

int solveNQueens(int row, int n) {

    if (row == n)
        return 1;

    for (int col = 0; col < n; col++) {

        if (isSafeQueen(row, col, n)) {

            board[row][col] = 1;

            if (solveNQueens(row + 1, n))
                return 1;

            board[row][col] = 0;
        }
    }

    return 0;
}

void printQueenBoard(int n) {

    for (int i = 0; i < n; i++) {

        for (int j = 0; j < n; j++)
            printf("%d ", board[i][j]);

        printf("\n");
    }
}

/* =========================================================
   26. DYNAMIC PROGRAMMING - FIBONACCI
   ========================================================= */

int dpFibonacci(int n) {

    if (n <= 1)
        return n;

    int *dp = malloc((n + 1) * sizeof(int));

    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++)
        dp[i] = dp[i - 1] + dp[i - 2];

    int answer = dp[n];

    free(dp);

    return answer;
}

/* =========================================================
   27. DYNAMIC PROGRAMMING - 0/1 KNAPSACK
   ========================================================= */

int knapsack(int capacity,
             int weights[],
             int values[],
             int n) {

    int dp[n + 1][capacity + 1];

    for (int i = 0; i <= n; i++) {

        for (int w = 0; w <= capacity; w++) {

            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            }
            else if (weights[i - 1] <= w) {

                int include =
                    values[i - 1] +
                    dp[i - 1][w - weights[i - 1]];

                int exclude =
                    dp[i - 1][w];

                dp[i][w] =
                    include > exclude ?
                    include : exclude;
            }
            else {
                dp[i][w] =
                    dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

/* =========================================================
   28. LONGEST COMMON SUBSEQUENCE
   ========================================================= */

int maxValue(int a, int b) {
    return a > b ? a : b;
}

int lcs(char X[], char Y[]) {

    int m = strlen(X);
    int n = strlen(Y);

    int dp[m + 1][n + 1];

    for (int i = 0; i <= m; i++) {

        for (int j = 0; j <= n; j++) {

            if (i == 0 || j == 0)
                dp[i][j] = 0;

            else if (X[i - 1] == Y[j - 1])
                dp[i][j] =
                    dp[i - 1][j - 1] + 1;

            else
                dp[i][j] =
                    maxValue(dp[i - 1][j],
                             dp[i][j - 1]);
        }
    }

    return dp[m][n];
}

/* =========================================================
   29. TRIE
   ========================================================= */

#define ALPHABET_SIZE 26

typedef struct TrieNode {
    struct TrieNode *children[ALPHABET_SIZE];
    int isEnd;
} TrieNode;

TrieNode *createTrieNode() {

    TrieNode *node =
        malloc(sizeof(TrieNode));

    node->isEnd = 0;

    for (int i = 0; i < ALPHABET_SIZE; i++)
        node->children[i] = NULL;

    return node;
}

void trieInsert(TrieNode *root, char word[]) {

    TrieNode *current = root;

    for (int i = 0; word[i] != '\0'; i++) {

        int index = word[i] - 'a';

        if (current->children[index] == NULL)
            current->children[index] =
                createTrieNode();

        current = current->children[index];
    }

    current->isEnd = 1;
}

int trieSearch(TrieNode *root, char word[]) {

    TrieNode *current = root;

    for (int i = 0; word[i] != '\0'; i++) {

        int index = word[i] - 'a';

        if (current->children[index] == NULL)
            return 0;

        current = current->children[index];
    }

    return current->isEnd;
}

/* =========================================================
   30. BIT MANIPULATION
   ========================================================= */

int isPowerOfTwo(int n) {

    if (n <= 0)
        return 0;

    return (n & (n - 1)) == 0;
}

int countSetBits(unsigned int n) {

    int count = 0;

    while (n) {
        n = n & (n - 1);
        count++;
    }

    return count;
}

void printBinary(unsigned int n) {

    if (n > 1)
        printBinary(n / 2);

    printf("%d", n % 2);
}

/* =========================================================
   31. MATHEMATICAL ALGORITHMS
   ========================================================= */

int gcd(int a, int b) {

    while (b != 0) {

        int temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

int lcm(int a, int b) {

    return abs(a * b) / gcd(a, b);
}

int isPrime(int n) {

    if (n < 2)
        return 0;

    for (int i = 2; i * i <= n; i++) {

        if (n % i == 0)
            return 0;
    }

    return 1;
}

int power(int base, int exponent) {

    int result = 1;

    while (exponent > 0) {

        if (exponent % 2 == 1)
            result *= base;

        base *= base;
        exponent /= 2;
    }

    return result;
}

/* =========================================================
   32. MAIN FUNCTION
   ========================================================= */

int main() {

    printf("=============================================\n");
    printf("       DATA STRUCTURES & ALGORITHMS IN C\n");
    printf("=============================================\n\n");

    /* Arrays */
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original Array: ");
    printArray(arr, n);

    bubbleSort(arr, n);

    printf("Sorted Array: ");
    printArray(arr, n);

    /* Searching */
    printf("Binary Search for 22: Index = %d\n",
           binarySearch(arr, n, 22));

    /* Recursion */
    printf("Factorial of 5 = %d\n",
           factorial(5));

    printf("Fibonacci of 10 = %d\n",
           fibonacci(10));

    /* Linked List */
    Node *head = NULL;

    insertEnd(&head, 10);
    insertEnd(&head, 20);
    insertBeginning(&head, 5);

    printf("Linked List: ");
    printLinkedList(head);

    /* Stack */
    Stack stack;

    initStack(&stack);

    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);

    printf("Stack Top = %d\n",
           peek(&stack));

    printf("Stack Pop = %d\n",
           pop(&stack));

    /* Queue */
    Queue queue;

    initQueue(&queue);

    enqueue(&queue, 10);
    enqueue(&queue, 20);

    printf("Queue Dequeue = %d\n",
           dequeue(&queue));

    /* Binary Search Tree */
    TreeNode *root = NULL;

    root = bstInsert(root, 50);
    root = bstInsert(root, 30);
    root = bstInsert(root, 70);
    root = bstInsert(root, 20);
    root = bstInsert(root, 40);
    root = bstInsert(root, 60);
    root = bstInsert(root, 80);

    printf("BST Inorder: ");
    inorder(root);
    printf("\n");

    /* Graph */
    int graph[MAX_VERTICES][MAX_VERTICES] = {0};

    addEdgeMatrix(graph, 0, 1);
    addEdgeMatrix(graph, 0, 2);
    addEdgeMatrix(graph, 1, 3);
    addEdgeMatrix(graph, 2, 3);

    printf("Graph BFS: ");
    bfs(graph, 4, 0);

    printf("Graph DFS: ");
    dfs(graph, 4, 0);

    /* Dynamic Programming */
    printf("DP Fibonacci(10) = %d\n",
           dpFibonacci(10));

    /* Mathematics */
    printf("GCD(48, 18) = %d\n",
           gcd(48, 18));

    printf("LCM(12, 18) = %d\n",
           lcm(12, 18));

    printf("Is 29 Prime? %s\n",
           isPrime(29) ? "Yes" : "No");

    /* Bit Manipulation */
    printf("Set Bits in 15 = %d\n",
           countSetBits(15));

    printf("\n=============================================\n");
    printf("             DSA PROGRAM COMPLETED\n");
    printf("=============================================\n");

    return 0;
}