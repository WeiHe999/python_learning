#!/usr/bin/env python
# coding: utf-8

# ## Heap

# In[151]:


class MinHeap:
    def __init__(self):
        self.data = [None]
        self.cap = 100
        self.size = 0
        
    def heapify(self):
        current_data = self.data[-1]
        current_id = self.data.index(current_data)
        while True:
            parent_id = current_id // 2
            if parent_id == 0:
                break
            if current_data < self.data[parent_id]:
                parent_data = self.data[parent_id]
                self.data[current_id], self.data[parent_id] = parent_data, current_data
                current_id = parent_id
                if current_id == 1:
                    break
            else:
                break

    def bubble_down(self):
        current_id = 1
        while True:
            current_data = self.data[current_id]
            # case 1: no children
            if (current_id * 2) + 1 > self.size - 1:
                break
            # case 2: only left child
            elif current_id * 2 == self.size - 1:
                min_index = left_child_index
            #case 3: both children
            else:
                left_child_index = current_id * 2
                right_child_index = (current_id * 2) + 1
                min_index = left_child_index
                if self.data[left_child_index] > self.data[right_child_index]:
                    min_index = right_child_index
            if current_data > self.data[min_index]:
                minimum = self.data[min_index]
                self.data[current_id], self.data[min_index] = minimum, current_data
                current_id = min_index
            else:
                break

    def add(self, node):
        self.data.append(node)
        self.heapify()
        self.size += 1
        
    def remove(self):
        temp = self.data[1]
        self.data[1] = self.data[-1]
        self.data = self.data[:-1]
        self.size -= 1
        if self.size > 0:
            self.bubble_down()
        return temp
        
    def printing(self):
        for x in self.data[1:]:
            print(x, end = ' ')
        print('')


# ## Heap sort

# In[152]:


list1 = [-10,100,23,45,123,67,89]
heap = MinHeap()
list2 = []
for x in list1:
    heap.add(x)
for x in range(len(list1)):
    list2.append(heap.remove())
print(list1)
print(list2)


# ## use Max Heap to sort a list from greatest to least

# In[164]:


class MaxHeap:
    def __init__(self):
        self.data = [None]
        self.cap = 100
        self.size = 0
    
    def heapify(self):
        current = self.data[-1]
        current_index = len(self.data) - 1
        while True:
            parent_index = current_index // 2
            if parent_index == 0:
                break
            parent = self.data[parent_index]
            if current > parent:
                self.data[current_index], self.data[parent_index] = parent, current
                current_index = parent_index
                if current_index == 1:
                    break
            else:
                break
          
    def bubble_down(self):
        current_id = 1
        while True:
            current_data = self.data[current_id]
            left_child_index = current_id * 2
            right_child_index = (current_id * 2) + 1
            if right_child_index > self.size - 1:
                break
            elif left_child_index == self.size - 1:
                max_index = left_child_index
            else:
                max_index = left_child_index
                if self.data[right_child_index] > self.data[max_index]:
                    max_index = right_child_index
            if self.data[max_index] > current_data:
                tmp = self.data[max_index]
                self.data[max_index] = current_data
                self.data[current_id] = tmp
            else:
                break

    def add(self, node):
        self.data.append(node)
        self.heapify()
        self.size += 1

    def remove(self):
        temp = self.data[1]
        self.data[1] = self.data[-1]
        self.data = self.data[:-1]
        self.size -= 1
        if self.size > 0:
            self.bubble_down()
        return temp

    def printing(self):
        for x in self.data[1:]:
            print(x, end = ' ')
        print('')

list1 = [76, 12, 34, 9, 137, 98]
heap = MaxHeap()
for x in list1:
    heap.add(x)
list2 = []
for a in range(len(list1)):
    list2.append(heap.remove())
print(list2)


# ## Floyd-Warshall algorithm

# In[22]:


graph = {}
graph['a'] = {}
graph['a']['b'] = 3
graph['a']['d'] = 7
graph['b'] = {}
graph['b']['c'] = 2
graph['b']['a'] = 8
graph['c'] = {}
graph['c']['a'] = 5
graph['c']['d'] = 1
graph['d'] = {}
graph['d']['a'] = 2


# In[23]:


# use Dijkstra's algorithm to find all pairs of shortest paths
def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node
def dijkstra(start_node, end_node, graph):
    list_nodes = sorted(list(graph.keys()))
    costs = {}
    for x in graph.keys():
        if x == start_node:
            costs[x] = 0
        else:
            costs[x] = float('inf')
    parents = {}
    parents[start_node] = None
    visited = []
    while True:
        min_node = find_min_node(costs, visited) 
        if min_node == None:
            break
        visited.append(min_node)
        for x in graph[min_node].keys():
            c = costs[min_node] + graph[min_node][x]
            if c < costs[x]:
                costs[x] = c
                parents[x] = min_node
    print(costs)
    return costs[end_node]
dijkstra('a', 'd', graph)


# In[30]:


import copy
def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node

def dijkstra(start_node, end_node, graph):
    list_nodes = sorted(list(graph.keys()))
    costs = {}
    for x in graph.keys():
        if x == start_node:
            costs[x] = 0
        else:
            costs[x] = float('inf')
    parents = {}
    parents[start_node] = None
    visited = []
    while True:
        min_node = find_min_node(costs, visited) 
        if min_node == None:
            break
        visited.append(min_node)
        for x in graph[min_node].keys():
            c = costs[min_node] + graph[min_node][x]
            if c < costs[x]:
                costs[x] = c
                parents[x] = min_node
    return costs[end_node]

n = int(input())
for x in range(1, n + 1):
    line = input()
    line = [int(s) for s in line.split(' ')]
    num_nodes = line[0]
    num_edges = line[1]
    start_node = line[2]
    end_node = line[3]
    graph = {}
    if num_edges == 0:
        print('Case #' + str(x) + ': unreachable')
        continue
    for a in range(num_edges):
        line = input()
        line = [int(s) for s in line.split(' ')]
        if line[0] not in graph:
            graph[line[0]] = {}
        graph[line[0]][line[1]] = line[2]
        if line[1] not in graph:
            graph[line[1]] = {}
        graph[line[1]][line[0]] = line[2]
    cost = dijkstra(start_node, end_node, graph)
    if cost != float('inf'):
        print('Case #' + str(x) + ': ' + str(cost))
    else:
        print('Case #' + str(x) + ': unreachable')


# In[160]:


def convert_to_matrix(graph):
    list_nodes = sorted(graph.keys())
    list1 = []
    for a in list_nodes:
        list1.append([])
        for b in list_nodes:
            if a == b:
                list1[-1].append(0)
            elif b not in graph[a].keys():
                list1[-1].append(float('inf'))
            else:
                list1[-1].append(graph[a][b])
    return list1
convert_to_matrix(graph)


# In[25]:


import copy
def convert_to_matrix(graph):
    list_nodes = sorted(graph.keys())
    list1 = []
    for a in list_nodes:
        list1.append([])
        for b in list_nodes:
            if a == b:
                list1[-1].append(0)
            elif b not in graph[a].keys():
                list1[-1].append(float('inf'))
            else:
                list1[-1].append(graph[a][b])
    return list1

graph = {}
graph['a'] = {}
graph['a']['b'] = 3
graph['a']['d'] = 7
graph['b'] = {}
graph['b']['c'] = 2
graph['b']['a'] = 8
graph['c'] = {}
graph['c']['a'] = 5
graph['c']['d'] = 1
graph['d'] = {}
graph['d']['a'] = 2
list1 = convert_to_matrix(graph)
v = len(list1)
for a in range(v):
    list2 = copy.deepcopy(list1)
    for start_id in range(v):
        for end_id in range(v):
            for mid_id in range(v):
                if list1[start_id][mid_id] + list1[mid_id][end_id] < list2[start_id][end_id]:
                    list2[start_id][end_id] = list1[start_id][mid_id] + list1[mid_id][end_id]
    list1 = list2
print(list2)


# ## Union Find and Kruskals algorithm

# In[1]:


# Function to find root for a node
def find_root(node):
    x = dict_mapping[node]
    list1 = []
    while x != list_parents[x]:
        list1.append(x)
        x = list_parents[x]
    # path compression
    for y in list1:
        list_parents[y] = x
    return x

# Function to merge two nodes
def union(node1, node2):
    # find the roots 
    # if they are the same, return the root
    # if not the same, find which one has larger size, merge small component to larger component
    # update component size
    root1 = find_root(node1)
    root2 = find_root(node2)
    if root1 == root2:
        return [root1, root2]
    elif dict_comp_sizes[root2] > dict_comp_sizes[root1]:
        list_parents[root1] = root2
        dict_comp_sizes[root2] += dict_comp_sizes[root1]
        dict_comp_sizes[root1] = 0
        keep_edges.append((node1, node2))
        return root2
    else:
        list_parents[root2] = root1
        dict_comp_sizes[root1] += dict_comp_sizes[root2]
        dict_comp_sizes[root2] = 0
        keep_edges.append((node1, node2))
        return root1

# Function to find minimum spanning tree using Kruskal's algorithm
def kruskal(graph):
    list1 = []
    for x in graph.keys():
        for y in graph[x].keys():
            list1.append([x, y, graph[x][y]])
    list1 = sorted(list1, key=lambda s:s[2])
    for a in list1:
        if max(dict_comp_sizes.values())==len(list(set(list_nodes))):
            break
        parent = union(a[0], a[1])
    return parent    


# In[80]:


# step 1: define the graph
graph = {}
graph[0] = {}
graph[0][1] = 1
graph[0][2] = 6
graph[1] = {}
graph[1][2] = 2
graph[2] = {}
graph[2][3] = 3
graph[3] = {}
graph[3][0] = 5

# step 2: mapping node to node_id
list_nodes = sorted(graph.keys())
dict_mapping = {}
for k, x in enumerate(list_nodes):
    dict_mapping[x] = k

# step 3: init list_parents, and dict_comp_sizes
list_parents = []
for x in range(len(list_nodes)):
    list_parents.append(x)
dict_comp_sizes = {}
for a in list_parents:
    dict_comp_sizes[a] = 1
    
# step 4: minimum spanning tree
keep_edges = []
root = kruskal(graph)
print('root node: {}'.format(root))
print('Spanning edges:')
print(keep_edges)
min_cost = 0
for x in keep_edges:
    min_cost += graph[x[0]][x[1]]
print('Total cost: {}'.format(min_cost))


# ## Union find to detect graph cycle

# In[274]:


# step 1: graph
graph = {}
graph[0] = {}
graph[0][1] = 1
graph[0][2] = 3
graph[1] = {}
graph[1][0] = 1
graph[1][2] = 2
graph[2] = {}
graph[2][1] = 2
graph[2][0] = 3
# step 2: mapping node to node_id
list_nodes = sorted(graph.keys())
dict_mapping = {}
for k, x in enumerate(list_nodes):
    dict_mapping[x] = k
# step 3: init list_parents, and dict_comp_sizes
list_parents = []
for x in range(len(list_nodes)):
    list_parents.append(x)
dict_comp_sizes = {}
for a in list_parents:
    dict_comp_sizes[a] = 1
# step 4: def find_parent(x)
def find_root(node):
    x = dict_mapping[node]
    list1 = []
    while x != list_parents[x]:
        list1.append(x)
        x = list_parents[x]
    # path compression
    for y in list1:
        list_parents[y] = x
    return x
# step 5: def union(x, y)
def union(node1, node2):
    # find the roots 
    # if they are the same, return the root
    # if not the same, find which one has larger size, merge small component to larger component
    # update component size
    root1 = find_root(node1)
    root2 = find_root(node2)
    if root1 == root2:
        return [root1, root2]
    elif dict_comp_sizes[root2] > dict_comp_sizes[root1]:
        list_parents[root1] = root2
        dict_comp_sizes[root2] += dict_comp_sizes[root1]
        dict_comp_sizes[root1] = 0
        keep_edges.append((node1, node2))
        return root2
    else:
        list_parents[root2] = root1
        dict_comp_sizes[root1] += dict_comp_sizes[root2]
        dict_comp_sizes[root2] = 0
        keep_edges.append((node1, node2))
        return root1

test = 0
list1 = []
for x in graph.keys():
    for y in graph[x].keys():
        list1.append([x, y, graph[x][y]])
list1 = sorted(list1, key=lambda s:s[2])
for a in list1:
    root1 = find_root(a[0])
    root2 = find_root(a[1])
    if root1 == root2:
        test += 1
        print('graph contains cycle')
        break
    else:
        union(a[0], a[1])
if test == 0:
    print('graph does not contain cycle')    


# ## Priority queue

# In[277]:


# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())


# In[286]:


import heapq
list1 = [-10,100,23,45,67,98,234]
list2 = []
while list1:
    heapq.heapify(list1)
    a = list1.pop(0)
    list2.append(a)
print(list2)


# ## segment tree

# ### min range

# In[4]:


import math
# step-1: define a function to initialize list_seg_tree
def init_list_seg_tree_v1(list_data):
    return [float('inf')] * ((2 ** math.ceil((math.log(len(list_data), 2) + 1))) - 1)
# step-2: define a function to construct seg tree
def construct_seg_tree_v1(list_data, list_seg_tree, low, high, node_id):
    if low == high:
        list_seg_tree[node_id] = list_data[low]
        return list_seg_tree[node_id]
    left_id = node_id * 2 + 1
    right_id = left_id + 1
    l_low = low
    l_high = (low + high) // 2
    r_low = l_high + 1
    r_high = high
    a = min(construct_seg_tree_v1(list_data, list_seg_tree, l_low, l_high, left_id), construct_seg_tree_v1(list_data, list_seg_tree, r_low, r_high, right_id))
    list_seg_tree[node_id] = a
    return a
def query_seg_tree_v1(list_seg_tree, q_low, q_high, low, high, node_id):
    # base case 1: data range is totally inside of query range
    if q_low <= low and q_high >= high:
        return list_seg_tree[node_id]
    # base case 2: query range and data range are completely disjoint
    if low > q_high or high < q_low:
        return float('inf')
    # recursive case: ask left child and right child, and then return the min of both children
    l = query_seg_tree_v1(list_seg_tree, q_low, q_high, low, (low + high) // 2, 2 * node_id + 1)
    r = query_seg_tree_v1(list_seg_tree, q_low, q_high, (low + high) // 2 + 1, high, 2 * node_id + 2)
    return min(l, r)


# In[5]:


list_data = [-1, 2, 4, 0]
list_seg_tree = init_list_seg_tree_v1(list_data)
print(list_seg_tree)
construct_seg_tree_v1(list_data, list_seg_tree, 0, len(list_data) - 1, 0)
print(list_seg_tree)
# query
q_low = 0
q_high = 3
query_seg_tree_v1(list_seg_tree, q_low, q_high, 0, len(list_data)-1, 0)


# ## max range segment tree

# In[251]:


def init_list_seg_tree_v2(list_data):
    return [-1*float('inf')] * ((2 ** math.ceil((math.log(len(list_data), 2) + 1))) - 1)
# step-2: define a function to construct seg tree
def construct_seg_tree_v2(list_data, list_seg_tree, low, high, node_id):
    if low == high:
        list_seg_tree[node_id] = list_data[low]
        return list_seg_tree[node_id]
    left_id = node_id * 2 + 1
    right_id = left_id + 1
    l_low = low
    l_high = (low + high) // 2
    r_low = l_high + 1
    r_high = high
    a = max(construct_seg_tree_v2(list_data, list_seg_tree, l_low, l_high, left_id), construct_seg_tree_v2(list_data, list_seg_tree, r_low, r_high, right_id))
    list_seg_tree[node_id] = a
    return a
def query_seg_tree_v2(list_seg_tree, q_low, q_high, low, high, node_id):
    # base case 1: data range is totally inside of query range
    if q_low <= low and q_high >= high:
        return list_seg_tree[node_id]
    # base case 2: query range and data range are completely disjoint
    if low > q_high or high < q_low:
        return -1 * float('inf')
    # recursive case: ask left child and right child, and then return the min of both children
    l = query_seg_tree_v2(list_seg_tree, q_low, q_high, low, (low + high) // 2, 2 * node_id + 1)
    r = query_seg_tree_v2(list_seg_tree, q_low, q_high, (low + high) // 2 + 1, high, 2 * node_id + 2)
    return max(l, r)


# In[252]:


list_data = [-1, 2, 4, 0]
list_seg_tree = init_list_seg_tree_v2(list_data)
print(list_seg_tree)
construct_seg_tree_v2(list_data, list_seg_tree, 0, len(list_data) - 1, 0)
print(list_seg_tree)
# query
q_low = 1
q_high = 2
query_seg_tree_v2(list_seg_tree, q_low, q_high, 0, len(list_data)-1, 0)


# ## sum range segment tree

# In[249]:


def init_list_seg_tree_v3(list_data):
    return [0] * ((2 ** math.ceil((math.log(len(list_data), 2) + 1))) - 1)
# step-2: define a function to construct seg tree
def construct_seg_tree_v3(list_data, list_seg_tree, low, high, node_id):
    if low == high:
        list_seg_tree[node_id] = list_data[low]
        return list_seg_tree[node_id]
    left_id = node_id * 2 + 1
    right_id = left_id + 1
    l_low = low
    l_high = (low + high) // 2
    r_low = l_high + 1
    r_high = high
    a = construct_seg_tree_v3(list_data, list_seg_tree, l_low, l_high, left_id) + construct_seg_tree_v3(list_data, list_seg_tree, r_low, r_high, right_id)
    list_seg_tree[node_id] = a
    return a
def query_seg_tree_v3(list_seg_tree, q_low, q_high, low, high, node_id):
    # base case 1: data range is totally inside of query range
    if q_low <= low and q_high >= high:
        return list_seg_tree[node_id]
    # base case 2: query range and data range are completely disjoint
    if low > q_high or high < q_low:
        return 0
    # recursive case: ask left child and right child, and then return the min of both children
    l = query_seg_tree_v3(list_seg_tree, q_low, q_high, low, (low + high) // 2, 2 * node_id + 1)
    r = query_seg_tree_v3(list_seg_tree, q_low, q_high, (low + high) // 2 + 1, high, 2 * node_id + 2)
    return l + r


# In[250]:


list_data = [-1, 2, 4, 0]
list_seg_tree = init_list_seg_tree_v3(list_data)
print(list_seg_tree)
construct_seg_tree_v3(list_data, list_seg_tree, 0, len(list_data) - 1, 0)
print(list_seg_tree)
# query
q_low = 0
q_high = 1
query_seg_tree_v3(list_seg_tree, q_low, q_high, 0, len(list_data)-1, 0)


# ## Dynamic programming

# ### tiling

# In[200]:


memo = {}
def tiling(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
        return 1
    return tiling(n - 1) + tiling(n - 2)
tiling(5)


# Palindrome: A positive integer is said to be a palindrome with respect to base b, if its
# representation in base b reads the same from left to right as from right to left. Palindromes are
# formed as follows:
# Given a number, reverse its digits and add the resulting number to the original number. If
# the result isn't a palindrome, repeat the process. For example, start with 87 base 10.
# Applying this process, we obtain:
# 87 + 78 = 165
# 165 + 561 = 726
# 726 + 627 = 1353
# 1353 + 3531 = 4884, a palindrome
# Whether all numbers eventually become palindromes under this process is unproved, but all base
# 10 numbers less than 10,000 have been tested. Every one becomes a palindrome in a relatively
# small number of steps (of the 900 3-digit numbers, 90 are palindromes to start with and 735 of
# the remainder take fewer than 5 reversals and additions to yield a palindrome). Except, that is,
# for 196. Although no proof exists that it will not produce a palindrome, this number has been
# carried through to produce a 2 million-digit number without producing a palindrome.
# INPUT: 5 sets of data. Each set will consist of a positive integer and its base. Bases will be in
# the range 10 – 16.
# OUTPUT: Print the palindrome produced. If no palindrome is produced after 10 additions, print
# the word “none” and the last sum.
# SAMPLE DATA SAMPLE OUTPUT
# 1. A23, 16 1. D4D # 	
# A345 12
# 2. A345, 12 2. 9B4B9
# 3. 196, 10 3. NONE, 18211171
# Test Data Test Output
# 1. 6A, 16 1. 121
# 2. 5896, 13 2. BB8AA8BB
# 3. 8769, 15 3. 45522554
# 4. 46894, 10 4. NONE, 1317544822
# 5. AAB4, 12 5. 3A88A3

# In[209]:


def to_decimal(n, base):
    dict1 = {'A' : '10', 'B' : '11', 'C' : '12', 'D' : '13', 'E' : '14', 'F' : '15'}
    list1 = list(n)
    length = len(list1)
    sum1 = 0
    for k, x in enumerate(list1[::-1]):
        if x in dict1.keys():
            x = dict1[x]
        sum1 += int(x) * (base ** k)
    return sum1

def from_decimal(n, base):
    dict1 = {'A' : '10', 'B' : '11', 'C' : '12', 'D' : '13', 'E' : '14', 'F' : '15'}
    dict2 = {v:k for k,v in dict1.items()}
    list1 = []
    while n != 0:
        remainder = n % base
        if remainder > 9:
            remainder = dict2[str(remainder)]
        list1.append(str(remainder))
        n = n // base
    return ''.join(list1[::-1])

n = 0
str1 = input()
while n != 10:
    list1 = str1.split(' ')
    a = to_decimal(list1[0], int(list1[1]))
    b = to_decimal(list1[0][::-1], int(list1[1]))
    str2 = str(from_decimal(a + b, int(list1[1])))
    if str2[::-1] == str2:
        break
    str1 = str2 + ' ' + list1[1]
    n += 1
if n == 10:
    print('NONE ' + str2)
else:
    print(str2)


# WRAP AROUND CODE
# This is yet another in a long list of ACSL code programs. You would think we would have run
# out of them by now. In this program you will be given a set of letters to encode. The difference
# here is that different rules are used for different letters and the counting process starts where the
# last letter ends. Using the numerical value of each letter (A=1, B=2, … Z= 26) the rules are as
# follows:
# The number of letters to count is given by:
# RULE 1 Multiply its numerical value by 2
# RULE 2 Divide its numerical value by 3. Multiply the integer
# remainder by 5
# RULE 3 Divide its numerical value by 4. Multiply the integer part of
# the quotient by –8.
# RULE 4 Take the square root of the numerical value. Truncate the
# decimal part of the answer. Multiply the resulting integer by
# –12.
# RULE 5 Find the sum of the factors of its numerical value. Multiply
# by 10.
# For the first letter of each set, if the computed value is non-negative, starting at A count the
# computed value to the right. For each additional letter start at the current encoded letter. If the
# first computed value is negative, starting at A count to the left which means wrapping around to
# the end of the alphabet. For each additional letter start at the current encoded letter. As an
# example, the input C, 1, B, 2, F, 3, $ would produce the encoded letters GQI. The C with a
# numerical value of 3 evaluates to a 6, using rule 1. Always starting each new set at A, and
# counting 6 letters to the right, the C encodes to an G. The B with a numerical value of 2
# evaluates to a 10. Counting down the alphabet 10 letters from G encodes the B to a Q. The F
# with a numerical value of 6 evaluates to a –8, using rule 3. Counting to the left 8 letters from Q
# encodes the F to an I. The final encoded value is GQI.
# INPUT: There will be 5 input lines. Each line will consist of a series of upper case letters each
# followed by a rule number. The line will end with a $. You may enter the letters and numbers
# one at a time. The commas shown are for clarification and do not have to be entered. The $ is not
# encoded.
# OUTPUT: For each input line, print the encoded string it produces.
# SAMPLE INPUT SAMPLE OUTPUT
# 1. C, 1, B,2, F,3, $ 1. GQI
# 2. A,1,A,1,A,1,$ 2. CEG
# 3. A,1,H,2,D,3,$ 3. CME
# 4. T,5,S,4,$ 4. EI
# TEST INPUT TEST OUTPUT
# 1. A,1,B,1,C,1,$ 1. CGM
# 2. A,2,C,4,S,5,L,3,$ 2. FTLN
# 3. C,5, P,4,L,3,U,2,S,1,$ 3. OSUUG
# 4. C,2,H,3,P,4,$ 4. AKO
# 5. M,1,O,2,N,3,T,4,R,5,E,1,A,2,L,3,$ 5. AACGGQVX

# In[211]:


alphabet = 'abcdefghijklmnopqrstuvwxyz'
list1 = list(alphabet)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
dict1 = {}
for k, x in enumerate(list1):
    dict1[x] = list2[k]
dict2 = {v:k for k,v in dict1.items()}
str1 = input()
list1 = str1.split(' ')[:-1]
list1 = [s.strip() for s in list1]
list2 = []
for x in range(0, len(list1), 2):
    list2.append(list1[x : x + 2])
current = 1
str1 = ''
for a in list2:
    if a[1] == '1':
        current = current + dict1[a[0].lower()] * 2
        current = current % 26
        str1 += dict2[current].upper()
    if a[1] == '2':
        current = current + ((dict1[a[0].lower()] % 3) * 5)
        current = current % 26
        str1 += dict2[current].upper()
    if a[1] == '3':
        current = current + ((dict1[a[0].lower()] // 4) * -8)
        current = current % 26
        str1 += dict2[current].upper()
    if a[1] == '4':
        current = current + (int(dict1[a[0].lower()] ** (1/2)) * (-12))
        current = current % 26
        str1 += dict2[current%26].upper()
    if a[1] == '5':
        count = 0
        for x in range(1, int(dict1[a[0].lower()]) + 1):
            if dict1[a[0].lower()] % x == 0:
                count += x
        current = current + (count * 10)
        current = current % 26
        str1 += dict2[current].upper()
print(str1)


# In[179]:


n = int(input())
for x in range(1, n + 1):
    row1 = int(input())
    for a in range(4):
        line = input()
        if a + 1 == row1:
            line = [int(s) for s in line.split(' ')]
            list1 = line
    row2 = int(input())
    for b in range(4):
        line = input()
        if b + 1 == row2:
            line = [int(s) for s in line.split(' ')]
            list2 = line
    count = 0
    number = None
    for c in list1:
        if c in list2:
            number = c
            count += 1
    if count == 1:
        print('Case ' + str(x) + ': ' + str(number))
    elif count > 1:
        print('Case ' + str(x) + ': Bad Magician!')
    else:
        print('Case ' + str(x) + ': Volunteer Cheated!')


# In[10]:


import copy
inf = float('inf')
list1 = [[0, 3, inf, 7], [8, 0, 2, inf], [5, inf, 0, 1], [2, inf, inf, 0]]
def floyd_warshall(list1):
    v = len(list1)
    list2 = copy.deepcopy(list1)
    for a in range(v):
        for start in range(v):
            for end in range(v):
                for mid in range(v):
                    if list1[start][mid] + list1[mid][end] < list2[start][end]:
                        list2[start][end] = list1[start][mid] + list1[mid][end]
        list1 = copy.deepcopy(list2)
    return list2
floyd_warshall(list1)
#[[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]


# Can Shahir even get there?!
# Shahir was already taped shut in the box when it occurred to him that he didn't know if it was possible to get from his
# house to his prom date's. That's no problem: he asks one of the friends that will deliver him, Dhruvit, to check.
# There are houses in Shahir's neighbourhood, and roads that connect those houses. Each road connects two
# houses. All roads can be traveled down both directions. Each house is distinctly numbered and identified by a number in
# the range .
# Shahir lives in house . His date lives in house . Is there a path of roads to follow such that Dhruvit can drive the
# packaged Shahir from house to house ? Dhruvit wrote (and you, vicariously, will write) a program to answer that
# question.
# Input Specification
# The first line will contain four integers, separated by spaces:
# : The number of houses in Shahir's neighbourhood.
# : The number of roads in Shahir's neighbourhood.
# : Shahir lives in house A.
# : Shahir's date lives in house B.
# The next lines contain two space-separated integers and , denoting a road that connects
# house with house . Two roads will never connect the same two houses.
# Output Specification
# On a single line, print GO SHAHIR! if Shahir can make it to his date's house. Otherwise, print NO SHAHIR! .
# Sample Input 1
# 6 7 1 6
# 1 2
# 2 3
# 2 5
# 5 1
# 3 4
# 4 5
# 4 6
# Sample Output 1
# N M N
# 1..N
# A B
# A B
# N (1 ≤ N ≤ 2000)
# M (0 ≤ M ≤ N)
# A (1 ≤ A ≤ N)
# B (1 ≤ B ≤ N)
# M X Y (1 ≤ X, Y ≤ N)
# X Y
# CCC Level 1 W21 Class 14 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the question. Submit a zip
# file named as lastnamefirstnamec15HW contains the solution for each question.
# Page 2 of 2
# GO SHAHIR!
# Explanation for Sample 1
# Here is the graph of Shahir's neighbourhood:
# Shahir's house is house . His date's house is at house . Dhruvit can drive Jeffrey from houses to by following the
# path or .
# Sample Input 2
# 6 6 1 6
# 1 2
# 2 3
# 2 5
# 5 1
# 3 4
# 4 5
# Sample Output 2
# NO SHAHIR!
# Explanation for Sample 2
# This map of Shahir's neighbourhood is the same as the one in Sample 1, but the edge between houses and is
# removed. As a result, Dhruvit can no longer drive Shahir to his date's house.

# In[148]:


line = input()
line = [int(s) for s in line.split(' ')]
houses = line[0]
roads = line[1]
house1 = line[2]
house2 = line[3]
graph = {}
for x in range(roads):
    line = input()
    line = [int(s) for s in line.split(' ')]
    if line[0] not in graph:
        graph[line[0]] = []
    graph[line[0]].append(line[1])
    if line[1] not in graph:
        graph[line[1]] = []
    graph[line[1]].append(line[0])
parents = {}
for a in range(1, houses + 1):
    if a not in graph:
        graph[a] = []
parents[1] = None
start_node = house1
end_node = house2
visited = []
def dfs(node):
    if node not in visited:
        visited.append(node)
        neighbours = graph[node]
        for x in neighbours:
            dfs(x)
dfs(1)
if end_node in visited:
    print('GO SHAHIR!')
else:
    print('NO SHAHIR!')


# In[150]:


n = int(input())
line = input()
list1 = [int(s) for s in line.split(' ')]
a = int(input())
for x in range(a):
    b = int(input())
    minimum = float('inf')
    for x in list1:
        if x >= b and x < minimum:
            minimum = x
    c = list1.count(minimum)
    print(minimum, c)


# There are n SMTP servers connected by network cables. Each of the m cables connects two computers and has a certain latency measured in milliseconds required to send an email message. What is the shortest time required to send a message from server S to server T along a sequence of cables?
# 
# Assume that there is no delay incurred at any of the servers.
# 
# Input
# 
# The first line of input gives the number of cases, N. N test cases follow. Each one starts with a line
# 
# containing n (2 ≤ n ≤ 20000), m (0 ≤ m ≤ 50000), S (0 ≤ S < n) and T (0 ≤ T < n). S ̸= T. The
# 
# next m lines will each contain 3 integers: 2 different servers (in the range [0, n − 1]) that are connected
# 
# by a bidirectional cable and the latency, w, along this cable (0 ≤ w ≤ 10000).
# 
# Output
# 
# For each test case, output the line ‘Case #x:’ followed by the number of milliseconds required to send
# 
# a message from S to T. Print ‘unreachable’ if there is no route from S to T.
# 
# Sample Input
# 
# 3
# 
# 2 1 0 1
# 
# 0 1 100
# 
# 3 3 2 0
# 
# 0 1 100
# 
# 0 2 200
# 
# 1 2 50
# 
# 2 0 0 1
# 
# Sample Output
# 
# Case #1: 100
# 
# Case #2: 150
# 
# Case #3: unreachable

# In[165]:


import copy
def convert_to_matrix(graph):
    list_nodes = sorted(graph.keys())
    list1 = []
    for a in list_nodes:
        list1.append([])
        for b in list_nodes:
            if a == b:
                list1[-1].append(0)
            elif b not in graph[a].keys():
                list1[-1].append(float('inf'))
            else:
                list1[-1].append(graph[a][b])
    return list1

n = int(input())
for x in range(1, n + 1):
    line = input()
    line = [int(s) for s in line.split(' ')]
    num_nodes = line[0]
    num_edges = line[1]
    start_node = line[2]
    end_node = line[3]
    graph = {}
    if num_edges == 0:
        print('Case #' + str(x) + ': unreachable')
        continue
    for a in range(num_edges):
        line = input()
        line = [int(s) for s in line.split(' ')]
        if line[0] not in graph:
            graph[line[0]] = {}
        graph[line[0]][line[1]] = line[2]
        if line[1] not in graph:
            graph[line[1]] = {}
        graph[line[1]][line[0]] = line[2]
    list1 = convert_to_matrix(graph)
    v = len(list1)
    for a in range(v):
        list2 = copy.deepcopy(list1)
        for start_id in range(v):
            for end_id in range(v):
                for mid_id in range(v):
                    if list1[start_id][mid_id] + list1[mid_id][end_id] < list2[start_id][end_id]:
                        list2[start_id][end_id] = list1[start_id][mid_id] + list1[mid_id][end_id]
        list1 = list2
    if list2[start_node][end_node] != float('inf'):
        print('Case #' + str(x) + ': ' + str(list2[start_node][end_node]))
    else:
        print('Case #' + str(x) + ': unreachable')


# Q1) Special Node
# You are given a weighted graph with N nodes and M edges. Some of the nodes are marked
# as special nodes. Your task is to find the shortest pairwise distance between any two
# different special nodes.
# Input
# The first line of the input contains three space-separated integers N, M and K denoting the
# number of nodes, the number of edges, and the number of special nodes.
# The following line contains K space-separated distinct integers A1, A2, ..., AK , denoting the
# special nodes.
# Each of the following M lines (say, the j
# th) contains a triple Xj Yj Zj, denoting the edge
# connecting the nodes Xj and Yj, and having the weight of Zj.
# Output
# Output the shortest pairwise distance between any two different special nodes.
# Constraints
# • 2 ≤ K ≤ N
# • The given graph is connected.
# • The given graph doesn't contain self loops and multiple edges.
# • 1 ≤ Ai ≤ N
# • 1 ≤ Zj ≤ 104
# • 1 ≤ Xj, Yj ≤ N
# Subtasks
# • Subtask #1 (20 points): 2 ≤ N ≤ 300, N-1 ≤ M ≤ N*(N-1)/2, 2 ≤ K ≤ N
# • Subtask #2 (25 points): 2 ≤ N ≤ 105
# , N-1 ≤ M ≤ 105
# , 2 ≤ K ≤ 10
# • Subtask #3 (55 points): 2 ≤ N ≤ 105
# , N-1 ≤ M ≤ 3 * 105
# , 2 ≤ K ≤ 104
# Example
# Input:
# 5 5 3
# 1 3 5
# 1 2 3
# 2 3 4
# 3 4 1
# 4 5 8
# 1 5 19
# Output:
# 7
# Explanation
# Nodes 1, 3 and 5 are special nodes. Shortest distance between nodes 1 and 3 is 7 and that
# between nodes 3 and 5 is 9. Shortest distance between nodes 1 and 5 is 16. Minimum of
# these distances is 7. Hence answer is 7.

# In[ ]:





# In[182]:


import copy
def convert_to_matrix(graph):
    list1 = []
    for a in list_nodes:
        list1.append([])
        for b in list_nodes:
            if a == b:
                list1[-1].append(0)
            elif b not in graph[a].keys():
                list1[-1].append(float('inf'))
            else:
                list1[-1].append(graph[a][b])
    return list1

line = input()
line = [int(s) for s in line.split(' ')]
num_nodes = line[0]
num_edges = line[1]
num_special_nodes = line[2]
line = input()
special = []
for x in [int(s) for s in line.split(' ')]:
    special.append(x)
graph = {}
for x in range(num_edges):
    line = input()
    line = [int(s) for s in line.split(' ')]
    if line[0] not in graph:
        graph[line[0]] = {}
    graph[line[0]][line[1]] = line[2]
list_nodes = []
for a in range(1, num_edges + 1):
    list_nodes.append(a)
for a in list_nodes:
    if a not in graph:
        graph[a] = {}

list1 = convert_to_matrix(graph)
v = len(list1)
for a in range(v):
    list2 = copy.deepcopy(list1)
    for start_id in range(v):
        for end_id in range(v):
            for mid_id in range(v):
                if list1[start_id][mid_id] + list1[mid_id][end_id] < list2[start_id][end_id]:
                    list2[start_id][end_id] = list1[start_id][mid_id] + list1[mid_id][end_id]
    list1 = list2
minimum = float('inf')
for a in special:
    for b in special:
        if a != b:
            if list2[a - 1][b - 1] < minimum:
                minimum = list2[a - 1][b - 1]
            if list2[b - 1][a - 1] < minimum:
                minimum = list2[b - 1][a - 1]
print(minimum)


# Q1) Substring
# How many distinct substrings does a given string S have?
# For example, if S = "abc", S has 7 distinct substrings: {"","a","b","c","ab","bc","abc"}. Note that
# the empty string and S itself are considered substrings of S.
# On the other hand, if S = "aaa", S has only 4 distinct substrings: {"","a","aa","aaa"}.
# The first line of the input file contains N, the number of test cases. For each test case, a line
# follows giving S, a string of from 1 to 1000 alphanumeric characters. Your output consists of one
# line per case, giving the number of distinct substrings of S. Try to write an efficient program.
# Sample Input
# 2
# abc
# aaa
# Output for Sample Input
# 7
# 4

# In[316]:


n = int(input())
for x in range(n):
    str1 = input()
    list1 = list(str1)
    list2 = []
    for k1 in range(len(list1)):
        for k2 in range(len(list1) + 1):
            list2.append(''.join(list1[k1:k2]))
    print(len(list(set(list2))))


# Aromatic Numbers
# This question involves calculating the value of aromatic numbers which are a combination of Arabic
# digits and Roman numerals.
# An aromatic number is of the form ARARAR...AR, where each A is an Arabic digit, and each R is a
# Roman numeral. Each pair ARcontributes a value described below, and by adding or subtracting these
# values together we get the value of the entire aromatic number.
# An Arabic digit A, can be 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9. A Roman numeral R is one of the seven letters I, V,
# X, L, C, D, or M. Each Roman numeral has a base value:
# Symbol I V X L C D M
# Base value 1 5 10 50 100 500 1000
# The value of a pair AR is A times the base value of R. Normally, you add up the values of the pairs to get
# the overall value. However, wherever there are consecutive symbols ARA'R' with R' having a strictly
# bigger base value than R, the value of pair AR must be subtractedfrom the total, instead of being
# added.
# For example, the number 3M1D2C has the value 3×1000 + 1×500 + 2*100 = 3700 and 3X2I4X has the
# value 3×10 - 2×1 + 4×10 = 68.
# Write a program that computes the values of aromatic numbers.
# Input Format
# The input is a valid aromatic number consisting of between 2 and 20 symbols.
# Output Format
# The output is the decimal value of the given aromatic number.
# Sample Input 1
# 3M1D2C
# Sample Output 1
# 3700
# Sample Input 2
# 2I3I2X9V1X
# Sample Output 2
# -16

# In[351]:


str1 = input()
roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000
list1 = list(str1)
count = 0
for k, x in enumerate(list1):
    if k % 2 == 0:
        if k != 0:
            if roman[list1[k - 1]] < roman[list1[k + 1]]:
                count -= 2 * int(list1[k - 2]) * roman[list1[k - 1]]
            count += int(x) * roman[list1[k + 1]]
        else:
            count += int(x) * roman[list1[k + 1]]
print(count)


# In an episode of the Dick Van Dyke show, little Richie connects the freckles on his
# 
# 
# 
# Dad’s back to form a picture of the Liberty Bell. Alas, one of the freckles turns out to
# 
# 
# 
# be a scar, so his Ripley’s engagement falls through.
# 
# 
# 
# Consider Dick’s back to be a plane with freckles at various (x, y) locations. Your job
# 
# 
# 
# is to tell Richie how to connect the dots so as to minimize the amount of ink used.
# 
# 
# 
# Richie connects the dots by drawing straight lines between pairs, possibly lifting the
# 
# 
# 
# pen between lines. When Richie is done there must be a sequence of connected lines
# 
# 
# 
# from any freckle to any other freckle.
# 
# 
# 
# Input
# 
# 
# 
# The input begins with a single positive integer on a line by itself indicating the number
# 
# 
# 
# of test cases, followed by a blank line.
# 
# 
# 
# The first line of each test case contains 0 < n ≤ 100, giving the number of freckles on
# 
# 
# 
# Dick’s back. For each freckle, a line follows; each following line contains two real numbers
# 
# 
# 
# indicating the (x, y) coordinates of the freckle.
# 
# 
# 
# There is a blank line between each two consecutive test cases.
# 
# 
# 
# Output
# 
# 
# 
# For each test case, your program must print a single real number to two decimal places:
# 
# 
# 
# the minimum total length of ink lines that can connect all the freckles. The output of
# 
# 
# 
# each two consecutive cases must be separated by a blank line.
# 
# 
# 
# Sample Input
# 
# 
# 
# 1
# 
# 3
# 
# 1.0 1.0
# 
# 2.0 2.0
# 
# 2.0 4.0
# 
# Sample Output
# 
# 3.41

# In[88]:


def find_root(node):
    x = dict_mapping[node]
    list1 = []
    while x != list_parents[x]:
        list1.append(x)
        x = list_parents[x]
    for y in list1:
        list_parents[y] = x
    return x
def union(node1, node2):
    root1 = find_root(node1)
    root2 = find_root(node2)
    if root1 == root2:
        return [root1, root2]
    elif dict_comp_sizes[root2] > dict_comp_sizes[root1]:
        list_parents[root1] = root2
        dict_comp_sizes[root2] += dict_comp_sizes[root1]
        dict_comp_sizes[root1] = 0
        keep_edges.append((node1, node2))
        return root2
    else:
        list_parents[root2] = root1
        dict_comp_sizes[root1] += dict_comp_sizes[root2]
        dict_comp_sizes[root2] = 0
        keep_edges.append((node1, node2))
        return root1 
def kruskal(graph):
    list1 = []
    for x in graph.keys():
        for y in graph[x].keys():
            list1.append([x, y, graph[x][y]])
    list1 = sorted(list1, key=lambda s:s[2])
    for a in list1:
        if max(dict_comp_sizes.values())==len(list(set(list_nodes))):
            break
        parent = union(a[0], a[1])
    return parent
def distance(x, y):
    return (((y[0] - x[0]) ** 2) + ((y[1] - x[1]) ** 2)) ** (1/2)

test_cases = int(input())
for x in range(test_cases):
    list1 = []
    freckles = int(input())
    for a in range(freckles):
        line = input()
        line = line.split(' ')
        line = [float(s) for s in line]
        line = tuple(line)
        list1.append(line)
    graph = {}
    for a in list1:
        graph[a] = {}
        for b in list1:
            if a != b:
                graph[a][b] = distance(a, b)
start_node = list1[0]
visited = [start_node]
parents = {start_node: None}
total_cost = 0
list_nodes = sorted(graph.keys())
dict_mapping = {}
for k, x in enumerate(list_nodes):
    dict_mapping[x] = k
list_parents = []
for x in range(len(list_nodes)):
    list_parents.append(x)
dict_comp_sizes = {}
for a in list_parents:
    dict_comp_sizes[a] = 1
keep_edges = []
list_nodes = sorted(graph.keys())
dict_mapping = {}
for k, x in enumerate(list_nodes):
    dict_mapping[x] = k
list_parents = []
for x in range(len(list_nodes)):
    list_parents.append(x)
dict_comp_sizes = {}
for a in list_parents:
    dict_comp_sizes[a] = 1
root = kruskal(graph)
dict_mapping_inv = {v:k for k, v in dict_mapping.items()}
parents = {}
root = dict_mapping_inv[root]   
cost = 0
for x in keep_edges:
    cost += graph[x[0]][x[1]]
print(round(cost, 2))


# In[17]:


graph = {(1.0, 1.0): {(2.0, 2.0): 1.4142135623730951, (2.0, 4.0): 3.1622776601683795}, (2.0, 2.0): {(1.0, 1.0): 1.4142135623730951, (2.0, 4.0): 2.0}, (2.0, 4.0): {(1.0, 1.0): 3.1622776601683795, (2.0, 2.0): 2.0}}
[((1.0, 1.0), (2.0, 2.0)), ((2.0, 2.0), (2.0, 4.0))]
start_node = list1[0]
visited = [start_node]
parents = {start_node: None}
total_cost = 0
list_nodes = sorted(graph.keys())
dict_mapping = {}
for k, x in enumerate(list_nodes):
    dict_mapping[x] = k
list_parents = []
for x in range(len(list_nodes)):
    list_parents.append(x)
dict_comp_sizes = {}
for a in list_parents:
    dict_comp_sizes[a] = 1
keep_edges = []
list_nodes = sorted(graph.keys())
dict_mapping = {}
for k, x in enumerate(list_nodes):
    dict_mapping[x] = k
list_parents = []
for x in range(len(list_nodes)):
    list_parents.append(x)
dict_comp_sizes = {}
for a in list_parents:
    dict_comp_sizes[a] = 1
root = kruskal(graph)
dict_mapping_inv = {v:k for k, v in dict_mapping.items()}
parents = {}
root = dict_mapping_inv[root]   
cost = 0
for x in keep_edges:
    cost += graph[x[0]][x[1]]
print(round(cost, 2))


# Q1)Email
# A seldom-known fact about email addresses is that you can format a given address in several
# different ways. In particular:
# • The entire address is case-insensitive.
# • Dots (‘.’) before the at-sign (‘@’) sign are ignored.
# • A plus (‘+’) followed by any string can be added before the at-sign (‘@’). The plus and
# following string are ignored.
# For example, “foo@bar.com” and “fO.o+baz123@bAR.com” refer to the same email address.
# John runs a service where users sign up with their email address. He has noticed that some users have
# signed up multiple times using different representations of the same address. He has asked for your
# help to determine the number of unique email addresses that have signed up on his site.
# Input Specifications
# DATA11.txt (DATA12.txt for the second try) will contain 10 datasets. Each dataset begins with a line
# containing an integer N (1 ≤ N ≤ 100,000), the number of email addresses. The next N lines each
# contain an email address S (1 ≤ |S| ≤ 30). The email address will be formatted as a non-empty user
# part consisting of letters, numbers, dots, and pluses followed by a single at-sign followed by a nonempty domain part consisting of letters, numbers, and dots.
# For the first 6 cases, N ≤ 100.
# Output Specifications
# For each dataset, output the number of unique email addresses in the dataset.
# Sample Input (Two Datasets Shown)
# 3
# foo@bar.com
# fO.o+baz123@bAR.com
# foo@bar..com
# 3
# c++@foo.com
# c...@Foo.com
# .c+c@FOO.COM

# In[2]:


n = int(input())
list1 = []
for x in range(n):
    line = input()
    list1.append(line)
list_all = []
for a in list1:
    list2 = list(a)
    divider = list2.index('@')
    for k, b in enumerate(list2):
        list2[k] = b.lower()
    while list2.index('.') < list2.index('@'):
        index1 = list2.index('.')
        if index1<divider:
            list2.pop(index1)
    list3 = list2
    if '+' in list2:
        index = list2.index('+')
        if index < divider:
            divider = list2.index('@')
            list3 = list2[:index] + list2[divider:]
    list_all.append(''.join(list3))
print(len(list(set(list_all))))


# In[1]:


def from_decimal(n, base):
    dict1 = {'A' : '10', 'B' : '11', 'C' : '12', 'D' : '13', 'E' : '14', 'F' : '15'}
    dict2 = {v:k for k,v in dict1.items()}
    list1 = []
    while n != 0:
        remainder = n % base
        if remainder > 9:
            remainder = dict2[str(remainder)]
        list1.append(str(remainder))
        n = n // base
    return ''.join(list1[::-1])
n = int(input())
list1 = []
for x in range(2, n):
    if from_decimal(n, x) == from_decimal(n, x)[::-1]:
        list1.append(x)
for a in list1:
    print(a, end = ' ')


# In[33]:


list1 = [-2, 4, 2, -1, 7, 5]
list2 = []
for a in range(len(list1)):
    list3 = []
    for b in range(len(list1)):
        if b < a:
            list3.append('Invalid')
        else:
            list3.append(min(list1[a : b + 1]))
    list2.append(list3)
for c in list2:
    print(c)


# In[86]:


def find_root(node):
    x = dict_mapping[node]
    list1 = []
    while x != list_parents[x]:
        list1.append(x)
        x = list_parents[x]
    for y in list1:
        list_parents[y] = x
    return x

def union(node1, node2):
    root1 = find_root(node1)
    root2 = find_root(node2)
    if root1 == root2:
        return [root1, root2]
    elif dict_comp_sizes[root2] > dict_comp_sizes[root1]:
        list_parents[root1] = root2
        dict_comp_sizes[root2] += dict_comp_sizes[root1]
        dict_comp_sizes[root1] = 0
        keep_edges.append((node1, node2))
        return root2
    else:
        list_parents[root2] = root1
        dict_comp_sizes[root1] += dict_comp_sizes[root2]
        dict_comp_sizes[root2] = 0
        keep_edges.append((node1, node2))
        return root1

def kruskal(graph):
    list1 = []
    for x in graph.keys():
        for y in graph[x].keys():
            list1.append([x, y, graph[x][y]])
    list1 = sorted(list1, key=lambda s:s[2])
    for a in list1:
        if max(dict_comp_sizes.values())==len(list(set(list_nodes))):
            break
        parent = union(a[0], a[1])
    return parent    
a = int(input())
for x in range(a):
    line = input()
    line = [int(s) for s in line.split()]
    n = line[0]
    m = line[1]
    l = line[2]
    s = line[3]
    start = int(input())
    graph = {}
    for b in range(m):
        line = input()
        line = [int(s) for s in line.split()]
        if line[0] not in graph:
            graph[line[0]] = {}
        graph[line[0]][line[1]] = line[2] + l
        if line[1] not in graph:
            graph[line[1]] = {}
        graph[line[1]][line[0]] = line[2] + l
    for c in range(len(graph.keys())):
        if c not in graph:
            graph[c] = {}
    list_nodes = sorted(graph.keys())
    dict_mapping = {}
    for k, x in enumerate(list_nodes):
        dict_mapping[x] = k
    list_parents = []
    for x in range(len(list_nodes)):
        list_parents.append(x)
    dict_comp_sizes = {}
    for a in list_parents:
        dict_comp_sizes[a] = 1
    keep_edges = []
    root = kruskal(graph)
    min_cost = 0
    for x in keep_edges:
        min_cost += graph[x[0]][x[1]]
    print(min_cost)


# In[87]:


keep_edges


# In[71]:


1
4 6 10 1
3
1 2 4
1 3 8
1 4 1
2 3 2
2 4 5
3 4 20


# In[ ]:


'1 2 4', '1 3 8', '1 4 1', '2 3 2', '2 4 5', '3 4 20'


# In[ ]:





# In[ ]:





# In[ ]:





# In[158]:


def get_max_util(ss, se, qs, qe, si):
    #        Three Cases to consider
    #        Case 1: If qs and qe are complteley overalap with ss and se
    #        then return the value either segment tree at st[si] or st[se]
    if ss >= qs and se <= qe:
        return list_seg_tree[si]
    #        Case 2: if qs and qe are completely outside then return inf
    if qe < ss or se < qs:
        return -1 * float('inf')
    #        Case 3: Partially overlap
    l_low = ss
    l_high = (ss + se) // 2
    r_low = l_high + 1
    r_high = se
    return max(get_max_util(l_low, l_high, qs, qe, si * 2 + 1), get_min_util(r_low, r_high, qs, qe, si * 2 + 2))
    #        Recurse to the left chold at si and right child at si and 
    #        return the min of those values


# Q1)Highway
# A number of cities are connected by a network of highways. Each highway is bidirectional and connects two cities, with a
# given travel time. What is the shortest time to get from a given city to another given city?
# Input
# The first line of input contains the number of test cases.
# Each test case starts with a line containing the number of cities n (2 ≤ n ≤ 100000), the number of highways m (1 ≤ m ≤
# 100000), the starting city and the ending city. Cities are numbered from 1 to n.
# Then m lines follow, each describing one highway. The description consists of the two distinct city numbers and the time
# in minutes to travel along the highway. The time will be between 1 and 1000.
# Output
# For each test case output a single line containing the minimum time it takes to get from the start to the destination. If no
# connection exists, output NONE.

# In[16]:


def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node
a = int(input())
for x in range(a):
    line = input()
    line = [int(s) for s in line.split()]
    n = line[0]
    m = line[1]
    start = line[2]
    end = line[3]
    graph = {}
    for b in range(m):
        line = input()
        line = list1[b]
        line = [int(s) for s in line.split()]
        if line[0] not in graph:
            graph[line[0]] = {}
        graph[line[0]][line[1]] = line[2]
        if line[1] not in graph:
            graph[line[1]] = {}
        graph[line[1]][line[0]] = line[2]
    for b in range(1, n + 1):
        if b not in graph:
            graph[b] = {}
    list_nodes = sorted(list(graph.keys()))
    costs = {}
    for x in graph.keys():
        if x == start:
            costs[x] = 0
        else:
            costs[x] = float('inf')
    parents = {}
    parents[start] = None
    visited = []
    while True:
        min_node = find_min_node(costs, visited) 
        if min_node == None:
            break
        visited.append(min_node)
        for x in graph[min_node].keys():
            c = costs[min_node] + graph[min_node][x]
            if c < costs[x]:
                costs[x] = c
                parents[x] = min_node
    if costs[end] == float('inf'):
        print('NONE')
    else:
        print(costs[end])


# In[ ]:


2
4 2 1 4
1 2 5
3 4 5
4 4 1 4
1 2 5
2 3 5
3 4 5
4 2 6


# In[43]:


visited = []
def dfs(node):
    if node not in visited:
        visited.append(node)
        neighbours = graph[node]
        for x in neighbours:
            dfs(x)
dfs(0)
print(visited)


# In[42]:


graph = {}
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 3]
graph[3] = [1, 2, 4]
graph[4] = [1, 3]
graph[5] = [6, 7]
graph[6] = [5, 8]
graph[7] = [5, 8]
graph[8] = [6, 7]
print(graph)


# In[91]:


def dfs(graph, node):
    if node not in visited:
        visited.append(node)
        neighbours = graph[node]
        for x in neighbours:
            dfs(graph, x)

line = input()
line = line.split(' ')
n = int(line[0])
m = int(line[1])
graph = {}

for a in range(1, n + 1):
    if a not in graph:
        graph[a] = []
for x in range(m):
    line = input()
    line = line.split(' ')
    graph[int(line[0])].append(int(line[1]))
line = input()
line = line.split(' ')
visited = []
dfs(graph, int(line[0]))
if int(line[1]) in visited:
    print('yes')
else:
    visited = []
    dfs(graph, int(line[1]))
    if int(line[0]) in visited:
        print('no')
    else:
        print('unknown')


# ## Graph algorithms review

# ### dijkstra

# In[77]:


def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node

def dijkstra(start_node, end_node, graph):
    list_nodes = sorted(list(graph.keys()))
    costs = {}
    for x in graph.keys():
        if x == start_node:
            costs[x] = 0
        else:
            costs[x] = float('inf')
    parents = {}
    parents[start_node] = None
    visited = []
    while True:
        min_node = find_min_node(costs, visited) 
        if min_node == None:
            break
        visited.append(min_node)
        for x in graph[min_node].keys():
            c = costs[min_node] + graph[min_node][x]
            if c < costs[x]:
                costs[x] = c
                parents[x] = min_node
    return costs[end_node]

# test case
graph = {}
graph['A'] = {}
graph['A']['B'] = 3
graph['A']['C'] = 6
graph['B'] = {}
graph['B']['C'] = 4
graph['B']['D'] = 4
graph['B']['E'] = 11
graph['C'] = {}
graph['C']['D'] = 8
graph['D'] = {}
graph['D']['E'] = 4
graph['D']['F'] = 5
graph['D']['G'] = 2
graph['E'] = {}
graph['E']['H'] = 9
graph['F'] = {}
graph['F']['H'] = 1
graph['G'] = {}
graph['G']['H'] = 2
graph['H'] = {}
dijkstra('A', 'H', graph)


# ### prim's algorithm

# In[78]:


#prim
def find_min_node(visited):
    min_cost = float('inf')
    min_node = None
    for x in visited:
        for y in graph[x].keys():
            if y not in visited:
                if min_cost > graph[x][y]:
                    min_cost = graph[x][y]
                    min_node = y
                    parent = x
    parents[min_node] = parent
    return min_node, min_cost, parent

def prim(graph, start_node):
    start_node = list(graph.keys())[0]
    visited = [start_node]
    parents = {start_node : None}
    total_cost = 0
    while len(visited) != len(graph.keys()):
        min_node, min_cost, parent = find_min_node(visited)
        if min_node == None:
            break
        visited.append(min_node)
        total_cost += min_cost
    return total_cost

# test
graph = {}
graph['A'] = {}
graph['A']['B'] = 8
graph['A']['C'] = 6
graph['A']['D'] = 5
graph['B'] = {}
graph['B']['A'] = 8
graph['B']['D'] = 4
graph['C'] = {}
graph['C']['A'] = 6
graph['C']['D'] = 3
graph['D'] = {}
graph['D']['A'] = 5
graph['D']['B'] = 4
graph['D']['C'] = 3
prim(graph, 'A')


# ### DFS

# In[79]:


# note: need to define a global list: visited=[]
def dfs(graph, node):
    if node not in visited:
        visited.append(node)
        neighbours = graph[node]
        for x in neighbours:
            dfs(graph, x)

# test
graph = {}
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 3]
graph[3] = [1, 2, 4]
graph[4] = [1, 3]
graph[5] = [6, 7]
graph[6] = [5, 8]
graph[7] = [5, 8]
graph[8] = [6, 7]

visited = []
dfs(graph, 0)
print(visited)


# ### BFS

# In[89]:


def bfs(start_node, end_node, graph):
    visited = []
    paths = []
    paths.append([start_node])
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        if current_node not in visited:
            visited.append(current_node)
            neighbors = graph[current_node]
            for node in neighbors:
                path = current_path + [node]
                if path[-1] == end_node:
                    return path
                else:
                    paths.append(path)
    return None

# test case
graph = {'2': ['1'], '3': ['2'], '1': ['3'], '11': ['10'], '10': ['100'], '100': ['11']}
shortest_path = bfs('1', '2', graph)
print(shortest_path)


# In[ ]:




