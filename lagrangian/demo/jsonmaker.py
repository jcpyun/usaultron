from threading import Thread
import urllib
import re
import json
import time
import math 
import itertools
"""
def bfsTree(t):
    curnode=t
    nextline=[]
    output=[]
    while (curnode):
        output.append(curnode.data)
        nextline.append(curnode.left)
        nextline.append(curnode.right)
        curnode=nextline[0]
        del nextline[0]
    print output
"""
class Node:
    def __init__(self,name, sex,parent=None,image=None):
        self.name=name
        self.sex=sex
        self.image=image
        self.parent=parent
        self.children=[]
class FamilyTree:
    def __init__(self):
        self.root=None
    def insert(self,node):
        if node.parent==None:
            tempn=node
            self.root=tempn
        else:
            curnode=self.root
            nextline=[]
            while (curnode):
                if curnode.name==node.parent:
                    curnode.children.append(node)
                    break
                else:
                    nextline.append(curnode.children)
                    curnode=nextline[0]
                    del nextline[0]

    def export(self):
        curnode=self.root
        nextline=[]
        output={}
        
        while (curnode):
            curobject={}
            print curnode.name,"shit"
            curobject.setdefault("name",curnode.name)
            curobject.setdefault("sex",curnode.sex)
            curobject.setdefault("children",curnode.children)
            output.setdefault("member",curobject)
            nextline=(curnode.children)
            print nextline
            if nextline==[]:
                break
            curnode=nextline[0]
            del nextline[0]
            print "poop"
        return output



John=Node("John Pyun","male")
Bob=Node("Bob Pyun","male","John Pyun")
JohnTree=FamilyTree()
JohnTree.insert(John)
# print JohnTree.root.name
JohnTree.insert(Bob)
# print JohnTree.root.children[0].name
print JohnTree.export()
            
            
    

        

def memberobject(firstname,lastname,sex,image=None):
    membertree={}
    membertree.setdefault("firstname",firstname)
    membertree.setdefault("lastname",lastname)
    membertree.setdefault("sex",sex)
    membertree.setdefault("image",image)
    return membertree
# print memberobject("john","pyun","male")

def nestedtry(x,partner,child):
    familytree={}
    familytree.setdefault("member",x)
    familytree.setdefault("partner",partner)
    familytree.setdefault("child",child)
    return familytree
"""
class Person:
    ID = itertools.count()
    def __init__(self, name, parent=None, level=0):
        self.id = self.__class__.ID.next() # next(self.__class__.ID) in python 2.6+
        self.parent = parent
        self.name = name
        self.level = level
        self.children = []
john=Person("john")

def createTree(d, parent=None, level=0):
    if d:
        member = Person(d['parent'], parent, level)
        level = level + 1
        member.children = [createTree(child, member, level) for child in d['children']]
        return member
print createTree(john)

"""

# def flatten(parent):
#     L = [parent]
#     for child in parent.children:
#         L += flatten(child)
#     return L
# flattened_tree = flatten(t)
# print "all members",[person.name for person in flattened_tree]


"""

def createTree(d, parent=None, level=0):
    if d:
        member = Person(d['parent'], parent, level)
        level = level + 1
        member.children = [createTree(child, member, level) for child in d['children']]
        return member

t = createTree(my_tree)          # my_tree is the name of your dictionary
def printout(parent, indent=0):
    print '\t'*indent, parent.name
    for child in parent.children:
        printout(child, indent+1)        
printout(t)

def flatten(parent):
    L = [parent]
    for child in parent.children:
        L += flatten(child)
    return L
flattened_tree = flatten(t)
print "All members: ", [person.name for person in flattened_tree]
print "Number of members:", len(flattened_tree)
print "Number of levels:", max([person.level for person in flattened_tree]) + 1
cooper = flattened_tree[6]
cooper_fl = flatten(cooper)
print "Members below Cooper: ", [person.name for person in cooper_fl]
print "Number:", len(cooper_fl)
levels = [person.level for person in cooper_fl]
print "Number of levels:", max(levels) - min(levels) + 1

"""