# python3

import sys
import threading
import numpy  
def limenavektors(z,n,parent):  
    if(parent[z] == -1):
        return 1
    if(height[z]!=-1):
        return height[z]
    height[z]=limenavektors(parent[i], parent, height)+1
    return height[i]
def compute_height(n,parent):
    max_height = 0
    height = [-1]*(n)
    for j in range(n):
        max_height = max(res, rec(z, parent, height))

    return max_height




   
   #l = compute_height.parent
   #while l:
        #max_height +=1
        #l=l.parent
     #Your code here
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