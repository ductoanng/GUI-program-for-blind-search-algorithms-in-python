#!/usr/bin/env python
# coding: utf-8

# In[15]:


# import everything from tkinter module
from tkinter import *
from collections import defaultdict
# globally declare the expression variable

# Using graph data structure
class Graph:
    
    # Constructor
    def __init__(self):
        #Lead to reset()
        self.reset()
    
    # Reset the object
    def reset(self):
        self.graph = defaultdict(list)
    
    # Check empty
    def isEmpty(self):
        return len(self.graph) == 0
    
    # Function to add an edge to the tree
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Breadth-First Search Algorithm
    def BFS(self, s):
        
        resultBFS=""
        # Mark all the nodes as not visited in a list
        visitedBFS = [False] * (len(self.graph)+10000) 
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visitedBFS[s] = True
 
        while queue:
            # Dequeue a node from queue and add it to the result string
            s = queue.pop(0)
            resultBFS = resultBFS + str(s)+" "
 
            # Get all children of the dequeued vertex s. 
            for i in self.graph[s]:
                # If the node is not visited, then enqueue it and mark it visited
                if visitedBFS[i] == False:
                    queue.append(i)
                    visitedBFS[i] = True
        
        # Return string value, which is the list searched by BFS
        return resultBFS   
    
    #Depth-First Search Algorithm
    
    # Create global list of elements searched by DFS and their states
    DFSlist=[]
    visitedDFS = []
    
    def DFS(self, v):
        
        # Globalize the variables
        global visitedDFS
        global DFSlist
        
        # Mark the current node as visited
        visitedDFS[v]= True
        DFSlist.append(v)

        # Using recursion for all the nodes adjacent to this vertex
        for i in self.graph[v]:
            # If the node is unvisited, then do the recursion for it
            if visitedDFS[i] == False:
                self.DFS(i)
     
    def printDFS(self,v):
        
        global DFSlist
        global visitedDFS
        
        # Mark all the nodes as not visited in a list
        visitedDFS = [False] * (len(self.graph)+10000) 
        DFSlist=[]
        
        resultDFS=""
        self.DFS(v)
        
        # After running the DFS() function, 
        # we get the searched list and change it into string
        for i in DFSlist:
            resultDFS = resultDFS + str(i) + " "
            
        # Return string value, which is the list searched by DFS    
        return resultDFS
    
    
    #Iterative Deepening Algorithm
    
    # Create global list of elements searched by IDS and their states
    IDSlist=[]
    visitedIDS = []
    
    def IDS(self, v, height_limit):
        
        global visitedIDS
        global IDSlist
        
        # IF the height_limit less than 0, break out the function
        if height_limit < 0:
            return
        
        # Mark the current node as visited
        visitedIDS[v]= True
        IDSlist.append(v)

        # Using recursion for all the nodes adjacent to this vertex
        for i in self.graph[v]:
            # If the node is unvisited, then do the recursion for it and decrease the height by 1
            if visitedIDS[i] == False:
                self.IDS(i, height_limit-1)
     
    def printIDS(self,v,max_height):
        
        global IDSlist
        global visitedIDS
        
        # Mark all the nodes as not visited in a list
        visitedIDS = [False] * (len(self.graph)+10000) 
        IDSlist=[]
        
        resultIDS=""
        self.IDS(v,max_height)
        
        # After running the IDS() function, 
        # we get the searched list and change it into string
        for i in IDSlist:
            resultIDS = resultIDS + str(i) + " "
            
        # Return string value, which is the list searched by IDS    
        return resultIDS
    
# Main program
if __name__ == "__main__":
    tree = Graph()
    gui = Tk()
    gui.title("Tree Search Algorithms")
    gui.geometry("500x420")
    
    lb1 = Label(gui,text="Edge table:")
    lb1.grid(row=0,column=0)
    
    lb2 = Label(gui,text="Search table:")
    lb2.grid(row=0,column=1)
    
    edgeTable = Text(gui, height=10, width=30)
    edgeTable.grid(row=1, column=0)
    
    searchTable = Text(gui, height=10, width=30)
    searchTable.grid(row=1, column=1)
    
    root = 0
    d = 0
    
    # Adding edge function in GUI
    def new():
        searchTable.delete("1.0","end")
        u = str(EntryU.get())
        v = str(EntryV.get())
        
        EntryU.delete(0,"end")
        EntryV.delete(0,"end")
        
        global d
        global root
        
        #Choosing the u node in the first edge to be the root
        d += 1
        if d == 1:
            root = int(u)
            searchTable.insert("end","The root is "+str(root))
        
        # Checking valid input
        if  u != "" and v != "":
            
            # If another node points to root
            if int(v) == root:
                searchTable.insert("end","Error! Cannot add new edge point to root! Please enter another edge!")
                edgeTable.delete("end")
                return
            
            # Add edge
            edgeTable.insert("end", u +" --> "+ v +"\n")
            tree.addEdge(int(u),int(v))
            
        else: 
            searchTable.delete("1.0","end")
            searchTable.insert("end","Wrong input! Please reset and enter again!")
        
    
    # Reset function in GUI
    def clear():
        edgeTable.delete("1.0","end")
        searchTable.delete("1.0","end")
        tree.reset()
        EntryU.delete(0,"end")
        EntryV.delete(0,"end")
        EntryIDS.delete(0,"end")
        Lb.delete(0,"end")
        Lb.insert(1, 'Breadth-First')
        Lb.insert(2, 'Depth-First')
        Lb.insert(3, 'Iterative deepening')
        
        global d
        d=0
     
    # Generate BFS() list 
    def bfs():
        global root
        searchTable.delete("1.0","end")
        if (tree.isEmpty()):
            searchTable.insert("end", "The tree is empty now! Please input the edges!")
        else:
            searchTable.insert("end",tree.BFS(root)+"\n")
    
    # Generate DFS() list
    def dfs():
        global root
        searchTable.delete("1.0","end")
        if (tree.isEmpty()):
            searchTable.insert("end", "The tree is empty now! Please input the edges!")
        else:
            searchTable.insert("end",tree.printDFS(root)+"\n")
    
    # Generate IDS() list        
    def ids():
        global root
        h = EntryIDS.get()
        searchTable.delete("1.0","end")
        if (tree.isEmpty()):
            searchTable.insert("end", "The tree is empty now! Please input the edges!")
        else:
            if str(h) == "":
                searchTable.insert("end", "Please enter the height limit for IDS")
            else:
                searchTable.insert("end",tree.printIDS(root,int(h))+"\n")
    
    
    lb3 = Label(gui,text="Add new edge (U,V):")
    lb3.grid(row=2,column=0)
    
    lbU = Label(gui,text="U = ")
    lbU.grid(row=3,column=0)
    lbV = Label(gui,text="V = ")
    lbV.grid(row=4,column=0)
    EntryU = Entry(gui)
    EntryV = Entry(gui)
    EntryU.grid(row=3, column=1)
    EntryV.grid(row=4, column=1)
    
   
    addButton = Button(gui, text=' Add ', fg='black', bg='red',
                        command=new, height=1, width=7)

    addButton.grid(row=5, column=1)
    
    lb4 = Label(gui,text="Want to reset?")
    lb4.grid(row=6,column=0)
    resetButton = Button(gui, text=' Reset ', fg='black', bg='red',
                        command=clear, height=1, width=7)
    resetButton.grid(row=6,column=1)
    
    lb5 = Label(gui,text="Choose the search algorithm")
    lb5.grid(row=7,column=0)
    
    Lb = Listbox(gui, height=3)
    Lb.insert(1, 'Breadth-First')
    Lb.insert(2, 'Depth-First')
    Lb.insert(3, 'Iterative deepening')
    Lb.grid(row=7, column=1)
    
    lb6 = Label(gui,text="Depth limit for Iterative Deepening Search")
    lb6.grid(row=8,column=0)
    
    EntryIDS = Entry(gui)
    EntryIDS.grid(row=8,column=1)
    
    def select():
        for i in Lb.curselection():
            if i == 0:
                bfs()
            if i == 1:
                dfs()
            if i == 2:
                ids()
    
    searchButton = Button(gui, text=' Search ', fg='black', bg='red', command=select,
                              height=1, width=7)
    searchButton.grid(row=9,column=1)
    
    gui.mainloop()


# In[ ]:




