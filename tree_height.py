# python3

import sys
import threading
import numpy  
def compute_height(n,parent):
    max_height =0
    for j in range(n):
        z=j
        pag =1
        while (parent[z] != -1):
            pag+=1
            z=parent[z]
        max_height = max(max_height,pag)

    return max_height




   
   #l = compute_height.parent
   #while l:
        #max_height +=1
        #l=l.parent
     #Your code here
    #return max_height


def main():
    text = input("Ievadat:")
    if "F" in text:
        fileName = input()
        if ".a" in fileName:
            return
        if ".a" not in fileName:
            fileName = "test/"+fileName
            with open(fileName, 'r') as file:
                n = int(file,readline())
            tree = compute_height(n,parent)
            print(tree)
    elif "I" in text:
        n = int(input())
        parent = list(map(int.input().split()))

    
    
    
    #tree.read()
    
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