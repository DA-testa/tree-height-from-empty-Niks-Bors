# python3

import sys
import threading
import numpy
def read(self)
self.n=int(sys.stdin.readline())
self.parent =list(map(int,sys.stdin.readline().split()))
self.nodes = None
self.root = None
def build_tree(self):
    self.nodes = [ [] for i in range(self.n)]
for child_index in range(self.n):
    parent_index = self.parent[child_index]
    if parent_index == -1:
        self.root = child_index
    else:
        self.nodes[parent_index].append(child_index)
def get_max_height(self, current, height):
    if not self.nodes[current]:
        return height
    max_height = 0
    for c in self.nodes[current]:
        max_height = max(max_height,self.get_max_height(c,height+1))
    return max_height

#def compute_height(n, parents):
def compute_height(self):
    self.build_tree()
    return self.get_max_height(self.root, 1)    
   # max_height = 0
    # Your code here
    #return max_height


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())
    # text = input()
   # if "F" in text:
       # fileName = input()
       # file = open(fileName, "r")
       # print(file)
    
    #elif "a" in text:
       # text = input()
        #ms = find_mismatch(text)
       # print(ms)
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))