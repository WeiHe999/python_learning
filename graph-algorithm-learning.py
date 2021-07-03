#!/usr/bin/env python
# coding: utf-8

# ## depth first search (DFS)

# In[151]:


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


# In[152]:


n = len(graph.keys())
visited = []
def dfs(node):
    if node not in visited:
        visited.append(node)
        neighbours = graph[node]
        for x in neighbours:
            dfs(x)
dfs(0)
print(visited)


# ## count number of components using dfs

# In[4]:


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
n = len(graph.keys())
visited = []
def dfs(node):
    if node not in visited:
        visited.append(node)
        neighbours = graph[node]
        for x in neighbours:
            dfs(x)
list_r = []
for a in graph.keys():
    if a not in visited:
        visited = []
        dfs(a)
        list_r.append(visited)
print(list_r)


# ## Tree

# ### find the height of a tree

# In[1]:


graph = {}
graph[0] = [1, 2]
graph[1] = [3, 4]
graph[2] = []
graph[3] = []
graph[4] = []
def treeheight(node):
    if node == None:
        return -1
    if graph[node] == []:
        return 0
    m = 0
    for x in graph[node]:
        n = treeheight(x)
        if n > m:
            m = n
    return (m + 1)
print(treeheight(0))


# ### rooting a tree

# In[6]:


graph = {}
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 3]
graph[3] = [1, 2, 4]
graph[4] = [1, 3]
graph_2 = {}
for a in graph.keys():
    graph_2[a] = []
root = 0
visited = []
def build_tree(node):
    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            if child not in visited:
                graph_2[node].append(child)
                build_tree(child)
build_tree(root)
print(graph_2)


# ### find the centers of an undirected graph

# In[34]:


graph = {}
graph[0] = [1]
graph[1] = [0, 2, 4]
graph[2] = [1, 3, 5]
graph[3] = [2]
graph[4] = [1, 7]
graph[5] = [2, 6]
graph[6] = [5]
graph[7] = [4]
graph_2 = graph.copy()
while len(graph_2.keys()) >= 3:
    list_cut = []
    for x in graph_2.keys():
        if len(graph_2[x]) == 1:
            list_cut.append(x)
    for c in list_cut:
        del graph_2[c]
    for a in graph_2.keys():
        for b in list_cut:
            if b in graph_2[a]:
                index = graph_2[a].index(b)
                graph_2[a] = graph_2[a][:index] + graph_2[a][index + 1:]
print(graph_2)


# ### identify if two trees are isomorphic

# In[42]:


# check if graph_1 and graph_2 are isomorphic
graph_1 = {}
graph_1[1] = [2, 3]
graph_1[2] = []
graph_1[3] = [4, 5]
graph_1[4] = []
graph_1[5] = []
graph_2 = {}
graph_2[1] = []
graph_2[2] = []
graph_2[3] = [4, 5]
graph_2[4] = [1, 2]
graph_2[5] = []
print(graph_1, graph_2)


# In[57]:


def encode_tree(node, graph):
    if graph[node] == []:
        return '()'
    list1 = []
    for x in graph[node]:
        list1.append(encode_tree(x, graph))
    list1 = sorted(list1, key=lambda x: len(x), reverse = True)
    str1 = '('
    for a in list1:
        str1 += a
    str1 += ')'
    return str1


# In[58]:


list_r1 = []
list_r2 = []
for node in graph_1.keys():
    list_r1.append(encode_tree(node, graph_1))
for node in graph_2.keys():
    list_r2.append(encode_tree(node, graph_2))


# In[59]:


if sorted(list_r1) == sorted(list_r2):
    print('isomorphic')


# ### binary tree

# In[ ]:


'''
Binary Trees in Python: Introduction and Traversal Algorithms
https://www.youtube.com/watch?v=6oL-0TdVy28
insertion and search
https://www.youtube.com/watch?v=yC83Kp2xig8
binary tree: remove a node
https://www.youtube.com/watch?v=YlgPi75hIBc&t=299s
'''


# #### create a binary tree and then print pre-order, in-order, and post-order traversal

# In[ ]:


'''
create a binary tree and then print pre-order, in-order, and post-order traversal
            1
           / \
          2   3
         / \   \
        4  5    6
pre-order(root-left-right): 1-2-4-5-3-6
in-order (left-root-right): 4-2-5-1-3-6
post-order (left-right-root): 4-5-2-6-3-1
'''


# In[95]:


def pre_order(node):
    if graph[node] == [None, None]:
        return [node]
    if graph[node][0] != None:
        left = pre_order(graph[node][0])
    else:
        left = []
    if graph[node][1] != None:
        right = pre_order(graph[node][1])
    else:
        right = []
    return [node] + left + right


# In[96]:


def in_order(node):
    if graph[node] == [None, None]:
        return [node]
    if graph[node][0] != None:
        left = in_order(graph[node][0])
    else:
        left = []
    if graph[node][1] != None:
        right = in_order(graph[node][1])
    else:
        right = []
    return left + [node] + right


# In[97]:


def post_order(node):
    if graph[node] == [None, None]:
        return [node]
    if graph[node][0] != None:
        left = post_order(graph[node][0])
    else:
        left = []
    if graph[node][1] != None:
        right = post_order(graph[node][1])
    else:
        right = []
    return left + right + [node]


# In[98]:


graph = {}
graph[1] = [2, 3]
graph[2] = [4, 5]
graph[3] = [None, 6]
graph[4] = [None, None]
graph[5] = [None, None]
graph[6] = [None, None]
print('Pre-order:', pre_order(1))
print('In-order:', in_order(1))
print('Post-order:', post_order(1))


# #### binary search tree, insert data

# In[209]:


# build a binary search tree using the list below, insert node one by one
list_data = [5, 3, 6, 4, 2, 1, 9, 8]
graph = {}
root = list_data[0]
graph[root] = [None, None]
for insert_data in list_data[1:]:
    done=0
    root = list_data[0]
    while True:
        while insert_data<root:
            if graph[root][0] == None:
                graph[root][0] = insert_data
                graph[insert_data] = [None, None]
                done = 1
                break
            root = graph[root][0]
        while root!=None and insert_data>root:
            if graph[root][1] == None:
                graph[root][1] = insert_data
                graph[insert_data] = [None, None]
                done = 1
                break
            root = graph[root][1]
        if done==1:
            break
print(graph)


# #### binary search tree: find the min and max item

# In[222]:


graph = {5: [3, 6], 3: [2, 4], 6: [None, 9], 4: [None, None], 2: [1, None], 1: [None, None], 9: [8, None], 8: [None, None]}
root = 5
amin = float('inf')
amax = float('-inf')
while True:
    if graph[root][0] == None:
        break
    if graph[root][0] < amin:
        root = graph[root][0]
        amin = root
print(amin)
root = 5
while True:
    if graph[root][1] == None:
        break
    if graph[root][1] > amax:
        root = graph[root][1]
        amax = root
print(amax)


# In[225]:


graph = {5: [3, 6], 3: [2, 4], 6: [None, 9], 4: [None, None], 2: [1, None], 1: [None, None], 9: [8, None], 8: [None, None]}
root = 5
def find_min(node):
    if graph[node][0] == None:
        return node
    return find_min(graph[node][0])
print(find_min(root))
def find_max(node):
    if graph[node][1] == None:
        return node
    return find_max(graph[node][1])
print(find_max(root))


# #### binary search tree: seach for a data item

# In[235]:


graph = {5: [3, 6], 3: [2, 4], 6: [None, 9], 4: [None, None], 2: [1, None], 1: [None, None], 9: [8, None], 8: [None, None]}
find = 8
root = 5
while True:
    if find < root:
        if graph[root][0] == None:
            print('Did not find the element')
            break
        root = graph[root][0]
        continue
    if find > root:
        if graph[root][1] == None:
            print('Did not find the element')
            break
        root = graph[root][1]
        continue
    else:
        print('Found it!')
        break


# #### binary search tree, remove a data item

# In[35]:


def find_min(node):
    if graph[node][0] == None:
        return node
    return find_min(graph[node][0])

def delete_leaf(root, node, graph):
    if graph[node] == [None, None]:
        graph.pop(node)
        index = graph[parents[node]].index(node)
        graph[parents[node]][index] = None
        return graph 
    return "Invalid"

def delete_sigle_child_node(root, node, graph):
    if graph[node][0] == None:
        index = graph[parents[node]].index(node)
        graph[parents[node]][index] = graph[node][1]
        graph.pop(node)
        return graph
    if graph[node][1] == None:
        index = graph[parents[node]].index(node)
        graph[parents[node]][index] = graph[node][0]
        graph.pop(node)
        return graph
    return "Invalid"

def delete_node(root, node, graph):
    if graph[node] == [None, None]:
        return delete_leaf(root, node, graph)
    if graph[node][0] == None or graph[node][1] == None:
        return delete_sigle_child_node(root, node, graph)
    
    # find the min from right sub-tree
    temp = find_min(graph[node][1])
    # deletet the min-node
    if graph[temp] == [None, None]:
        graph = delete_leaf(root, temp, graph)
    else:
        if graph[temp][0] == None or graph[temp][1] == None:
            graph = delete_sigle_child_node(root, temp, graph) 
    # repalce node with min-node
    p = parents[node]
    index = graph[p].index(node)
    graph[p][index] = temp
    graph[temp] = graph[node]
    graph.pop(node)
    
    return graph


# In[36]:


graph = {5: [3, 6], 3: [2, 4], 6: [5.5, 9], 4: [None, None], 2: [1, None], 1: [None, None], 9: [8, None], 8: [None, None], 5.5: [None, None]}
parents = {}
print(graph)
for node in graph.keys():
    list_children = graph[node]
    for child in list_children:
        if child != None:
            if child not in parents:
                parents[child] = node
print(parents)


# In[38]:


graph = delete_node(5, 6, graph)
print(graph)


# ### Lowest Common Ancestor

# In[122]:


graph = {5: [3, 6], 3: [2, 4], 6: [None, 9], 4: [None, None], 2: [1, None], 1: [None, None], 9: [8, None], 8: [None, None]}


# In[132]:


def get_ancestors(node, root):
    list1 = []
    while root != None:
        list1.append(root)
        if node == root:
            return list1[::-1]
        if node < root:
            root = graph[root][0]
        else:
            root = graph[root][1]
    return []

def lca(node1, node2, root):
    list1 = get_ancestors(node1, root)
    list2 = get_ancestors(node2, root)
    if list1 == [] or list2 == []:
        return 'Not in graph'
    print(list1, list2)
    for x in list1:
        if x in list2:
            return x
lca(4, 1, 5)


# ### binary search tree using node
# #### https://www.youtube.com/watch?v=yC83Kp2xig8&t=558s

# In[165]:


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Binary_tree(object):
    def __init__(self):
        self.root = None
        
    def _insert_node(self, node, data):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert_node(node.left, data)
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert_node(node.right, data)
        else:
            print('Already exists')
    def insert_node(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert_node(self.root, data)
            
    def pre_order(self, node):
        if node==None:
            return []
        return [node.data] + self.pre_order(node.left) + self.pre_order(node.right)
    
    def in_order(self, node):
        if node==None:
            return []
        return self.in_order(node.left) + [node.data] + self.in_order(node.right)
    
    def post_order(self, node):
        if node==None:
            return []
        return self.post_order(node.left) + self.post_order(node.right) + [node.data]
    
    def print_tree(self, order):
        if order not in [0, 1, 2]:
            print('order should be 0, 1, or 2')
        else:
            if order==0:
                list_nodes = self.pre_order(self.root)
            elif order==1:
                list_nodes = self.in_order(self.root) 
            else:
                list_nodes = self.post_order(self.root) 
            list_nodes = [str(s) for s in list_nodes]
            print('-'.join(list_nodes))
    def find(self, data):
        root = self.root
        while root != None:
            if data == root.data:
                print(True)
                break
            elif data < root.data:
                root = root.left
            else:
                root = root.right
        if root == None:   
            print(False)
    def height(self):
        root = self.root
        print(self._height(root))
    def _height(self, node):
        if node == None:
            return 0
        else:
            return max(self._height(node.left), self._height(node.right)) + 1
    def height2(self, root):
        if root == None:
            return 0
        else:
            return max(self.height2(root.left), self.height2(root.right)) + 1
    def depth(self, data):
        count = 0
        root = self.root
        while root != None:
            if root.data == data:
                return count
            elif root.data > data:
                root = root.left
            else:
                root = root.right
            count += 1
        return -1
    def depth2(self, data, root, count=0):
        if root.data == data:
            return count
        elif root.data > data:
            return self.depth2(data, root.left, count + 1)
        else:
            return self.depth2(data, root.right, count + 1)
    def max_value(self, node):
        if node.right == None:
            return node.data
        else:
            return self.max_value(node.right)
bst_tree = Binary_tree()
bst_tree.insert_node(5)
bst_tree.insert_node(3)
bst_tree.insert_node(8)
bst_tree.insert_node(2)
bst_tree.insert_node(1)
bst_tree.insert_node(9)
bst_tree.insert_node(6)
bst_tree.print_tree(0)
bst_tree.print_tree(1)
bst_tree.print_tree(2)
bst_tree.find(6)
bst_tree.find(-1)
bst_tree.height()
print(bst_tree.height2(bst_tree.root))
print(bst_tree.depth(6))
print(bst_tree.depth2(8, bst_tree.root))
print(bst_tree.max_value(bst_tree.root))


# ### heap

# In[ ]:


'''
heap animation
https://www.youtube.com/watch?v=AE5I0xACpZs
heap series
https://www.youtube.com/watch?v=WCm3TqScBM8&list=PLSVu1-lON6Lwqj5nDqg8YyD7f4tjLMMBN
heap using python library
https://www.youtube.com/watch?v=3Z8QDJynDgo
'''


# In[39]:


import heapq


# ## topological sort

# In[221]:


"""
https://www.youtube.com/watch?v=eL-KzMXSXXI&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=15
"""


# In[237]:


graph = {'A' : ['D'], 'B' : ['D'], 'C' : ['A', 'B'], 'D' : [], 'E' : ['A', 'D']}
list_nodes = graph.keys()


# In[238]:


def dfs(start_node):
    if start_node not in visited:
        visited.append(start_node)
        for x in graph[start_node]:
            dfs(x)


# In[242]:


visited2 = []
for node in list_nodes:
    if node not in visited2:
        visited = []
        dfs(node)
        for s in visited:
            if s not in visited2:
                visited2.append(s)
print(visited2)


# ## shortest path to all nodes using topological sort

# In[14]:


def dfs(start_node):
    if start_node not in visited:
        visited.append(start_node)
        for x in graph[start_node].keys():
            dfs(x)

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

visited2 = []
list_nodes = graph.keys()
for node in list_nodes:
    if node not in visited2:
        visited = []
        dfs(node)
        for s in visited:
            if s not in visited2:
                visited2.append(s)
print(visited2)


# In[15]:


start_node = 'A'
costs = {}
for x in graph.keys():
    if x == start_node:
        costs[x] = 0
    else:
        costs[x] = float('inf')
for node in visited2:
    neighbours = graph[node].keys()
    for a in neighbours:
        c = costs[node] + graph[node][a]
        if c < costs[a]:
            costs[a] = c
print(costs)


# ## longest path

# In[250]:


def dfs(start_node):
    if start_node not in visited:
        visited.append(start_node)
        for x in graph[start_node].keys():
            dfs(x)

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
graph['D']['E'] = -4
graph['D']['F'] = 5
graph['D']['G'] = 2
graph['E'] = {}
graph['E']['H'] = 9
graph['F'] = {}
graph['F']['H'] = 1
graph['G'] = {}
graph['G']['H'] = 2
graph['H'] = {}

visited2 = []
for node in list_nodes:
    if node not in visited2:
        visited = []
        dfs(node)
        for s in visited:
            if s not in visited2:
                visited2.append(s)
print(visited2)

start_node = 'A'
costs = {}
for x in graph.keys():
    if x == start_node:
        costs[x] = 0
    else:
        costs[x] = float('inf')
for node in visited2:
    neighbours = graph[node].keys()
    for a in neighbours:
        c = costs[node] - graph[node][a]
        if c < costs[a]:
            costs[a] = c
for b in costs.keys():
    costs[b] *= -1
print(costs)


# ## Dijkstra's algorithm

# In[269]:


def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node

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

start_node = 'A'

costs = {}
for x in graph.keys():
    if x == start_node:
        costs[x] = 0
    else:
        costs[x] = float('inf')

parents = {}
parents[start_node] = None

visited = []


# In[271]:


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


# ## strongly connected component for undirected graph using DFS

# In[26]:


graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'D']
graph['D'] = ['B', 'C']
graph['E'] = ['F']
graph['F'] = ['E']


# In[322]:


# find strongly connected components
# expected output: list_output = [['A', 'B', 'C', 'D'], ['E', 'F']]


# In[28]:


def dfs(start_node):
    if start_node not in visited2:
        visited2.append(start_node)
        for x in graph[start_node]:
            dfs(x)

list1 = []
visited1 = []
for x in graph.keys():
    if x not in visited1:
        visited2 = []
        dfs(x)
        for a in visited2:
            visited1.append(a)
        list1.append(visited2)
print(list1)


# ## strongly connected component for directed graph using Tarjan algorithm

# In[32]:


graph = {}
graph[0] = [1]
graph[1] = [2]
graph[2] = [0]
graph[3] = [4, 7]
graph[4] = [5]
graph[5] = [0, 6]
graph[6] = [0, 2, 4]
graph[7] = [3, 5]


# In[38]:


def dfs1(start_node):
    if start_node not in visited2:
        visited2.append(start_node)
        for x in graph[start_node]:
            dfs1(x)
        list1 = []
        for a in graph[start_node]:
            if a not in visited1:
                list1.append(lowlink[a])
        lowlink[start_node] = min(list1 + [lowlink[start_node]])

visited1 = []
lowlink = {}
for k in graph.keys():
    lowlink[k] = k
for x in graph.keys():
    if x not in visited1:
        visited2 = []
        dfs1(x)
        for a in visited2:
            visited1.append(a)
print(lowlink)


# In[39]:


lowlinks = lowlink.values()
list1 = []
for x in lowlinks:
    if x not in list1:
        list1.append(x)
print(len(list1))


# In[45]:


dict1 = {}
for a in list1:
    dict1[a] = []
    for x in lowlink.keys():
        if lowlink[x] == a:
            dict1[a].append(x)
print(dict1)


# ## Eulerian path

# In[68]:


graph = {}
graph[0] = []
graph[1] = [2, 3]
graph[2] = [2, 4, 4]
graph[3] = [1, 2, 5]
graph[4] = [3, 6]
graph[5] = [6]
graph[6] = [3]


# In[69]:


def count_in_out_degrees(graph):
    dict_in = {}
    dict_out = {}
    for x in graph.keys():
        dict_in[x] = []
        dict_out[x] = []
        for a in graph[x]:
            dict_out[x].append(a)
    for x in dict_out:
        for a in dict_out[x]:
            dict_in[a].append(x)
    for b in graph.keys():
        dict_in[b] = len(dict_in[b])
        dict_out[b] = len(dict_out[b])
    return dict_in, dict_out
dict_in, dict_out = count_in_out_degrees(graph)
print(dict_in)
print(dict_out)


# In[70]:


def get_dict_diff(graph):
    dict_diff = {}
    dict_in, dict_out = count_in_out_degrees(graph)
    for x in graph.keys():
        dict_diff[x] = dict_in[x] - dict_out[x]
    return dict_diff

def eulerian_path_exist(graph):
    dict_diff = get_dict_diff(graph)
    count1 = 0
    count2 = 0
    for x in dict_diff.keys():
        if dict_diff[x] < -1 or dict_diff[x] > 1:
            return False
        if dict_diff[x] == 1:
            count1 += 1
        if dict_diff[x] == -1:
            count2 += 1
    if count1 > 1 or count2 > 1:
        return False
    return True
eulerian_path_exist(graph)


# In[71]:


def find_eulerian_path_start_node(graph):
    dict_diff = get_dict_diff(graph)
    boolean = eulerian_path_exist(graph)
    if boolean == True:
        if dict_diff.values() == ([0] * len(dict_diff.values())):
            return dict_diff.keys[0]
        else:
            for x in dict_diff.keys():
                if dict_diff[x] == -1:
                    return x
    return 'Eulerian Path does not exist.'
find_eulerian_path_start_node(graph)


# In[72]:


def get_all_links(graph):
    dict_links = {}
    for x in graph.keys():
        dict_links[x] = {}
        for y in graph.keys():
            count = 0
            for a in graph[x]:
                if a == y:
                    count += 1
            dict_links[x][y] = count
    return dict_links
dict_links = get_all_links(graph)
print(dict_links)


# In[73]:


def select_unvisited_link(graph, start_node, dict_links):
    for a in dict_links[start_node].keys():
        if dict_links[start_node][a] > 0:
            return a
    return None
print(select_unvisited_link(graph, 2, dict_links))


# In[170]:


'''
def count_in_out_degrees(graph)
def eulerian_path_exist(graph)
def find_eulerian_path_start_node(graph)
def find_eulerian_path(graph)
def get_all_links(graph)
def select_unvisited_link(graph, start_node)
'''


# In[74]:


def dfs3(start_node):
    while dict_out[start_node] > 0:
        dict_out[start_node] = dict_out[start_node] - 1
        neighbour_node = select_unvisited_link(graph, start_node, dict_links)
        if neighbour_node != None:
            dict_links[start_node][neighbour_node] -= 1
            dfs3(neighbour_node)
    visited2.insert(0, start_node)


# ### Find Eulerian path from a graph

# In[75]:


# step 1: check if Enlerian path exist
if eulerian_path_exist(graph) != True:
    print('There is no Eulerian Path.')
else:
    start_node = find_eulerian_path_start_node(graph)
    dict_in, dict_out = count_in_out_degrees(graph)
    dict_links = get_all_links(graph)
    visited2 = []
    dfs3(start_node)
    print(visited2)


# ## Minimum spanning tree (Prim's algorithm)
# 
# https://www.youtube.com/watch?v=MaaSoZUEoos&t=42s

# In[8]:


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

start_node = 'A'
visited = [start_node]
parents = {'A': None}
total_cost = 0

while len(visited) != len(graph.keys()):
    min_node, min_cost, parent = find_min_node(visited)
    if min_node == None:
        break
    visited.append(min_node)
    total_cost += min_cost
print(total_cost)
print(parents)


# ## Max flow using the Ford-Fulkerson algorithm
# 
# https://downey.io/blog/max-flow-ford-fulkerson-algorithm-explanation/
# https://www.youtube.com/watch?v=LdOnanfc5TM&t=625s

# In[41]:


graph = {}
graph['s'] = {}
graph['s']['0'] = 10
graph['s']['1'] = 10
graph['0'] = {}
graph['0']['2'] = 25
graph['1'] = {}
graph['1']['3'] = 15
graph['2'] = {}
graph['2']['t'] = 10
graph['3'] = {}
graph['3']['t'] = 10
graph['3']['0'] = 6
graph['t'] = {}
graph_res = graph.copy()


# In[42]:


import copy
graph = {}
graph['s'] = {}
graph['s']['A'] = 3
graph['s']['B'] = 2
graph['A'] = {}
graph['A']['B'] = 5
graph['A']['t'] = 2
graph['B'] = {}
graph['B']['t'] = 3
graph['t'] = {}
graph_res = copy.deepcopy(graph)


# In[43]:


def dfs1(start_node):
    if start_node not in visited1:
        visited1.append(start_node)
        for x in graph_res[start_node]:
            if graph_res[start_node][x] > 0:
                dfs1(x)
            
# find the bottle neck for a path
def find_bottleneck_for_path(graph_res, path):
    min_value = float('inf')
    node = 's'
    index = path.index(node)
    while path[index + 1] != 't':
        value = graph_res[node][path[index + 1]]
        if value < min_value:
            min_value = value
        node = path[index + 1]
        index = path.index(node)
    return min_value # a float

# constuct residual graph
def update_res_graph(graph_res, path, bottleneck):
    for k, x in enumerate(path):
        if x == 't':
            break
        graph_res[x][path[k + 1]] = graph_res[x][path[k + 1]] - bottleneck
    path1 = path[::-1]
    for k, x in enumerate(path1):
        if x == 's':
            continue
        if x in graph_res:
            if path1[k + 1] in graph_res[x]:
                graph_res[x][path1[k + 1]] = graph_res[x][path1[k + 1]] + bottleneck
            else:
                graph_res[x][path1[k + 1]] = bottleneck
        else:
            graph_res[x][path1[k + 1]] = bottleneck
    return graph_res


# In[44]:


get_ipython().run_cell_magic('time', '', "# find the path from s to t using dfs\nstart_node = 's'\nwhile True:\n    visited1 = []\n    dfs1(start_node)\n    if 't' not in visited1:\n        break\n    index = visited1.index('t')\n    visited1 = visited1[:index + 1]\n    bottleneck = find_bottleneck_for_path(graph_res, visited1)\n    graph_res = update_res_graph(graph_res, visited1, bottleneck)\nprint(graph)\nprint(graph_res)")


# In[241]:


dict_flow = {}
for x in graph.keys():
    dict_flow[x] = {}
    for y in graph[x].keys():
        difference = graph[x][y] - graph_res[x][y]
        dict_flow[x][y] = difference
print(dict_flow)
count = 0
for a in dict_flow['s'].keys():
    count += dict_flow['s'][a]
print('Max Flow is', count)


# ## Max flow using the capacity scaling algorithm
# 

# In[53]:


graph = {}
graph['s'] = {}
graph['s']['0'] = 10
graph['s']['1'] = 10
graph['0'] = {}
graph['0']['2'] = 25
graph['1'] = {}
graph['1']['3'] = 15
graph['2'] = {}
graph['2']['t'] = 10
graph['3'] = {}
graph['3']['t'] = 10
graph['3']['0'] = 6
graph['t'] = {}
graph_res = graph.copy()


# In[54]:


import copy
graph = {}
graph['s'] = {}
graph['s']['A'] = 3
graph['s']['B'] = 2
graph['A'] = {}
graph['A']['B'] = 5
graph['A']['t'] = 2
graph['B'] = {}
graph['B']['t'] = 3
graph['t'] = {}
graph_res = copy.deepcopy(graph)


# In[55]:


def dfs2(start_node):
    if start_node not in visited1:
        visited1.append(start_node)
        for x in graph_res[start_node]:
            if graph_res[start_node][x] > minimum:
                dfs1(x)
            
# find the bottle neck for a path
def find_bottleneck_for_path(graph_res, path):
    min_value = float('inf')
    node = 's'
    index = path.index(node)
    while path[index + 1] != 't':
        value = graph_res[node][path[index + 1]]
        if value < min_value:
            min_value = value
        node = path[index + 1]
        index = path.index(node)
    return min_value # a float

# constuct residual graph
def update_res_graph(graph_res, path, bottleneck):
    for k, x in enumerate(path):
        if x == 't':
            break
        graph_res[x][path[k + 1]] = graph_res[x][path[k + 1]] - bottleneck
    path1 = path[::-1]
    for k, x in enumerate(path1):
        if x == 's':
            continue
        if x in graph_res:
            if path1[k + 1] in graph_res[x]:
                graph_res[x][path1[k + 1]] = graph_res[x][path1[k + 1]] + bottleneck
            else:
                graph_res[x][path1[k + 1]] = bottleneck
        else:
            graph_res[x][path1[k + 1]] = bottleneck
    return graph_res

def find_max_link_cap(graph_res):
    maximum_cap = 0
    for x in graph_res.keys():
        for y in graph_res[x]:
            if graph_res[x][y] > maximum_cap:
                maximum_cap = graph_res[x][y]
    return maximum_cap


# In[56]:


start_node = 's'
max_value = find_max_link_cap(graph_res)
minimum = 1
while minimum * 2 <= max_value:
    minimum *= 2
while True:
    visited1 = []
    dfs2(start_node)
    if 't' not in visited1:
        if minimum == 1:
            break
        minimum = minimum / 2
        continue
    index = visited1.index('t')
    visited1 = visited1[:index + 1]
    bottleneck = find_bottleneck_for_path(graph_res, visited1)
    graph_res = update_res_graph(graph_res, visited1, bottleneck)
print(graph)
print(graph_res)


# In[57]:


dict_flow = {}
for x in graph.keys():
    dict_flow[x] = {}
    for y in graph[x].keys():
        difference = graph[x][y] - graph_res[x][y]
        dict_flow[x][y] = difference
count = 0
for a in dict_flow['s'].keys():
    count += dict_flow['s'][a]
print('Max Flow is', count)


# ## Max flow using Edmonds-Karp Algorithm

# In[32]:


graph = {}
graph['s'] = {}
graph['s']['0'] = 10
graph['s']['1'] = 10
graph['0'] = {}
graph['0']['2'] = 25
graph['1'] = {}
graph['1']['3'] = 15
graph['2'] = {}
graph['2']['t'] = 10
graph['3'] = {}
graph['3']['t'] = 10
graph['3']['0'] = 6
graph['t'] = {}
graph_res = graph.copy()


# In[33]:


import copy
graph = {}
graph['s'] = {}
graph['s']['A'] = 3
graph['s']['B'] = 2
graph['A'] = {}
graph['A']['B'] = 5
graph['A']['t'] = 2
graph['B'] = {}
graph['B']['t'] = 3
graph['t'] = {}
graph_res = copy.deepcopy(graph)


# In[34]:


def bfs(graph_res, start_node):
    visited1 = []
    visited1.append(start_node)
    paths = [[start_node]]
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        for x in graph_res[current_node]:
            if graph_res[current_node][x]>0:
                if x not in visited1:
                    if x == 't':
                        return current_path + [x]
                    visited1.append(x)
                    paths.append(current_path + [x])
    return None
# find the bottle neck for a path
def find_bottleneck_for_path(graph_res, path):
    min_value = float('inf')
    node = 's'
    index = path.index(node)
    while path[index + 1] != 't':
        value = graph_res[node][path[index + 1]]
        if value < min_value:
            min_value = value
        node = path[index + 1]
        index = path.index(node)
    return min_value # a float

# constuct residual graph
def update_res_graph(graph_res, path, bottleneck):
    for k, x in enumerate(path):
        if x == 't':
            break
        graph_res[x][path[k + 1]] = graph_res[x][path[k + 1]] - bottleneck
    path1 = path[::-1]
    for k, x in enumerate(path1):
        if x == 's':
            continue
        if x in graph_res:
            if path1[k + 1] in graph_res[x]:
                graph_res[x][path1[k + 1]] = graph_res[x][path1[k + 1]] + bottleneck
            else:
                graph_res[x][path1[k + 1]] = bottleneck
        else:
            graph_res[x][path1[k + 1]] = bottleneck
    return graph_res


# In[35]:


get_ipython().run_cell_magic('time', '', "# find the path from s to t using dfs\nstart_node = 's'\nwhile True:\n    path = bfs(graph_res, start_node)\n    if path==None:\n        break\n    print(path)\n    bottleneck = find_bottleneck_for_path(graph_res, path)\n    graph_res = update_res_graph(graph_res, path, bottleneck)\nprint(graph)\nprint(graph_res)")


# In[31]:


dict_flow = {}
for x in graph.keys():
    dict_flow[x] = {}
    for y in graph[x].keys():
        difference = graph[x][y] - graph_res[x][y]
        dict_flow[x][y] = difference
count = 0
for a in dict_flow['s'].keys():
    count += dict_flow['s'][a]
print('Max Flow is', count)


# ## max flow using Dicnic algorithm

# In[124]:


import copy
graph = {}
graph['s'] = {}
graph['s']['A'] = 3
graph['s']['B'] = 2
graph['A'] = {}
graph['A']['B'] = 5
graph['A']['C'] = 4
graph['A']['t'] = 2
graph['B'] = {}
graph['B']['t'] = 3
graph['C'] = {}
graph['C']['t'] = 6
graph['t'] = {}
graph_res = copy.deepcopy(graph)


# In[126]:


def find_level_graph(graph_res):
    levels = {'s' : 0, 't' : float('inf')}
    visited = []
    paths = [['s']]
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        if current_node not in visited:
            visited.append(current_node)
            if current_node != 's':
                levels[current_node] = levels[current_path[-2]] + 1
            for x in graph_res[current_node].keys():
                if graph_res[current_node][x] > 0:
                    if x != 't':
                        paths.append(current_path + [x])
                    else:
                        if levels[current_node] + 1 < levels['t']:
                            levels['t'] = levels[current_node] + 1
                            print(levels['t'])
                        if len(levels.keys()) == len(graph_res.keys()):
                            return levels
    return None
find_level_graph(graph_res)


# In[ ]:





# In[ ]:





# In[ ]:





# ## breadth first search (BFS)

# In[58]:


graph = {}
graph['s'] = {}
graph['s']['Tom'] = 7
graph['s']['Jerry'] = 7
graph['s']['Mike'] = 7
graph['s']['Jack'] = 7
graph['Tom'] = {}
graph['Tom']['A'] = 1
graph['Tom']['B'] = 1
graph['Tom']['D'] = 1
graph['Jerry'] = {}
graph['Jerry']['B'] = 1
graph['Jerry']['C'] = 1
graph['Jerry']['D'] = 1
graph['Mike'] = {}
graph['Mike']['A'] = 1
graph['Mike']['C'] = 1
graph['Mike']['E'] = 1
graph['Jack'] = {}
graph['Jack']['C'] = 1
graph['Jack']['D'] = 1
graph['Jack']['E'] = 1
graph['A'] = {}
graph['B'] = {}
graph['C'] = {}
graph['D'] = {}
graph['E'] = {}
graph['A']['t'] = 1
graph['B']['t'] = 2
graph['C']['t'] = 2
graph['D']['t'] = 1
graph['E']['t'] = 1
graph['t'] = {}


# In[59]:


def bfs_all(graph, start_node, end_node):
    visited = []
    paths = [[start_node]]
    list_r = []
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        if current_node not in visited:
            visited.append(current_node)
            for x in graph[current_node].keys():
                if graph[current_node][x] > 0:
                    if x == end_node:
                        list_r.append(current_path + [x])
                        visited = []
                    else:
                        paths.append(current_path + [x])
    return list_r


# In[60]:


bfs_all(graph, start_node, end_node)


# In[61]:


def bfs_single(graph, start_node, end_node):
    paths = [[start_node]]
    visited = []
    while len(paths)>0:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        if current_node not in visited:
            visited.append(current_node)
        for node in graph[current_node].keys():
            if node=='t':
                return current_path+[node]
            else:
                paths.append(current_path+[node]) 
    return []


# In[62]:


def bfs(graph, start_node):
    visited = []
    visited.append(start_node)
    paths = [[start_node]]
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        for x in graph[current_node]:
            if x not in visited:
                visited.append(x)
                paths.append(current_path+[x])
    return visited


# In[63]:


single_results = bfs_single(graph, start_node, end_node)
print(single_results)


# In[65]:


bfs(graph, start_node)


# In[66]:


bfs_all(graph, 's', 't')


# ## Unweighted Bipartite Matching using Edmonds-Karp Algorithm

# In[69]:


'''
Four students named Tom, Jerry, Mike, Jack to borrow books from library 
which has 6 books named A (1), B (2), C (2), D (1), E (1) 
(integer in bracket represents the number of copies for the book).
Tom is interested in books A, B, D,
Jerry is interested in books B, C, and D
Mike is interested in books A, C, E,
Jack is interested in books C, D, E
What is the maximum number of books that can be borrowed by the 4 students from library?
'''


# In[35]:


import copy
graph = {}
graph['s'] = {}
graph['s']['Tom'] = 7
graph['s']['Jerry'] = 7
graph['s']['Mike'] = 7
graph['s']['Jack'] = 7
graph['Tom'] = {}
graph['Tom']['A'] = 1
graph['Tom']['B'] = 1
graph['Tom']['D'] = 1
graph['Jerry'] = {}
graph['Jerry']['B'] = 1
graph['Jerry']['C'] = 1
graph['Jerry']['D'] = 1
graph['Mike'] = {}
graph['Mike']['A'] = 1
graph['Mike']['C'] = 1
graph['Mike']['E'] = 1
graph['Jack'] = {}
graph['Jack']['C'] = 1
graph['Jack']['D'] = 1
graph['Jack']['E'] = 1
graph['A'] = {}
graph['B'] = {}
graph['C'] = {}
graph['D'] = {}
graph['E'] = {}
graph['A']['t'] = 1
graph['B']['t'] = 2
graph['C']['t'] = 2
graph['D']['t'] = 1
graph['E']['t'] = 1
graph['t'] = {}
graph_res = copy.deepcopy(graph)
print(graph)


# In[36]:


def bfs(graph_res, start_node):
    visited1 = []
    visited1.append(start_node)
    paths = [[start_node]]
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        for x in graph_res[current_node]:
            if graph_res[current_node][x]>0:
                if x not in visited1:
                    if x == 't':
                        return current_path + [x]
                    visited1.append(x)
                    paths.append(current_path + [x])
    return None
# find the bottle neck for a path
def find_bottleneck_for_path(graph_res, path):
    min_value = float('inf')
    node = 's'
    index = path.index(node)
    while path[index + 1] != 't':
        value = graph_res[node][path[index + 1]]
        if value < min_value:
            min_value = value
        node = path[index + 1]
        index = path.index(node)
    return min_value # a float

# constuct residual graph
def update_res_graph(graph_res, path, bottleneck):
    for k, x in enumerate(path):
        if x == 't':
            break
        graph_res[x][path[k + 1]] = graph_res[x][path[k + 1]] - bottleneck
    path1 = path[::-1]
    for k, x in enumerate(path1):
        if x == 's':
            continue
        if x in graph_res:
            if path1[k + 1] in graph_res[x]:
                graph_res[x][path1[k + 1]] = graph_res[x][path1[k + 1]] + bottleneck
            else:
                graph_res[x][path1[k + 1]] = bottleneck
        else:
            graph_res[x][path1[k + 1]] = bottleneck
    return graph_res


# In[37]:


start_node = 's'
paths = []
while True:
    path = bfs(graph_res, start_node)
    if path==None:
        break
    paths.append(path)
    bottleneck = find_bottleneck_for_path(graph_res, path)
    graph_res = update_res_graph(graph_res, path, bottleneck)
for x in paths:
    print(x[1] + ' borrowed book ' + x[2] + '!')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Link list

# In[ ]:


'''
Introduction to Linked Lists (Data Structures & Algorithms #5)
https://www.youtube.com/watch?v=WwfhLC16bis
Python: Linked Lists (fast)
https://www.youtube.com/watch?v=Ast5sKQXxEU
'''


# In[43]:


class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
class Linklist(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def add(self, d):
        node = Node(d, self.root)
        self.root = node
        self.size += 1
    def print_linklist(self):
        node = self.root
        while node != None:
            print(node.data)
            node = node.next_node
linklist = Linklist()
list1 = [2, 4, 7, 1]
for x in list1[::-1]:
    linklist.add(x)
linklist.print_linklist()


# In[ ]:


# remove node with value=7


# In[58]:


class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
class Linklist(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def add(self, d):
        node = Node(d, self.root)
        self.root = node
        self.size += 1
    def print_linklist(self):
        node = self.root
        str1 = ''
        while node != None:
            str1 += str(node.data)
            str1 += ' '
            node = node.next_node
        print(str1)
    def remove_node(self, find_node):
        node = self.root
        if node.data == find_node:
            self.root = node.next_node
        else:
            while node.next_node != None:
                if node.next_node.data == find_node:
                    node.next_node = node.next_node.next_node
                    break
                node = node.next_node
    def insert_node(self, insert_data, index):
        node = self.root
        new_node = Node(insert_data)
        if index == node.data:
            old_root = self.root
            self.root = new_node
            new_node.next_node = old_root
        else:
            while node.next_node != None:
                if index == node.next_node.data:
                    old_node = node.next_node
                    node.next_node = new_node
                    new_node.next_node = old_node
                    break
                node = node.next_node
linklist = Linklist()
list1 = [2, 4, 7, 1]
for x in list1[::-1]:
    linklist.add(x)
linklist.print_linklist()
linklist.remove_node(1)
linklist.insert_node(1, 4)
linklist.print_linklist()


# In[84]:


def merge(result, left, right):
    index1 = 0
    index2 = 0
    while index1 < len(left) and index2 < len(right):
        a = left[index1]
        b = right[index2]
        if a < b:
            result.append(a)
            index1 += 1
        else:
            result.append(b)
            index2 += 1
    if index1 == len(left):
        for x in right[index2:]:
            result.append(x)
    else:
        for x in left[index1:]:
            result.append(x)
    return result
result = []
left = [1,5,7,9]
right = [-1,2,8,16]
result = merge(result, left, right)
print(result)


# In[83]:


def mergesort(list1):
    if len(list1) >= 2:
        result = []
        left = list1[:(len(list1)//2)]
        right = list1[(len(list1)//2):]
        mergesort(left)
        mergesort(right)
        merge(result, left, right)
        return result
    else:
        return list1
list1 = [5,4,3,2,1]
a=mergesort(list1)
print(a)


# Professors lead very busy lives with full schedules of work and appointments. Professor P likes to nap during the day, but his schedule is so busy that he doesn’t have many chances to do so.
# 
# He really wants to take one nap every day, however. Naturally, he wants to take the longest nap possible given his schedule. Write a program to help him with the task.
# 
# Input
# 
# The input consists of an arbitrary number of test cases, where each test case represents one day. The first line of each case contains a positive integer s ≤ 100, representing the number
# 
# of scheduled appointments for that day. The next s lines contain the appointments in the format time1 time2 appointment, where time1 represents the time which the appointment starts and time2 the time it ends. All times will be in the hh:mm format; the ending time will always be strictly after the starting time, and separated by a single space.
# 
# All times will be greater than or equal to 10:00 and less than or equal to 18:00. Thus your response must be in this interval as well; i.e., no nap can start before 10:00 and last after 18:00.
# 
# The appointment can be any sequence of characters, but will always be on the same line. You can assume that no line is be longer than 255 characters, that 10 ≤ hh ≤ 18 and that 0 ≤ mm < 60. You cannot assume, however, that the input will be in any specific order, and must read the input until you reach the end of file.
# 
# Output
# 
# For each test case, you must print the following line:
# 
# Day #d: the longest nap starts at hh : mm and will last for [H hours and] M minutes. where d stands for the number of the test case (starting from 1) and hh : mm is the time when the nap can start. To display the length of the nap, follow these rules:
# 
# 1. If the total time X is less than 60 minutes, just print “X minutes.”
# 
# 2. If the total duration X is at least 60 minutes, print “H hours and M minutes,”
# 
# where
# 
# H = X ÷ 60 (integer division, of course) and M = X mod 60. You don’t have to worry about correct pluralization; i.e., you must print “1 minutes” or “1 hours” if that is the case. The duration of the nap is calculated by the difference between the ending time and the beginning time. That is, if an appointment ends at 14:00 and the next one starts at 14:47, then you have 14:47 – 14:00 = 47 minutes of possible napping.
# 
# If there is more than one longest nap with the same duration, print the earliest one. You can assume the professor won’t be busy all day, so there is always time for at least one possible nap.
# 
# Sample Input
# 
# 4
# 
# 10:00 12:00 Lectures
# 
# 12:00 13:00 Lunch, like always.
# 
# 13:00 15:00 Boring lectures...
# 
# 15:30 17:45 Reading
# 
# 4
# 
# 10:00 12:00 Lectures
# 
# 12:00 13:00 Lunch, just lunch.
# 
# 13:00 15:00 Lectures, lectures... oh, no!
# 
# 16:45 17:45 Reading (to be or not to be?)
# 
# 4
# 
# 10:00 12:00 Lectures, as everyday.
# 
# 12:00 13:00 Lunch, again!!!
# 
# 13:00 15:00 Lectures, more lectures!
# 
# 15:30 17:15 Reading (I love reading, but should I schedule it?)
# 
# 1
# 
# 12:00 13:00 I love lunch! Have you ever noticed it? smile
# 
# Sample Output
# 
# Day #1: the longest nap starts at 15:00 and will last for 30 minutes.
# 
# Day #2: the longest nap starts at 15:00 and will last for 1 hours and 45 minutes.
# 
# Day #3: the longest nap starts at 17:15 and will last for 45 minutes.
# 
# Day #4: the longest nap starts at 13:00 and will last for 5 hours and 0 minutes.

# In[97]:


def find_interval(str1, str2):
    list1 = str1.split(':')
    list2 = str2.split(':')
    first_total = (int(list1[0]) * 60) + int(list1[1])
    second_total = (int(list2[0]) * 60) + int(list2[1])
    total = second_total - first_total
    return total
find_interval('10:45', '17:56')


# In[111]:


def find_interval(str1, str2):
    list1 = str1.split(':')
    list2 = str2.split(':')
    first_total = (int(list1[0]) * 60) + int(list1[1])
    second_total = (int(list2[0]) * 60) + int(list2[1])
    total = second_total - first_total
    return total
find_interval('10:45', '17:56')
for x in range(4):
    num = x + 1
    n = int(input())
    list1 = []
    naptime = []
    for a in range(n):
        line = input()
        line = line.split()
        list1.append(line)
        if a == 0:
            if line[0] != '10:00':
                interval = find_interval('10:00', line[0])
                naptime.append([interval, '10:00'])
        if a == (n - 1):
            if line[1] != '18:00':
                interval = find_interval(line[1], '18:00')
                naptime.append([interval, line[1]])
    for k, b in enumerate(list1):
        if k != len(list1) - 1:
            if b[1] != list1[k + 1][0]:
                interval = find_interval(b[1], list1[k + 1][0])
                naptime.append([interval, b[1]])
    choose_list = [c[0] for c in naptime]
    choose = int(max(choose_list))
    for d in naptime:
        if d[0] == choose:
            start = d[1]
            break
    hours = choose // 60
    minutes = choose % 60
    if hours == 0:
        print('Day #' + str(num) + ':' + ' the longest nap starts at ' + str(start) + ' and will last for ' + str(minutes) + ' minutes.')
    else:
        print('Day #' + str(num) + ':' + ' the longest nap starts at ' + str(start) + ' and will last for ' + str(hours) + ' hours and ' + str(minutes) + ' minutes.')


# FatalEagle is playing with blocks with each with a distinct number on them. He is trying to learn how to sort the blocks in ascending order with bubble sort. He would like you to show him the steps to sort his blocks.
# 
# 
# 
# Input Specification
# 
# The first line will have the integer .
# 
# The next line have integers, each separated with a space.
# 
# Output Specification
# 
# Print the initial block sequence, then after each time bubble sort swaps two elements, print the current block sequence.
# 
# Sample Input 1
# 
# 2
# 
# 2 1
# 
# Sample Output 2
# 
# 2 1
# 
# 1 2
# 
# Sample Input 2
# 
# 6
# 
# 9 1 2 6 4 7
# 
# Sample Output 2
# 
# 9 1 2 6 4 7
# 
# 1 9 2 6 4 7
# 
# 1 2 9 6 4 7
# 
# 1 2 6 9 4 7
# 
# 1 2 6 4 9 7
# 
# 1 2 6 4 7 9
# 
# 1 2 4 6 7 9

# In[1]:


n = int(input())
line = input()
list1 = [int(s) for s in line.split()]
str1 = ''
for a in list1:
    str1 += str(a)
    str1 += ' '
print(str1)
for x in range(len(list1)):
    for y in range(0, len(list1) - 1 - x): 
        if list1[y] > list1[y + 1]: 
            temp = list1[y]
            list1[y] = list1[y + 1]
            list1[y + 1] = temp
            str1 = ''
            for a in list1:
                str1 += str(a)
                str1 += ' '
            print(str1)


# In[120]:


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Binary_tree(object):
    def __init__(self):
        self.root = None
        
    def _insert_node(self, node, data):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert_node(node.left, data)
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert_node(node.right, data)
        else:
            print('Already exists')
    def insert_node(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert_node(self.root, data)
            
    def pre_order(self, node):
        if node==None:
            return []
        return [node.data] + self.pre_order(node.left) + self.pre_order(node.right)
    
    def in_order(self, node):
        if node==None:
            return []
        return self.in_order(node.left) + [node.data] + self.in_order(node.right)
    
    def post_order(self, node):
        if node==None:
            return []
        return self.post_order(node.left) + self.post_order(node.right) + [node.data]
    
    def print_tree(self, order):
        if order not in [0, 1, 2]:
            print('order should be 0, 1, or 2')
        else:
            if order==0:
                list_nodes = self.pre_order(self.root)
            elif order==1:
                list_nodes = self.in_order(self.root) 
            else:
                list_nodes = self.post_order(self.root) 
            list_nodes = [str(s) for s in list_nodes]
            print('-'.join(list_nodes))
    def find(self, data):
        root = self.root
        while root != None:
            if data == root.data:
                print(True)
                break
            elif data < root.data:
                root = root.left
            else:
                root = root.right
        if root == None:   
            print(False)
    def height(self):
        root = self.root
        print(self._height(root))
    def _height(self, node):
        if node == None:
            return 0
        else:
            return max(self._height(node.left), self._height(node.right)) + 1
bst_tree = Binary_tree()
bst_tree.insert_node(5)
bst_tree.insert_node(3)
bst_tree.insert_node(8)
bst_tree.insert_node(2)
bst_tree.insert_node(1)
bst_tree.insert_node(9)
bst_tree.insert_node(6)
bst_tree.print_tree(0)
bst_tree.print_tree(1)
bst_tree.print_tree(2)
bst_tree.find(6)
bst_tree.find(-1)
bst_tree.height()


# Pinball Ranking
# Pinball is an arcade game in which an individual player controls a silver ball by means of flippers, with the
# objective of accumulating as many points as possible. At the end of each game, the player's score and rank
# are displayed. The score, an integer between 0 and 1 000 000 000, is that achieved by the player in the
# game just ended. The rank is displayed as "r of n". n is the total number of games ever played on the
# machine, and r is the position of the score for the just-ended game within this set.
# More precisely, r is one greater than the number of games whose score exceeds that of the game just
# ended.
# Input
# You are to implement the pinball machine's ranking algorithm. The first line of input contains a positive
# integer, t, the total number of games played in the lifetime of the machine. t lines follow, given the scores of
# these games, in chronological order.
# Output
# You are to output the average of the ranks (rounded to two digits after the decimal) that would be displayed
# on the board.
# At least one test case will have t ≤ 100. All test cases will have t ≤ 100 000.
# Sample Input
# 5
# 100
# 200
# 150
# 170
# 50
# Sample Output
# 2.20
# Explanation
# The pinball screen would display (in turn):
# 1 of 1
# 1 of 2
# 2 of 3
# 2 of 4
# 5 of 5
# The average rank is (1+1+2+2+5)/5 = 2.20.

# In[57]:


n = int(input())
list1 = []
count = 0
for x in range(n):
    a = int(input())
    list1.append(a)
    list1 = sorted(list1)
    index = list1[::-1].index(a)
    count += (index + 1)
rank = count / n
if len(str(rank)) < 4:
    str1 = str(rank)
    add = 4 - len(str1)
    for b in range(add):
        str1 += '0'
    print(str1)
else:
    print(round(rank, 2))


# Roy has a stack of student yearbook photos. He wants to lay the pictures on a flat surface edge-to-edge to form a filled
# rectangle with minimum perimeter. All photos must be fully visible. Each picture is a square with dimensions 1 unit by 1
# unit.
# For example, he would place 12 photos in the following configuration, where each photo is indicated with an X .
# XXXX
# XXXX
# XXXX
# Of course, he could orient them in the other direction, such as
# XXX
# XXX
# XXX
# XXX
# which would have the same perimeter, 14 units.
# Your program should repeatedly read a positive integer , the number of pictures to be laid out. For each input, it
# should print the smallest possible perimeter for a filled rectangle that is formed by laying all the pictures edge-to-edge.
# Also print the dimensions of this rectangle.
# You may assume that there are less than photos. An input value of indicates that the program should
# terminate.
# Sample Input
# 100
# 15
# 195
# 0
# Sample Output
# Minimum perimeter is 40 with dimensions 10 x 10
# Minimum perimeter is 16 with dimensions 3 x 5
# Minimum perimeter is 56 with dimensions 13 x 15

# In[189]:


def find_factors(n):
    list1 = []
    for x in range(1, n + 1):
        if n % x == 0:
            list1.append(x)
    if n == (int(n ** (1 / 2)) ** 2):
        list1.append(int(n ** (1 / 2)))
    return sorted(list1)
a = int(input())
list1 = []
while a != 0:
    list1.append(a)
    a = int(input())
list1 = [100, 15, 195]
for x in list1:
    list2 = find_factors(x)
    index = (len(list2) // 2) - 1
    perimeter = 2 * (list2[index] + list2[index + 1])
    print('Minimum perimeter is ' + str(perimeter) + ' with dimensions ' + str(list2[index]) + ' x ' + str(list2[index + 1]))


# In the early days of computing, instructions had to be "punched" onto rectangular cards, one instruction per card. This
# card deck was then fed into a card reader so the program could be read and executed. Students put elastic bands
# around their card deck, and, often, carried their cards in a box for fear that they would become rearranged, and thus,
# their program would be incorrect.
# Poor Bill though... he left his cards right near a window and the wind blew his neat deck of cards all over the place, and
# thus his program is out of order! Bill decides to pick up the cards in some random order and then execute the program.
# Write a program to read and execute the commands in Bill's "new" program.
# Input Specification
# The programming language that Bill is using has only two variables ( and ) and seven different types of instructions.
# Initially, the variables and contain the value .
# There is one instruction per line. An instruction is an integer in the range , possibly followed by a variable name,
# which in turn is possibly followed by either a number or a variable.
# In all instructions below, the variable or may refer to either or . The specific instructions are:
# 1 X n means set the variable to the integer value ;
# 2 X means output the value of variable to the screen;
# 3 X Y means calculate and store the value in variable ;
# 4 X Y means calculate and store the value in variable ;
# 5 X Y means calculate and store the value in variable ;
# 6 X Y means calculate the quotient of and store the value in variable as an integer, discarding the
# remainder.
# 7 means stop execution of this program.
# You may assume that all division instructions do not cause a division by zero, and that all other operations (including
# instruction 1) do not cause the computed/stored value to be larger than or smaller than .
# (To clarify division of negative numbers, and both have quotient and has quotient .)
# Output Specification
# Your program should output the value of the indicated variables, one integer per line, until the "stop" instruction has
# been read in, at which time your program should stop execution.
# Sample Input
# 1 A 3
# 1 B 4
# 2 B
# 2 A
# 3 A B
# 2 A
# 5 A A
# 2 A
# 2 B
# 7
# Sample Output
# 4
# 3
# 7
# 0
# 4

# In[220]:


a = input()
list1 = []
while a != '7':
    list1.append(a.split(' '))
    a = input()
dict_var = {}
for x in list1:
    if x[0] == '1':
        dict_var[x[1]] = int(x[2])
        continue
    if x[0] == '2':
        print(dict_var[x[1]])
        continue
    if x[0] == '3':
        dict_var[x[1]] = dict_var[x[1]] + dict_var[x[2]]
    if x[0] == '4':
        dict_var[x[1]] = dict_var[x[1]] * dict_var[x[2]]
    if x[0] == '5':
        dict_var[x[1]] = dict_var[x[1]] - dict_var[x[2]]
    if x[0] == '6':
        dict_var[x[1]] = dict_var[x[1]] // dict_var[x[2]]


# In[272]:


dict_var = {}
for x in list1:
    if x[0] == '1':
        dict_var[x[1]] = int(x[2])
        continue
    if x[0] == '2':
        print(dict_var[x[1]])
        continue
    if x[0] == '3':
        dict_var[x[1]] = dict_var[x[1]] + dict_var[x[2]]
    if x[0] == '4':
        dict_var[x[1]] = dict_var[x[1]] * dict_var[x[2]]
    if x[0] == '5':
        dict_var[x[1]] = dict_var[x[1]] - dict_var[x[2]]
    if x[0] == '6':
        dict_var[x[1]] = dict_var[x[1]] // dict_var[x[2]]


# In[203]:


class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 

class LinkedList: 
    def __init__(self): 
        self.root = None

    def print_list(self):
        node = self.root
        while node != None:
            print(node.data, end = ' ')
            node = node.next
        print('')
        
    def add(self, data):
        new_node = Node(data)
        connect = self.root
        self.root = new_node
        self.root.next = connect

    def index(self, data):
        node = self.root
        index = 0
        test = 0
        while node != None:
            if data == node.data:
                print('Index of ' + str(node.data) + ' is ' + str(index) + '.')
                test = 1
                break
            index += 1
            node = node.next
        if test == 0:
            print('Node does not exist.')
            
    def add_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            root = self.root
            self.root = new_node
            new_node.next = root
        else:
            count = 0
            node = self.root
            while count != index - 1:
                count += 1
                node = node.next
            temp = node.next
            node.next = new_node
            new_node.next = temp
            
    def remove(self):
        self.root = self.root.next
        
    def remove_index(self, index):
        node = self.root
        count = 0
        if index == 0:
            self.root = node.next
        else:
            while node.next != None:
                if count == index:
                    break
                count += 1
                if count != 1:
                    node = node.next
            if node.next != None:
                node.next = node.next.next
            else:
                print('Error')
            
                
list1 = LinkedList() 
list1.root = Node(10)
list1.root.next = Node(20)
list1.root.next.next = Node(30)
list1.add(0)
list1.print_list()
list1.index(20)
list1.add_index(2, 40)
list1.print_list()
list1.remove_index(2)
list1.print_list()
list1.index(40)
list1.remove()
list1.print_list()


# CCC Level 1 W21 Class 6 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec6HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname6HW with the source code for each one of the problems.
# Huffman Encoding
# There is an ingenious text-compression algorithm called Huffman coding, designed by David Huffman in
# 1952.
# The basic idea is that each character is associated with a binary sequence (i.e., a sequence of 0s and
# 1s). These binary sequences satisfy the prefix-free property: a binary sequence for one character is never
# a prefix of another character's binary sequence.
# It is worth noting that to construct a prefix-free binary sequence, simply put the characters as the leaves
# of a binary tree, and label the "left" edge as 0 and the "right" edge as 1. The path from the root to a leaf
# node forms the code for the character at that leaf node. For example, the following binary tree constructs
# a prefix-free binary sequence for the characters {A, B, C, D, E}:
# That is, A is encoded as 00, B is encoded as 01, C is encoded as 10, D is encoded 110 and E is encoded
# as 111.
# The benefit of a set of codes having the prefix-free property is that any sequence of these codes can be
# uniquely decoded into the original characters.
# Your task is to read a Huffman code (i.e., a set of characters and associated binary sequences) along
# with a binary sequence, and decode the binary sequence to its character representation.
# Input
# The first line of input will be an integer k (1 ≤ k ≤ 20), representing the number of characters and
# associated codes. The next k lines each contain a single character, followed by a space, followed by the
# binary sequence (of length at most 10) representing the associated code of that character. You may
# assume that the character is an alphabet character (i.e., 'a'...'z' and 'A'..'Z'). You may assume that the
# sequence of binary codes has the prefix-free property. On the (k + 2)th line is the binary sequence which 
# CCC Level 1 W21 Class 6 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec6HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname6HW with the source code for each one of the problems.
# is to be decoded. You may assume the binary sequence contains codes associated with the given
# characters, and that the (k + 2)th line contains no more than 250 binary digits.
# Output
# On one line, output the characters that correspond to the given binary sequence.
# Sample Input
# 5
# A 00
# B 01
# C 10
# D 110
# E 111
# 00000101111
# Sample Output
# AABBE

# In[ ]:


n = int(input())
dict1 = {}
for x in range(n):
    line = input()
    line = line.split(' ')
    dict1[line[0]] = line[1]
decoding = input()
list1 = []
while decoding != '':
    for a in dict1.keys():
        if dict1[a] == decoding[:len(dict1[a])]:
            list1.append(a)
            decoding = decoding[len(dict1[a]):]
for b in list1:
    print(b, end = '')


# Nowadays, almost any item can be bought and sold on the internet. The problem is shipping. Before an
# item can be sent, it must be carefully packaged in a cardboard box to protect it.
# While items come in many shapes and sizes, finding a box just the right size can be a problem. If the box
# is too small, the item will not fit. If the box is unnecessarily big, shipping cost will be higher, and the item is
# more likely to move around inside the box, and it may break.
# Cardboard box manufacturers offer a fixed set of standard box sizes. Your task is to find the standard box
# size with the smallest volume into which an item will fit.
# Each box is a rectangular prism with a given length, width, and height. Each item is also a rectangular
# prism with a given length, width, and height. An item may be rotated by multiples of 90 degrees in any
# direction before being packed into a box, but when it is packed, its faces must be parallel to the faces of
# the box. An item will fit into a box as long as its dimensions are equal to or less than the dimensions of
# the box.
# Input
# The first line of input will contain a single integer n; 0 < n < 1000, the number of different sizes of boxes
# available. The next n lines will contain three integers each, giving the length, width, and height of a box.
# The following line will contain a single integer m; 0 < m < 1000, the number of items to be packaged.
# The next m lines will contain three integers each, giving the length, width, and height of an item. All
# dimensions will be in millimetres and in the range from 1 mm to 2000 mm.
# Output
# Output is to consist of m lines, one for each item in the input. For each item, output a line containing a
# single integer, the volume (in mm³) of the smallest box into which the item will fit. The same size of box
# may be reused for any number of items. If an item does not fit in any box, print the line: Item does not
# fit. (with a period!)
# Sample Input
# 3
# 1 2 3
# 2 3 4
# 3 4 5
# 5
# 1 1 1
# 2 2 2
# 4 3 2
# 4 3 3
# 4 4 4
# CCC Level 1 W20 Class 7 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec7HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname7HW with the source code for each one of the problems.
# Sample Output
# 6
# 24
# 24
# 60
# Item does not fit.

# In[204]:


num_boxes = int(input())
boxes = []
for x in range(num_boxes):
    a = input()
    boxes.append(a.split(' '))
num_items = int(input())
items = []
for y in range(num_items):
    a = input()
    items.append(a.split(' '))
for x in items:
    options = []
    x = [int(s) for s in x]
    for a in boxes:
        a = [int(s) for s in a]
        list1 = sorted(x)
        list2 = sorted(a)
        count = 0
        for k, b in enumerate(list1):
            if b <= list2[k]:
                count += 1
        if count == 3:
            options.append(a)
    minimum = float('inf')
    if options == []:
        print('Item does not fit.')
        break
    for c in options:
        list1 = sorted(c)
        product = 1
        for d in list1:
            product *= d
        if product < minimum:
            minimum = product
    print(minimum)


# In[234]:


boxes = [['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
items = [['1', '1', '1'], ['2', '2', '2'], ['4', '3', '2'], ['4', '3', '3'], ['4', '4', '4']]
for x in items:
    options = []
    x = [int(s) for s in x]
    for a in boxes:
        a = [int(s) for s in a]
        list1 = sorted(x)
        list2 = sorted(a)
        count = 0
        for k, b in enumerate(list1):
            if b <= list2[k]:
                count += 1
        if count == 3:
            options.append(a)
    minimum = float('inf')
    if options == []:
        print('Item does not fit.')
        break
    for c in options:
        list1 = sorted(c)
        product = 1
        for d in list1:
            product *= d
        if product < minimum:
            minimum = product
    print(minimum)


# Jerseys
# A school team is trying to assign jerseys numbered 1, 2, 3, …, J to student athletes. The size of each
# jersey is either small (S), medium (M) or large (L).
# Each athlete has requested a specific jersey number and a preferred size. The athletes will not be
# satisfied with a jersey that is the wrong number or that is smaller than their preferred size. They will be
# satisfied with a jersey that is their preferred size or larger as long as it is the right number. Two students
# cannot be given the same jersey.
# Your task is to determine the maximum number of requests that can be satisfied.
# Input
# The first line of input is the integer J which is the number of jerseys.
# The second line of input is the integer A which is the number of athletes.
# The next J lines are each the characters S, M or L. Line j gives the size of jersey j (1 ≤ j ≤ J).
# The last A lines are each the character S, M or L followed by a space followed by an integer. Line a (1
# ≤ a ≤ A) gives the requested size and jersey number for athlete a where the athletes are numbered 1, 2,
# 3, …, A.
# For 50% of the test cases, 1 ≤ J ≤ 103 and 1 ≤ A ≤ 103
# .
# For the remaining 50% of the test cases, 1 ≤ J ≤ 106 and 1 ≤ A ≤ 106
# .
# Output
# The output will consist of a single integer which is the maximum number of requests that can be satisfied.
# Sample Input
# 4
# 3
# M
# S
# S
# L
# CCC Level 1 W20 Class 7 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec7HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname7HW with the source code for each one of the problems.
# L 3
# S 3
# L 1
# Sample Output
# 1
# Explanation
# Jersey 1 cannot be assigned because it is medium and athlete

# In[239]:


num_jerseys = int(input())
num_athletes = int(input())
jerseys = [None]
wants = []
for x in range(num_jerseys):
    a = input()
    jerseys.append(a)
for x in range(num_athletes):
    a = input()
    a = a.split(' ')
    wants.append(a)
visited = []
count = 0
for x in wants:
    want = []
    if x[0] == 'S':
        want = [jerseys[int(x[1])], x[1]]
        if want not in visited:
            visited.append(want)
            count += 1
    elif x[0] == 'M':
        if jerseys[int(x[1])] == 'M' or jerseys[int(x[1])] == 'L':
            want = [jerseys[x[1]], x[1]]
            if want not in visited:
                visited.append(want)
                count += 1
    else:
        if jerseys[int(x[1])] == 'L':
            want = [jerseys[int(x[1])], x[1]]
            if want not in visited:
                visited.append(want)
                count += 1
print(count)


# You are given a weighted undirected graph. The vertices are enumerated from 1 to n. Your task is to find
# the shortest path between vertex 1 and vertex n.
# Input
# The first line contains two integers n and m (2 ≤ n ≤ 105, 0 ≤ m ≤ 105), where n is the number of vertices
# and m is the number of edges.
# Following m lines contain one edge each in form ai,bi and wi (1≤ai,bi≤n,1≤wi≤106), where ai, bi are edge
# endpoints and wi is the length of the edge.
# It is possible that the graph has loops and multiple edges between pair of vertices.
# Output
# Write the only integer -1 in case of no path. Write the shortest path in opposite case. If there are many
# solutions, print any of them.
# Sample Inputs
# 5 6
# 1 2 2
# 2 5 5
# 2 3 4
# 1 4 1
# 4 3 3
# 3 5 1
# 5 6
# 1 2 2
# 2 5 5
# 2 3 4
# 1 4 1
# 4 3 3 
# CCC Level 1 W21 Class 8 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec8HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname8HW with the source code for each one of the problems.
# 3 5 1
# Sample Outputs
# 1 4 3 5
# 1 4 3 5

# In[4]:


def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node

graph = {1: {2: 2, 4: 1}, 2: {5: 5, 3: 4}, 4: {3: 3}, 3: {5: 1}, 5: {}}
costs = {}
for x in graph.keys():
    if x == 1:
        costs[x] = 0
    else:
        costs[x] = float('inf')

parents = {}
start_node = 1
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
list1 = []
parent = n
list1.append(n)
while parents[parent] != None:
    parent = parents[parent]
    list1.append(parent)
for x in list1[::-1]:
    print(x, end = ' ')


# In an episode of the Dick Van Dyke show, little Richie connects the freckles on his Dad’s back to form a picture of the Liberty Bell. Alas, one of the freckles turns out to be a scar, so his Ripley’s engagement falls through.
# 
# Consider Dick’s back to be a plane with freckles at various (x, y) locations. Your job is to tell Richie how to connect the dots so as to minimize the amount of ink used. Richie connects the dots by drawing straight lines between pairs, possibly lifting the pen between lines. When Richie is done there must be a sequence of connected lines from any freckle to any other freckle.
# 
# Input
# 
# The input begins with a single positive integer on a line by itself indicating the numberm of test cases, followed by a blank line.
# 
# The first line of each test case contains 0 < n ≤ 100, giving the number of freckles on Dick’s back. For each freckle, a line follows; each following line contains two real numbers
# 
# indicating the (x, y) coordinates of the freckle. There is a blank line between each two consecutive test cases.
# 
# Output
# 
# For each test case, your program must print a single real number to two decimal places: the minimum total length of ink lines that can connect all the freckles. The output of each two consecutive cases must be separated by a blank line.
# 
# Sample Input
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

# In[2]:


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

    while len(visited) != len(graph.keys()):
        min_node, min_cost, parent = find_min_node(visited)
        if min_node == None:
            break
        visited.append(min_node)
        total_cost += min_cost
    print(round(total_cost, 2))


# Q1)Nature Reserve
# In a Nature Reserve and Wildlife Park, there are N environmental monitoring stations to monitor
# temperature, atmospheric pressure, humidity, fire, water quality, etc. Each station, labeled from 1 to N,
# uses solar panels to supply energy for its operations. There is a communication network consisting of
# several two-way communication channels between pairs of stations. All stations are connected via this
# communication network.
# To process data at each station, the Nature Reserve and Wildlife Park needs to install a Smart Data
# Analysis program (with the size of L bytes) to all environmental monitoring stations. The program is
# initially installed directly to S stations, then broadcast to and installed in all other stations via the
# communication network.
# To save energy, all communication channels are initially in an idle state and need to be activated to send
# information. It takes Eij energy units to activate the communication channel between station i and
# station j. Once a channel is activated, it takes one energy unit to transmit one byte via this channel.
# Your task is to determine the minimum energy units required to send the Smart Data Analysis program
# to all stations from the initial S stations.
# Input
# The input consists of several datasets. The first line of the input contains the number of datasets, which
# is a positive number and is not greater than 20. The following lines describe the datasets.
# Each dataset is described by the following lines:
# The first line contains four positive integers: the number of environmental monitoring stations N, the
# number of two-way communication channels M, the size of the program L (in bytes), and the number of
# initial stations S. The constraints are 1≤S≤N≤104, 1≤M≤106, M≤N(N−1)/2, and 1≤L≤106.
# The second line contains S positive integer representing the initial S stations.
# Each of the following M lines contains three positive integers i,j and Eij to denote that there is a two-way
# communicataion channel between station i and station j, and it takes Eij energy units to activate this
# channel (Eij≤106).
# CCC Level 1 W21 Class 9 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec9HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname9HW with the source code for each one of the problems.
# Output
# For each data set, output the minimum energy units required to send the Smart Data Analysis program
# to all stations from the initial S stations.
# Sample Input 1
# 1
# 4 6 10 1
# 3
# 1 2 4
# 1 3 8
# 1 4 1
# 2 3 2
# 2 4 5
# 3 4 20
# Sample Output 1
# 37

# In[1]:


def find_min_node(visited):
    min_cost = float('inf')
    min_node = None
    parent = None
    for x in visited:
        for y in graph[x].keys():
            if y not in visited:
                if min_cost > graph[x][y]:
                    min_cost = graph[x][y]
                    min_node = y
                    parent = x
    parents[min_node] = parent
    return min_node, min_cost, parent

n = int(input())
line = input()
line = [int(s) for s in line.split(' ')]
num_nodes = line[0]
num_edges = line[1]
add_bytes = line[2]
num_start_nodes = line[3]
start_node = input()
graph = {}
for x in range(num_edges):
    line = input()
    line = line.split(' ')
    if line[0] not in graph:
        graph[line[0]] = {}
    graph[line[0]][line[1]] = (int(line[2]) + add_bytes)
    if line[1] not in graph:
        graph[line[1]] = {}
    graph[line[1]][line[0]] = (int(line[2]) + add_bytes)
for y in range(1, num_nodes + 1):
    if str(y) not in graph:
        graph[str(y)] = {}
visited = [start_node]
parents = {start_node: None}
total_cost = 0

while len(visited) != len(graph.keys()):
    min_node, min_cost, parent = find_min_node(visited)
    if min_node == None:
        break
    visited.append(min_node)
    total_cost += min_cost
print(total_cost)


# In[18]:


def find_min_node(visited):
    min_cost = float('inf')
    min_node = None
    parent = None
    for x in visited:
        for y in graph[x].keys():
            if y not in visited:
                if min_cost > graph[x][y]:
                    min_cost = graph[x][y]
                    min_node = y
                    parent = x
    parents[min_node] = parent
    return min_node, min_cost, parent

graph = {'1': {'2': 14, '3': 18, '4': 11}, '2': {'1': 14, '3': 12, '4': 15},
         '3': {'1': 18, '2': 12, '4': 30}, '4': {'1': 11, '2': 15, '3': 30}}
start_node = '3'
visited = [start_node]
parents = {start_node: None}
total_cost = 0

while len(visited) != len(graph.keys()):
    min_node, min_cost, parent = find_min_node(visited)
    if min_node == None:
        break
    visited.append(min_node)
    total_cost += min_cost
print(total_cost)


# Q2) Email
# There are n SMTP servers connected by network cables. Each of the m cables connects two computers
# and has a certain latency measured in milliseconds required to send an email message. What
# is the shortest time required to send a message from server S to server T along a sequence of cables?
# Assume that there is no delay incurred at any of the servers.
# Input
# The first line of input gives the number of cases, N. N test cases follow. Each one starts with a line
# containing n (2 ≤ n ≤ 20000), m (0 ≤ m ≤ 50000), S (0 ≤ S < n) and T (0 ≤ T < n). S ̸= T. The
# next m lines will each contain 3 integers: 2 different servers (in the range [0, n − 1]) that are connected
# by a bidirectional cable and the latency, w, along this cable (0 ≤ w ≤ 10000).
# CCC Level 1 W21 Class 9 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec9HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname9HW with the source code for each one of the problems.
# Output
# For each test case, output the line ‘Case #x:’ followed by the number of milliseconds required to send
# a message from S to T. Print ‘unreachable’ if there is no route from S to T.
# Sample Input
# 3
# 2 1 0 1
# 0 1 100
# 3 3 2 0
# 0 1 100
# 0 2 200
# 1 2 50
# 2 0 0 1
# Sample Output
# Case #1: 100
# Case #2: 150
# Case #3: unreachable

# In[17]:


def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node

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
    costs = {}
    for x in graph.keys():
        for y in graph[x]:
            if x == start_node:
                costs[x] = 0
            else:
                costs[x] = float('inf')
    visited = []
    while True:
        min_node = find_min_node(costs, visited)
        if min_node == end_node:
            print('Case #' + str(x) + ': ' + str(costs[min_node]))
            break
        if min_node == None:
            print('Case #' + str(x) + ': unreachable')
            break
        visited.append(min_node)
        for x in graph[min_node].keys():
            c = costs[min_node] + graph[min_node][x]
            if c < costs[x]:
                costs[x] = c


# Who is taller?
# You have a few minutes before your class starts, and you decide to compare the heights of your
# classmates. You dont have an accurate measuring device, so you just compare relative heights between
# two people: you stand two people back-to-back, and determine which one of the two is taller.
# Conveniently, none of your classmates are the same height, and you always compare correctly (i.e., you
# never make a mistake in your comparisons).
# After you have done all of your comparisons, you would like to determine who the tallest person is
# between two particular classmates.
# Input
# The first line contains two integers N and M separated by one space. N, the number of people in the
# class, is an integer with 1 ≤ N ≤ 1000000. M, the number of comparisons that have already been done, is
# an integer with 1 ≤ M ≤ 10000000. Each of the next Mlines contains two distinct
# integers x and y (1 ≤ x, y ≤ N) separated by a space, indicating that person number x was determined to
# be taller than person number y. Finally, the last line contains two distinct integers p and q (1 ≤ p, q ≤ N)
# separated by one space: your goal is to determine, if possible, whether person p is taller than person q.
# Note that it may be the case that neither p nor q occur in the input concerning measurements between
# classmates, and each measurement between any two particular people will be recorded exactly once.
# Output
# The output is one line, containing one of three possible strings:
# • yes (if p is taller than q),
# • no (if q is taller than p),
# • unknown (if there is not enough information to determine the relative heights of p and q).
# Sample Input 1
# 10 3
# 8 4
# 3 8
# 4 2
# 3 2
# Sample Output 1
# yes
# Sample Input 2
# CCC Level 1 W21 Class 10 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec10HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname10HW with the source code for each one of the
# problems.
# 10 3
# 3 8
# 2 8
# 3 4
# 3 2
# Sample Output 2
# unknown

# In[237]:


def bfs(graph, start_node):
    visited = []
    visited.append(start_node)
    paths = [[start_node]]
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        for x in graph[current_node]:
            if x not in visited:
                visited.append(x)
                paths.append(current_path+[x])

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
visited = bfs(graph, int(line[0]))
if int(line[1]) in visited:
    print('yes')
else:
    visited = bfs(graph, int(line[1]))
    if int(line[0]) in visited:
        print('no')
    else:
        print('unknown')


# The Alaska Highway runs 1422 miles from Dawson Creek, British Columbia to Delta Junction, Alaska. Brenda would like to be the first person to drive her new electric car the length of the highway. Her car can travel up to 200 miles once charged at a special charging station. There is a charging station in Dawson Creek, where she begins her journey, and also several charging stations along the way. Can Brenda drive her car from Dawson City to Delta Juntion and back? 
# 
# Input Specification
# 
# The input contains several scenario. Each scenario begins with a line containing n, a positive number indicating the number of charging stations. n lines follow, each giving the location of a filling station on the highway, including the one in Dawson City. The location is an integer between 0 and 1422, inclusive, indicating the distance in miles from Dawson Creek. No two filling stations are at the same location. A line containing 0 follows the last scenario. 
# 
# 
# 
# 
# 
# Sample Input
# 
# 2
# 
# 0
# 
# 900
# 
# 8
# 
# 1400
# 
# 1200
# 
# 1000
# 
# 800
# 
# 600
# 
# 400
# 
# 200
# 
# 0
# 
# 0
# 
# Output Specification
# 
# For each scenario, output a line containing POSSIBLE if Brenda can make the trip. Otherwise, output a line containing the word IMPOSSIBLE. 
# 
# Output for Sample Input
# 
# IMPOSSIBLE
# 
# POSSIBLE

# In[67]:


a = int(input())
while a != 0:
    cs = []
    for x in range(a):
        cs.append(int(input()))
    cs = sorted(cs)
    count = 0
    for k, b in enumerate(cs):
        if k != len(cs) - 1:
            if cs[k + 1] - b <= 200:
                count += 1
                continue
            else:
                print('IMPOSSIBLE')
                break
        else:
            if 2 * (1422 - b) <= 200:
                count += 1
                continue
            else:
                print('IMPOSSIBLE')
                break
    if count == len(cs):
        print('POSSIBLE')
    a = int(input())


# In[ ]:


At an open-source fair held at a major university, leaders of open-source projects put sign-up sheets on the wall, with the project name at the top in capital letters for identification.

Students then signed up for projects using their userids. A userid is a string of lower-case letters and numbers starting with a letter.

The organizer then took all the sheets off the wall and typed in the information.

Your job is to summarize the number of students who have signed up for each project. Some students were overly enthusiastic and put their name down several times for the same project. That's okay, but they should only count once. Students were asked to commit to a single project, so any student who has signed up for more than one project should not count for any project.

There are at most 10,000 students at the university, and at most 100 projects were advertised.

Input Specification:

The input contains several test cases, each one ending with a line that starts with the digit 1. The last test case is followed by a line starting with the digit 0.

Each test case consists of one or more project sheets. A project sheet consists of a line containing the project name in capital letters, followed by the userids of students, one per line.

Output Specification:

For each test case, output a summary of each project sheet. The summary is one line with the name of the project followed by the number of students who signed up. These lines should be printed in decreasing order of number of signups. If two or more projects have the same number of signups, they should be listed in alphabetical order.

Sample input

UBQTS TXT

tthumb

LIVESPACE BLOGJAM

philton

aeinstein

YOUBOOK

j97lee

sswxyzy

j97lee

aeinstein

SKINUX

1

0

Output for Sample Input

YOUBOOK 2

LIVESPACE BLOGJAM 1

UBQTS TXT 1

SKINUX 0


# In[96]:


dict1 = {}
a = input()
while a != '0':
    b = a
    while b != '1':
        dict1[b] = []
        line = input()
        while line[0].isupper() == False:
            if line == '1':
                break
            dict1[b].append(line)
            line = input()
        b = line
    num_students = {}
    for x in dict1.keys():
        num_students[x] = list(set(dict1[x]))
    all_students = []
    for x in num_students.keys():
        all_students = all_students + num_students[x]
    visited = []
    bad_students = []
    for x in all_students:
        if x not in visited:
            visited.append(x)
            if all_students.count(x) > 1:
                bad_students.append(x)
    for x in bad_students:
        for y in num_students.keys():
            if x in num_students[y]:
                index = num_students[y].index(x)
                hi = num_students[y].pop(index)
    list1 = []
    for x in num_students:
        list1.append([len(num_students[x]), x])
    list1 = sorted(list1, key = lambda x:x[1])
    list1 = sorted(list1, key = lambda x:x[0], reverse = True)
    for x in list1:
        print(x[1], x[0])
    a = input()


# The first line contains two integers n and m (2 ≤ n ≤ 105, 0 ≤ m ≤ 105), where n is the number of vertices and m is the number of edges.
# 
# Following m lines contain one edge each in form ai,bi and wi (1≤ai,bi≤n,1≤wi≤106), where ai, bi are edge endpoints and wi is the length of the edge.
# 
# It is possible that the graph has loops and multiple edges between pair of vertices.
# 
# Output
# 
# Write the only integer -1 in case of no path. Write the shortest path in opposite case. If there are many solutions, print any of them.
# 
# 
# 
# Sample Inputs
# 
# 5 6 
# 
# 1 2 2 
# 
# 2 5 5 
# 
# 2 3 4 
# 
# 1 4 1 
# 
# 4 3 3 
# 
# 3 5 1 
# 
# 
# 
# 5 6 
# 
# 1 2 2 
# 
# 2 5 5 
# 
# 2 3 4 
# 
# 1 4 1 
# 
# 4 3 3 
# 
# 3 5 1 
# 
# Sample Outputs
# 
# 1 4 3 5 
# 
# 1 4 3 5

# In[107]:


def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node
for x in range(2):
    if x == 1:
        hi = input()
    line = input()
    line = [int(s) for s in line.split(' ')]
    end_node = line[0]
    edges = line[1]
    graph = {}
    for x in range(edges):
        line = input()
        line = [int(s) for s in line.split(' ')]
        if line[0] not in graph:
            graph[line[0]] = {}
        graph[line[0]][line[1]] = line[2]
    for x in range(1, end_node + 1):
        if x not in graph:
            graph[x] = {}
    start_node = 1

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
    list1 = [end_node]
    x = end_node
    while parents[x] != None:
        list1.append(parents[x])
        x = parents[x]
    for x in list1[::-1]:
        print(x, end = ' ')
    print('')


# In[ ]:


You've been snowed in at your summer residence. And without the Internet! Unfortunately, this means you're going to have rely on using the phone to get what you need to survive: pizza, pop, and the latest video games.

Often times, companies replace the digits in their phone numbers with characters to make their phone numbers more memorable. Because apparently, it's easier to remember 416-BUY-MORE than it is to remember 416-289-6673. Some companies even add extra digits or characters (like 604-PIZZABOX) but any digits after the 10th are irrelevant.

Since it's getting tedious to do the conversion by hand, write a program to help change all the phone numbers in your phone book to the form xxx-xxx-xxxx, using the below image to assist you.

 

Input

Input consists of a series of test cases. The first line consists of an integer t, the number of test cases. Following this are t lines consisting of alpha-numeric characters separated by hyphens, representing valid phone numbers. All letters will be in uppercase. No line is longer than 40 characters.

Output

For each test case, output the phone number in the form xxx-xxx-xxxx to the screen.

Sample Input

5

88-SNOW-5555

519-888-4567

BUY-MORE-POP

416-PIZZA-BOX

5059381123

Sample Output

887-669-5555

519-888-4567

289-667-3767

416-749-9226

505-938-1123


# In[110]:


n = int(input())
list_phones = []
for x in range(n):
    list_phones.append(input())
dict1 = {'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4, 'j':5, 'k':5, 'l':5, 'm':6, 'n':6,
        'o':6, 'p':7, 'q':7, 'r':7, 's':7, 't':8, 'u':8, 'v':8, 'w':9, 'x':9, 'y':9, 'z':9}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
for x in list_phones:
    x = x.lower()
    list1 = list(x)
    for y in list1:
        if y in alphabet:
            x = x.replace(y, str(dict1[y]))
    list1 = list(x)
    list1 = [m for m in list1 if m != '-']
    list1.insert(3, '-')
    list1.insert(7, '-')
    list1 = list1[:12]
    str1 = ''.join(list1)
    print(str1)


# Maximum Distance
# Consider two descending sequences of integers X[0..n-1] and Y[0..n-1] with X[i] ≥ X[i+1] and Y[i] ≥ Y[i+1]
# and for all i,
# 0 ≤ i < n - 1. The distance between two elements X[i] and Y[j] is given by
# d(X[i], Y[j]) = j - i if j ≥ i and Y[j] ≥ X[i], or 0 otherwise
# The distance between sequence X and sequence Y is defined by
# d(X, Y) = max{d(X[i], Y[j]) | 0 ≤ i < n, 0 ≤ j < n}
# You may assume 0 < n ≤ 100,000.
# For example, for the sequences X and Y below, their maximum distance is reached for i = 2 and j = 7, so
# d(X, Y) = d(X[2], Y[7]) = 5.
#  i=2
#  |
# v
#  X 8 8 4 4 4 3 3 3 1
# 
#  Y 9 9 8 8 6 5 5 4 3
#  ^
#  |
#  j=7
# Sample Input
# 2
# 9
# 8 8 4 4 4 3 3 3 1
# 9 9 8 8 6 5 5 4 3
# 7
# 6 5 4 4 4 4 4
# 3 3 3 3 3 3 3
# Sample Output
# The maximum distance is 5
# The maximum distance is 0
# CCC Level 1 W21 Class 11 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec11HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname11HW with the source code for each one of the
# problems. 

# In[115]:


test_cases = int(input())
dict_tests = {}
for k in range(test_cases):
    n = int(input())
    line = input()
    line2 = input()
    list1 = [int(s) for s in line.strip().split(' ')]
    list2 = [int(s) for s in line2.strip().split(' ')]
    maximum = 0
    for a, x in enumerate(list1):
        for b, y in enumerate(list2):
            if y < x:
                break
            if b >= a:
                if b - a > maximum:
                    maximum = b - a
    print('The maximum distance is ' + str(maximum))


# Attack of the CipherTexts
# Ruby is a code-breaker. She knows that the very bad people (Mr. X and Mr. Z) are sending secret
# messages about very bad things to each other.
# However, Ruby has managed to intercept a plaintext message and the corresponding ciphertext
# message. By plaintext, we mean the message before it was encrypted (i.e., readable English sentences),
# and by ciphertext, we mean the message after it was encrypted (i.e., gibberish). To encrypt a message,
# each letter is changed to a new letter, so that if you read the ciphertext message, it is not obvious what
# the plaintext message is.
# However, Ruby being the outstanding code-breaker she is, knows the algorithm that Mr. X and Mr. Z use.
# She knows they simply map one letter to another (possibly different) letter when they encrypt their
# messages. Of course, this map must be “one-to-one”, meaning that each plaintext letter must correspond
# to exactly one ciphertext letter, as well as “onto”, meaning that each ciphertext letter has exactly one
# corresponding plaintext letter.
# Your job is to automate Ruby’s codebreaking and help save the world.
# Input
# The input consists of 3 strings, with each string on a separate line. The first string is the plaintext
# message which Ruby knows about. The second string is the ciphertext message which corresponds to
# the plaintext message. The third string is another ciphertext message. You may assume that all strings
# have length of at least 1 character and at most 80 characters. You can also assume that there are only 27
# valid characters: the uppercase letters (‘A’ through ‘Z’) as well as the space character (‘ ’). That is, there
# will be no punctuation, lowercase letters, or special characters (like ‘!’ or ‘@’) in either the plaintext or
# ciphertext messages.
# Output
# The output is a (plaintext) string which corresponds to the second ciphertext input. It may not be possible
# to determine each character of the second ciphertext string, however. If this is the case, the output should
# have a period (‘.’) character for those letters which cannot be determined.
# Sample Input 1
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
# UIFARVJDLACSPXOAGPYAKVNQTAPWFSAUIFAMB ZAEPH
# XFABSFAWFSZACBEAQFPQMFAEPJOHAWFSZACBEAUIJOHTAIBAIB
# Sample Output
# WE ARE VERY BAD PEOPLE DOING VERY BAD THINGS HA HA
# CCC Level 1 W21 Class 11 HW.
# Write a Program to solve each one of the following problems. Name each question as mention in the
# question. Submit a zip file named as lastnamefirstnamec11HW contains the solution for each question.
# Submit a Google Doc called lastnamefirstname11HW with the source code for each one of the
# problems.
# Explanation for Sample Output 1
# Notice that every plaintext character is in the first message, and so, the entire mapping can be computed.
# Sample Input 2
# THERE ARE NOT ENOUGH LETTERS
# XQAZASEZASNYXSANYLWQSTAXXAZM
# JSCENNYXSIACYIASXQJM
# Sample Output 2
# . .ANNOT .E.O.E TH.S
# Explanation for Sample Output 2
# Notice that the characters that cannot be determined are the (ciphertext) letters J, C, I, since these
# ciphertext letters do not appear in the earlier ciphertext message. It turns out that the plaintext message
# for the last ciphertext was I C

# In[147]:


line = input()
list1 = list(line)
line = input()
list2 = list(line)
line = input()
list3 = list(line)
dict1 = {}
for k, x in enumerate(list2):
    if x not in dict1:
        dict1[x] = list1[k]
str1 = ''
for a in list3:
    if a not in dict1:
        str1 = str1 + '.'
        continue
    str1 = str1 + str(dict1[a])
print(str1)


# In[ ]:





# In[ ]:





# In[ ]:


def find_bottleneck_for_path(graph_res, path):
    min_value = float('inf')
    node = 's'
    index = path.index(node)
    while path[index + 1] != 't':
        value = graph_res[node][path[index + 1]]
        if value < min_value:
            min_value = value
        node = path[index + 1]
        index = path.index(node)
    return min_value

def update_res_graph(graph_res, path, bottleneck):
    for k, x in enumerate(path):
        if x == 't':
            break
        graph_res[x][path[k + 1]] = graph_res[x][path[k + 1]] - bottleneck
    path1 = path[::-1]
    for k, x in enumerate(path1):
        if x == 's':
            continue
        if x in graph_res:
            if path1[k + 1] in graph_res[x]:
                graph_res[x][path1[k + 1]] = graph_res[x][path1[k + 1]] + bottleneck
            else:
                graph_res[x][path1[k + 1]] = bottleneck
        else:
            graph_res[x][path1[k + 1]] = bottleneck
    return graph_res
def bfs(graph_res, start_node):
    visited1 = []
    visited1.append(start_node)
    paths = [[start_node]]
    while paths:
        current_path = paths.pop(0)
        current_node = current_path[-1]
        for x in graph_res[current_node]:
            if graph_res[current_node][x]>0:
                if x not in visited1:
                    if x == 't':
                        return current_path + [x]
                    visited1.append(x)
                    paths.append(current_path + [x])
    return None
            


# In[ ]:


start_node = 's'
end_node = 't'
while True:
    path = bfs(graph_res, start_node)
    if path==None:
        break
    bottleneck = find_bottleneck_for_path(graph_res, path)
    graph_res = update_res_graph(graph_res, path, bottleneck)
print(graph)
print(graph_res)
dict_flow = {}
for x in graph.keys():
    dict_flow[x] = {}
    for y in graph[x].keys():
        difference = graph[x][y] - graph_res[x][y]
        dict_flow[x][y] = difference
print(dict_flow)
count = 0
for a in dict_flow['s'].keys():
    count += dict_flow['s'][a]
print('Max Flow is', count)


# ## Bellman Ford

# In[1]:


graph = {}
graph[1] = {}
graph[1][2] = 2
graph[2] = {}
graph[2][3] = -10
graph[3] = {}
graph[3][4] = 3
graph[4] = {}
graph[4][1] = 7
graph[4][2] = -5


# In[73]:


import copy
def find_min_node(costs, visited):
    minimum_node = None
    minimum_cost = float('inf')
    for x in costs.keys():
        if x not in visited and costs[x] < minimum_cost:
            minimum_node = x
            minimum_cost = costs[x]
    return minimum_node

def bellman_ford(graph):
    list1 = []
    start_node = 1
    costs = {}
    for x in graph.keys():
        if x == start_node:
            costs[x] = 0
        else:
            costs[x] = float('inf')
    for y in range(len(graph.keys()) - 1):
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
        list1.append(copy.deepcopy(costs))
    first = list1[0]
    count = 0
    for x in list1:
        if x == first:
            count += 1
    if count == len(list1):
        return False
    else:
        return True
bellman_ford(graph)


# ## Shortest-path with Bellman-Ford algorithm

# In[20]:


def bellman_ford(graph, start_node):
    costs = {}
    costs = {}
    for node in graph.keys():
        if node==start_node:
            costs[node] = 0
        else:
            costs[node] = float('inf')
    for a in range(len(graph.keys())-1):
        for start_node in graph.keys():
            for end_node in graph[start_node].keys():
                if costs[start_node] + graph[start_node][end_node] < costs[end_node]:
                    costs[end_node] = costs[start_node] + graph[start_node][end_node]
    for a in range(len(graph.keys())-1):
        for start_node in graph.keys():
            for end_node in graph[start_node].keys():
                if costs[start_node] + graph[start_node][end_node] < costs[end_node]:
                    costs[end_node] = -1 * float('inf') 
    return costs


# In[21]:


graph = {}
graph[0] = {}
graph[0][1] = 5
graph[1] = {}
graph[1][2] = 20
graph[1][5] = 30
graph[1][6] = 60
graph[2] = {}
graph[2][3] = 10
graph[2][4] = 75
graph[3] = {}
graph[3][2] = -15
graph[4] = {}
graph[4][9] = 100
graph[5] = {}
graph[5][6] = 5
graph[5][8] = 50
graph[6] = {}
graph[6][7] = -50
graph[7] = {}
graph[7][8] = -10
graph[8] = {}
graph[9] = {}
bellman_ford(graph, 0)


# In[22]:


visited2 = []
list_nodes = graph.keys()
for node in list_nodes:
    if node not in visited2:
        visited = []
        dfs(node)
        for s in visited:
            if s not in visited2:
                visited2.append(s)
print(visited2)


start_node = 0
costs = {}
for x in graph.keys():
    if x == start_node:
        costs[x] = 0
    else:
        costs[x] = float('inf')
for node in visited2:
    neighbours = graph[node].keys()
    for a in neighbours:
        c = costs[node] + graph[node][a]
        if c < costs[a]:
            costs[a] = c
print(costs)


# ## String Manipulation 1 [Programming Competition Problems]

# In[ ]:


'''
input:
3
this is a test
football
all your case

output:
case 1: test a is this
case 2: football
case 3: case your all
'''


# In[100]:


n = int(input())
for x in range(n):
    list1 = input()
    list1 = list1.split(' ')
    for y in list1[::-1]:
        print(y, end = ' ')
    print('')


# In[104]:


n = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']
for x in range(1, n + 1):
    str1 = input()
    list1 = list(str1)
    if list1[-1] in vowels:
        print('Case ' + str(x) + ': ' + str1 + ' is ruled by a queen.')
    elif list1[-1] == 'y':
        print('Case ' + str(x) + ': ' + str1 + ' is ruled by nobody.')
    else:
        print('Case ' + str(x) + ': ' + str1 + ' is ruled by a king.')


# In[124]:


n = int(input())
for x in range(1, n + 1):
    line = input()
    line = line.split(' ')
    done = int(line[0])
    not_done = int(line[1])
    list1 = []
    for y in range(not_done + done):
        list1.append(input())
    sublist1 = list1[:done]
    sublist2 = list1[done:]
    for k, z in enumerate(sublist1):
        sublist1[k] = z.split('/')[1:]
    for k, z in enumerate(sublist2):
        sublist2[k] = z.split('/')[1:]
    if sublist2 == []:
        print('Case ' + str(x) + ': 0')
    elif sublist1 == []:
        list1 = []
        for a in sublist2:
            for b in a:
                list1.append(b)
        count = len(list(set(list1)))
        print('Case ' + str(x) + ': ' + str(count))
    else:
        count = 0
        for a in sublist2:
            for b in a:
                for c in sublist1:
                    if b not in c:
                        count += 1
        print('Case ' + str(x) + ': ' + str(count))


# In[119]:


sublist1


# In[117]:


list1 = ['/home/gcj/finals', '/home/gcj/quads']
for x in list1:
    x = x.split('/')[1:]
print(list1)


# In[ ]:


Word Frame
The following program asks you to take a single word and use it to form a simple square frame,
where the word is printed four times, once each for one of the four sides of the square: The
corners and the centre of the square must contain stars. On top of the square the word is printed
from left to right, containing a single space between letters as shown in the sample. On the
bottom of the square the word is printed from right to left, also with spaces between letters. On
the right the word reads from top to bottom without blank spaces and on the left the word reads
from botom to top.
DATA11.txt (DATA12.txt for the second try) contains 5 words on 5 separate lines. Each word
contains less than 20 characters. Write a program to create a square as described above for
each word. The program should pause between squares and proceed to the next one under input
control
Sample Input:
CANADA
MAPLE
TO
FIRE
SHORT
Sample Output:
* C A N A D A *
A * * * * * * C
D * * * * * * A
A * * * * * * N
N * * * * * * A
A * * * * * * D
C * * * * * * A
* A D A N A C *
* M A P L E *
E * * * * * M
L * * * * * A
P * * * * * P
A * * * * * L
M * * * * * E
* E L P A M *
* T O *
O * * T
T * * O
* O T *
* F I R E *
E * * * * F
R * * * * I
I * * * * R
F * * * * E
* E R I F *
* S H O R T *
T * * * * * S
R * * * * * H
O * * * * * O
H * * * * * R
S * * * * * T
* T R O H S *


# In[134]:


list1 = []
for x in range(5):
    a = input()
    a = list(a)
    list1.append(a)
for x in list1:
    list2 = ['']*(len(x) + 2)
    list2[0] = list2[0] + '* '
    list2[-1] = list2[-1] + '* '
    for k, a in enumerate(x):
        list2[0] = list2[0] + a + ' '
        list2[-1] = list2[-1] + x[-1 * (k + 1)] + ' '
    list2[0] = list2[0] + '*'
    list2[-1] = list2[-1] + '*'
    str1 = ' *' * len(x)
    for k, a in enumerate(x):
        list2[k + 1] = list2[k + 1] + x[-1 * (k + 1)] + str1 + ' ' + a
    for b in list2:
        print(b)


# In[177]:


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


# In[178]:


list1 = [-10,100,23,45,123,67,89]


# In[179]:


heap = MinHeap()
list2 = []
for x in list1:
    heap.add(x)
for x in range(len(list1)):
    list2.append(heap.remove())
print(list2)


# In[95]:


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

    def add(self, node):
        self.data.append(node)
        self.heapify()
        self.size += 1

    def printing(self):
        for x in self.data[1:]:
            print(x, end = ' ')
        print('')


# In[ ]:


list1 = []
for x in range(52):
    n = input()
    list1.append(n)
player1 = 0
player2 = 0
low_cards = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
for k, x in enumerate(list1):
    length = len(list1)
    if x == 'jack':
        if len(list1) - 1 > k:
            if list1[k + 1] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 1 point(s).')
                    player1 += 1
                else:
                    print('Player B scores 1 point(s).')
                    player2 += 1
    elif x == 'queen':
        if len(list1) - 2 > k:
            if list1[k + 1] in low_cards and list1[k + 2] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 2 point(s).')
                    player1 += 2
                else:
                    print('Player B scores 2 point(s).')
                    player2 += 2
    elif x == 'king':
        if len(list1) - 3 > k:
            if list1[k + 1] in low_cards and list1[k + 2] in low_cards and list1[k + 3] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 3 point(s).')
                    player1 += 3
                else:
                    print('Player B scores 3 point(s).')
                    player2 += 3
    elif x == 'ace':
        if len(list1) - 4 > k:
            if list1[k + 1] in low_cards and list1[k + 2] in low_cards and list1[k + 3] in low_cards and list1[k + 4] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 4 point(s).')
                    player1 += 4
                else:
                    print('Player B scores 4 point(s).')
                    player2 += 4
    else:
        continue
print('Player A: ' + str(player1) + ' point(s).')
print('Player B: ' + str(player2) + ' point(s).')


# In[69]:


str1 = """three
seven
queen
eight
five
ten
king
eight
jack
queen
six
queen
jack
eight
seven
three
ten
four
king
nine
six
seven
ace
four
jack
ace
ten
nine
ten
queen
ace
king
seven
two
five
two
five
nine
three
king
six
eight
jack
six
five
four
two
ace
four
three
two
nine"""
list1 = str1.split('\n')
player1 = 0
player2 = 0
low_cards = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
for k, x in enumerate(list1):
    length = len(list1)
    if x == 'jack':
        if len(list1) - 1 > k:
            if list1[k + 1] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 1 point(s).')
                    player1 += 1
                else:
                    print('Player B scores 1 point(s).')
                    player2 += 1
    elif x == 'queen':
        if len(list1) - 2 > k:
            if list1[k + 1] in low_cards and list1[k + 2] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 2 point(s).')
                    player1 += 2
                else:
                    print('Player B scores 2 point(s).')
                    player2 += 2
    elif x == 'king':
        if len(list1) - 3 > k:
            if list1[k + 1] in low_cards and list1[k + 2] in low_cards and list1[k + 3] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 3 point(s).')
                    player1 += 3
                else:
                    print('Player B scores 3 point(s).')
                    player2 += 3
    elif x == 'ace':
        if len(list1) - 4 > k:
            if list1[k + 1] in low_cards and list1[k + 2] in low_cards and list1[k + 3] in low_cards and list1[k + 4] in low_cards:
                if k % 2 == 0:
                    print('Player A scores 4 point(s).')
                    player1 += 4
                else:
                    print('Player B scores 4 point(s).')
                    player2 += 4
    else:
        continue
print('Player A: ' + str(player1) + ' point(s).')
print('Player B: ' + str(player2) + ' point(s).')


# Problem J2: 9966
# The digits 0, 1, and 8 look much the same if rotated 180 degrees on the page (turned upside down). Also,
# the digit 6 looks much like a 9, and vice versa, when rotated 180 degrees on the page. A multi-digit
# number may also look like itself when rotated on the page; for example 9966 and 10801 do, but 999 and
# 1234 do not.
# You are to write a program to count how many numbers from a given interval look like themselves when
# rotated 180 degrees on the page. For example, in the interval [1..100] there are six : 1, 8, 11, 69, 88, and
# 96.
# Your program should take as input two integers, m and n, which define the interval to be checked, 1
# ≤ m ≤ n ≤ 32000. The output from your program is the number of rotatable numbers in the interval.
# You may assume that all input is valid.
# Sample Input
# 1
# 100
# Sample Output
# 6

# In[89]:


minimum = int(input())
maximum = int(input())
list1 = ['0', '1', '6', '8', '9']
count = 0
for x in range(minimum, maximum + 1):
    list2 = list(str(x))
    count2 = 0
    count_9 = 0
    count_6 = 0
    for y in list2:
        if y in list1:
            if y != '6' and y != '9':
                count2 += 1
            elif y == '6':
                count_6 += 1
            else:
                count_9 += 1
    if count_9 > 0 and count_6 > 0:
        if count_9 == count_6:
            count += 1
    if count2 == len(list2):
        if list2 == list2[::-1]:
            count += 1
        else:
            if count_9 > 0:
                count += 1
print(count)

